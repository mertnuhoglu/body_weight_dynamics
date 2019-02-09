from django.db import models
from sim import modelparser_vensim
from django.contrib.auth.models import User

import re
import copy
from sim import graph
from sim.bunch import Bunch
from copy import deepcopy 

class GameDefinition(models.Model):
    """This represents the original mathematical model. """
    original_text = models.TextField()
    name = models.CharField(max_length = 500)
    slug = models.SlugField(unique = True)
    game_description = models.TextField()
    purpose = models.TextField()

    def __unicode__(self):
        return u"GameDefinition: %s" % self.name

    def save(self):
        from datetime import datetime
        self.slug = slugify(datetime.today().strftime('%Y%m%d%H%M') + '_' + self.name)
        super(GameDefinition, self).save()

    def build_model_python(self):
        (eqns_in, eqns_stocks_in, stock_inits_in, mappings_in) = modelparser_vensim.convert(text = self.original_text)
        result = ModelPython()
        result.eqns = eqns_in
        result.eqns_stocks = eqns_stocks_in
        result.stock_inits = stock_inits_in
        result.game_definition = self
        return result, mappings_in

    def get_absolute_url(self):
# todo: make this independent of the host       
        return 'http://localhost:8000/mashap/introduce_game/%s/' % self.slug

    @property
    def model_python(self): return self.modelpython_set.all()[0]

    @property
    def model_definition(self): return self.model_python.model_definition
    @property
    def time_settings(self): return self.model_definition.time_settings
    @property
    def total_game_time(self): return self.time_settings.total_game_time
    @property
    def num_decisions(self): return len(self.model_definition.decision_variables)
    @property
    def time_between_decision_steps(self): return '%d'%(self.time_settings.time_between_decision_steps)

class ModelPython(models.Model):
    """This represents the model in python text"""

    eqns = models.TextField()
    eqns_stocks = models.TextField()
    stock_inits = models.TextField()
    game_definition = models.ForeignKey(GameDefinition)

    def __unicode__(self):
        return u"ModelPython %s" % self.id

    @property
    def model_definition(self):
            return self.modeldefinition_set.all()[0]

class ModelDefinition(models.Model):
    model_python = models.ForeignKey(ModelPython)

    def __unicode__(self):
        return u"ModelDefinition %s" % self.id

    def store_variable_run_data_for_stocks(self, X, time):
        '''ModelDefinition doesn't store data. ModelInstance stores.
        implemented due to duck typing'''
        pass

    @property
    def output_groups(self):
        # dict[var_name,formula]
        if not hasattr(self, '_output_groups_cache'):
            self._output_groups_cache = self.outputgroup_set.all()
        return self._output_groups_cache

    @property
    def variables(self):
        # dict[var_name,formula]
        if not hasattr(self, '_variables_cache'):
            self._variables_cache = dict([(var.name, var.formula) for var in self.variable_set.filter(is_stock=False)])
            self._variables_cache['time_step'] = str(0.5)
        return self._variables_cache

    @property
    def variable_map(self):
        if not hasattr(self, '_variable_map_cache'):
            self._variable_map_cache = dict([(var.name, var) for var in self.variable_set.all()]) # dict[var_name, var_object]
        return self._variable_map_cache

    @property
    def stock_set(self):
        if not hasattr(self, '_stock_set_cache'):
            self._stock_set_cache = [var for var in self.variable_set.filter(is_stock=True)]
        return self._stock_set_cache

    @property
    def stocks(self):
    # dict[stock_name,formula] ex: {'Protein': '+ Flow_P'}
        if not hasattr(self, '_stocks_cache'):
            self._stocks_cache = dict([(var.name, var.formula) for var in self.stock_set])
        return self._stocks_cache

    @property
    def stock_map(self):
        if not hasattr(self, '_stock_map_cache'):
            self._stock_map_cache = dict([(var.name, var) for var in self.stock_set]) # dict[stock_name, stock_object]
        return self._stock_map_cache

    @property
    def stock_inits(self):
    # dict[stock_name,initial_value]
        if not hasattr(self, '_stock_inits_cache'):
            self._stock_inits_cache = dict([(var.name, var.init_value) for var in self.stock_set])
        return self._stock_inits_cache

    @property
    def levels(self):
    # list[stock] ex: ['Protein'] sorted
        if not hasattr(self, '_levels_cache'):
            dependencies = self.find_dependencies(self.variables)			# dict[var_name,set(variable_names)]
            dependencies_with_stocks = copy.deepcopy( dependencies )
            dependencies_with_stocks.update( self.find_dependencies(self.stocks) )
            self.effects = dict([(var, self.find_dependents(dependencies, [var])) for (var, value) in dependencies.items()])
    #        (self.deps_without_stocks, self.effects) = self.add_timestep(self.deps_without_stocks, self.effects)
            self._levels_cache = graph.topological_sorting( self.deps_without_stocks, self.effects)
        return self._levels_cache

    @property
    def deps_without_stocks(self):
#       causes of the variables
#       dict{'var_name',set('cause_1','cause_2')}   
        if not hasattr(self, '_deps_without_stocks_cache'):
            dependencies = self.find_dependencies(self.variables)			# dict[var_name,set(variable_names)]
            self._deps_without_stocks = self.remove_dependency_on_stock( dependencies, self.stocks )
        return self._deps_without_stocks

    @property
    def stock_names(self):
        if not hasattr(self, '_stock_names_cache'):
            self._stock_names_cache = sorted(self.stocks.keys())
        return self._stock_names_cache

    @property
    def stock_bunches(self):
    # Bunch(name='Protein', pattern=r'\bProtein\b', replace=r'X[0]', init=7500)
        if not hasattr(self, '_stock_bunches_cache'):
            self._stock_bunches_cache = [Bunch(name=s, pattern=r'\b%s\b'%s, replace=r'stock_var__[%d]'
                % self.stock_names.index(s), init=self.stock_inits[s]) for s in self.stock_names]
        return self._stock_bunches_cache

    @property
    def eqns_sorted(self): return self.eqns_writer.eqns_sorted

    @property
    def eqns_stocks(self):
        if not hasattr(self, '_eqns_stocks_cache'):
            self._eqns_stocks_cache = [s + ' = ' + self.stocks[s] for s in self.stocks.keys()]
        return self._eqns_stocks_cache

    @property
    def differentials(self):
        # list[formula] ex: ['+ Flow_P'...] sorted
        if not hasattr(self, '_differentials_cache'):
            self._differentials_cache = [self.stocks[b.name] for b in self.stock_bunches]
        return self._differentials_cache

    @property
    def constant_vars_idmap(self):
        # dict[var.id, 'var_name [unit], description']
        if not hasattr(self, '_constant_vars_idmap_cache'):
            constant_vars = graph.find_independent_vars(self.deps_without_stocks)
            var_descriptions = []
            for var_name in constant_vars:
                var = self.variable_map[var_name]
                var_description = '%s         [%s], %s' % (var.name, var.unit, var.description)
                var_descriptions.append((var.id, var_description))
            self._constant_vars_idmap_cache = dict(var_descriptions)
        return self._constant_vars_idmap_cache

#    def __init__(self, variables={}, rates={}, stocks={}, stock_inits={}, *args, **kwargs):
#        super(Model, self).__init__(*args, **kwargs)

    @property
    def eqns_writer(self):
        if not hasattr(self, '_eqns_writer_cache'):
            self._eqns_writer_cache = EqnsWriter(self)
        return self._eqns_writer_cache

    @property
    def time_settings(self):
        if not hasattr(self, '_time_settings_cache'):
            self._time_settings_cache = TimeSettings.objects.get(model=self)
        return self._time_settings_cache
    @property
    def decision_period(self): return self.time_settings.time_between_decision_steps
    @property
    def record_period(self): return self.time_settings.record_period
    @property
    def time_step(self): return float(Variable.objects.get(model=self,name='time_step').formula)
    @property
    def decision_variables(self): return Variable.objects.filter(model=self,is_decision=True)

    def init_values(self):
#       This method initializes stocks. This method has to be called only at the beginning of the simulation.
#       At every decision step, this method should be overridden.
        result = []

#        dolayli referanslar olabileceginden, tum sabit degiskenlerin degerlerini hesaplamaliyiz
#        constant_vars = self.constant_vars_idmap.values()
#        for varname in constant_vars:
#            exec(varname + '=' + self.eqns_writer.dict_scipy[varname])
        for b in self.stock_bunches:
            if isfloat(b.init):
                result.append(float(b.init))
            else:
                #todo: burada matematiksel bir ifade olabilir. tum ifadeleri dikkate al: c_b + c_x gibi
                result.append(self.eval_formula(b.init))
        return result

    def eval_formula(self, formula):
# c = c_init
# c_init = c_b
# c_b = 400
# in this case, this function returns 400 for the input 'c_init'
        causes = self.find_vars(formula)
        for var in causes:
            formula_of_cause = self.eqns_writer.dict_scipy[var]
            exec(var+'='+str(self.eval_formula(formula_of_cause)))
        exec('result='+formula)
        return result

    def write_eqns_sorted(self):
        open('eqns_sorted.txt','wb').write('\n'.join(self.eqns_sorted))

    def __str__(self):
        result = "variables:\n" + self.variables.__str__() + "\nstock flows:\n" + self.stocks.__str__()
        return result

    def find_dependencies(self, formulas):
#       finds the causes of the variables
#       {'var_name',set('dep_1','dep_2') where
#       var_name = f(dep_1, dep_2)
        return dict([ (name, set(self.find_vars(formulas[name])) ) for name in formulas.keys() ] )

    def find_vars(self, formula):
        # match variables, exclude function calls and 't'
        # eg: 'max(x) + t' match: 'x' exclude 'max' 't'
        # eg: 'scipy.interpolate.UnivariateSpline(pts_x_0)' match: 'pts_x_0' exclude 'scipy.interpolate.UnivariateSpline'
# todo: keywordleri disaridan al
        variable_name_pattern = re.compile(r'((?!\bin\b|\bfor\b|\bif\b|\belse\b|\barray\b|\b__x\b|\b__y\b)(?!\b(?=\D)\w+(\.\w+)*\s*(?=\())(?!\bt\b)\b(?=\D)\w+)')
        return [item[0] for item in variable_name_pattern.findall(formula)]

    def find_dependents(self, dependencies, vars):
        result = []
        for variable in vars:
            result += [name for (name, value) in dependencies.items() if variable in value]
        return set(result)

    def remove_dependency_on_stock(self, a_deps, stocks):
        deps = copy.deepcopy(a_deps)
        for stock in stocks:
            for (k,v) in deps.items():
                if stock in v:
                    deps[k].remove(stock)
        return deps

    def add_timestep(self, deps_without_stocks, effects):
        missing_vars = graph.find_missing_variables(deps_without_stocks)
        if 'time_step' in missing_vars.values():
            self.add_timestep_into_dependency_graphs(deps_without_stocks, effects, missing_vars)
        return (deps_without_stocks, effects)

    def add_timestep_into_dependency_graphs(self, deps_without_stocks, effects, missing_vars):
        # required for graph.topological_sorting to work
        deps_without_stocks['time_step'] = [] # time_step becomes an independent variable
        # add effects of 'time_step' to effects so that for dep in effects[ind]: in graph.topological_sorting()
        # can find dependents on time_step
        self.add_timestep_to_effects(effects, missing_vars)

    def add_timestep_to_effects(self, effects, missing_vars):
        for (k,v) in missing_vars.items():
            if v in effects.keys():
                effects[v].append(k)
            else:
                effects[v] = [k]

def isfloat(var):
    return re.search(r'\b\d+(\.\d+)?\b',str(var))

class Variable(models.Model):
    model = models.ForeignKey(ModelDefinition)
    name = models.CharField(max_length=200)
    formula = models.CharField(max_length=2000)
    is_initial = models.BooleanField(default=False)
    is_decision = models.BooleanField(default=False)
    is_stock = models.BooleanField(default=False)
    init_value = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    description = models.TextField()

    @property
    def name_out(self): return self.name.capitalize().replace('_',' ')
    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        ordering = ('name',)

class InitialParams(object):
    """This represents selected parameters that will be initialized by game player at the beginning of the game"""

    def __unicode__(self):
        return u"InitialParams %s" % self.id

    def __init__(self, model):
        self.model = model

    @property
    def variables(self):
        # list[variable]
        if not hasattr(self, '_variables_cache'):
            self._variables_cache = [var for var in self.model.variable_set.all() if var.is_initial]
        return self._variables_cache

class DecisionParams(object):
    """This represents selected parameters that will be entered by game player at each game step"""

    def __unicode__(self):
        return u"DecisionParams %s" % self.id

    def __init__(self, model):
        self.model = model

    @property
    def variables(self):
        # list[variable]
        if not hasattr(self, '_variables_cache'):
            self._variables_cache = [var for var in self.model.variable_set.all() if var.is_decision]
        return self._variables_cache

class OutputGroup(models.Model):
    """This represents an output group that will be presented to the game player at each game step"""
    model = models.ForeignKey(ModelDefinition)
    name = models.CharField(max_length=250)
    is_advanced = models.BooleanField()
    variables = models.ManyToManyField(Variable)

    def __unicode__(self):
        return u"%s" % self.name

class GameManagementSettings(models.Model):
    """This represents general game management settings"""
    model = models.ForeignKey(ModelDefinition)
    notification_to_model_owner = models.BooleanField(blank=False)
    notification_email_address = models.EmailField(blank=False)
    entry_of_decision_variables_by_excel = models.BooleanField(blank=False)

    def __unicode__(self):
        return u"GameManagementSettings %s" % self.id

class TimeSettings(models.Model):
    """This represents time related settings of the game"""
    model = models.ForeignKey(ModelDefinition)
    time_between_decision_steps = models.FloatField()
    time_step = models.FloatField(default=0.5)
    total_game_time = models.IntegerField()
    record_period = models.IntegerField()

def slugify(string):
    string = re.sub('\s+', '_', string)
    string = re.sub('[^\w.-]', '', string)
    return string.strip('_.- ').lower()

class GameInstance(models.Model):
    game_definition = models.ForeignKey(GameDefinition)
    current_time = models.FloatField(default=0.0)
    current_stock_values = models.TextField()
    user = models.ForeignKey(User)

    def store_current_stock_values(self, stock_values_list):
        self.current_stock_values = stock_values_list.__str__()
        self.save()

    def init_values(self):
        if self.current_time == 0.0:    
            return self.model_instance.init_values()
        else:
            return eval(self.current_stock_values)

    def __unicode__(self):
        return u"GameInstance %s" % self.id

    @property
    def time_settings(self): return self.game_definition.model_definition.time_settings

    def advance_time(self):
        self.current_time = self.current_time + self.time_settings.time_between_decision_steps
        self.save()
        return self.current_time

    @property
    def model_instance(self):
        return self.modelinstance_set.all()[0]

class VariableRunData(models.Model):
    variable = models.ForeignKey(Variable)
    game_instance = models.ForeignKey(GameInstance)
    time = models.FloatField(blank=True)
    value = models.FloatField(blank=True)

    def __unicode__(self):
        return u"VariableRunData %s" % self.id

    class Meta:
        ordering = ('time',)

class OutputInstance(models.Model):
    output_group = models.ForeignKey(OutputGroup)
    game_instance = models.ForeignKey(GameInstance)
    path = models.CharField(max_length=200)

    def __unicode__(self):
        return u"OutputInstance %s" % self.id

    def make_path(self):
        return '/site_media/images/' + slugify(self.output_group.name) + '_' + str(self.game_instance.id) + '.png'

    def build_data_for(self, variable):
        '''
        queries database for VariableRunData.value wrt some Variable and GameInstance
        '''
        vrd_data = VariableRunData.objects.filter(variable=variable, game_instance=self.game_instance).order_by('time')
        return [vrd.value for vrd in vrd_data]

    def build_data(self):
        '''
        queries database for VariableRunData 
        collects all data for all Variables in the related OutputGroup
        '''
        variables = self.output_group.variables.all().order_by('name')
        data = [self.build_data_for(var) for var in variables]
        var_names = [var.name for var in variables]
        return data, self.build_time_for(variables[0]), var_names

    def build_time_for(self, variable):
        '''
        queries database for VariableRunData.time wrt some Variable and GameInstance
        '''
        vrd_data = VariableRunData.objects.filter(variable=variable, game_instance=self.game_instance).order_by('time')
        return [vrd.time for vrd in vrd_data]


class EqnsWriter(object):
    """"This is a strategy object. It knows how to write eqns (eqns_sorted). It takes data from the containing objects
    (ModelInstance or ModelDefinition)"""
    def __init__(self, model):
        self.model = model

    def update_value(self, var_name, new_value):
        self.dict_scipy[var_name] = new_value

    @property
    def eqns_sorted(self):
# todo: performans iyilestirmesi
#        if not hasattr(self, '_eqns_sorted_cache'):
#            self._eqns_sorted_cache = [var + ' = ' + self.dict_scipy[var] for var in self.levels]
#        return self._eqns_sorted_cache
        return [var + ' = ' + self.dict_scipy[var] for var in self.model.levels]

    @property
    def dict_scipy(self):
#       Ex: {'varname','formula'}
# eqns_sorted ile birlikte performans iyilestirme
        if not hasattr(self, '_dict_scipy_cache'):
            self._dict_scipy_cache = self.build_scipy_model()
        return self._dict_scipy_cache

    def build_scipy_model(self):
        eqns = {}
        eqns.update( deepcopy(self.model.variables) )
        return dict( [(k, self.replace_stockname_with_X(v)) for (k,v) in eqns.items()] )

    def replace_stockname_with_X(self, eqn):
        for b in self.model.stock_bunches:
            p = re.compile(b.pattern)
            eqn,n = p.subn(b.replace, eqn)
        return eqn

class ModelInstance(models.Model):
    game_instance = models.ForeignKey(GameInstance)
    model_definition = models.ForeignKey(ModelDefinition)

    def __unicode__(self):
        return u"ModelInstance %s" % self.id
        
    @property
    def stock_set(self): return self.model_definition.stock_set
    @property
    def eqns_writer(self):
        if not hasattr(self, '_eqns_writer_cache'):
            self._eqns_writer_cache = EqnsWriter(self)
        return self._eqns_writer_cache

    def set_decision_values(self, variable_values):
        # variable_values = dict[var_name, new_value]. puts this value into the dict_scipy
        for (var_name, new_value) in variable_values.items():
            self.eqns_writer.update_value(var_name, new_value)

    def store_variable_run_data_for_stocks(self, X, time):
        for i, bunch in enumerate(self.model_definition.stock_bunches):
            stock = self.model_definition.stock_map[bunch.name]
            vrd = VariableRunData()
            vrd.variable = stock
            vrd.game_instance = self.game_instance
            vrd.value = X[-1,i] # last value
            vrd.time = time[-1]
            vrd.save()

    def init_values(self):
        is_exist_vrd = VariableRunData.objects.filter(game_instance=self.game_instance).count()
        if not is_exist_vrd:
            result = []
            for b in self.model_definition.stock_bunches:
                if isfloat(b.init):
                    result.append(float(b.init))
                else:
                    #todo: burada dolayli referanslar olabilir. tum bagimlilik cizgesini cek
                    result.append(self.eval_formula(b.init))
            return result
        else:
            vrd_map = {}
            for stock in self.model_definition.stock_set:
                vrd_map[stock.name] = VariableRunData.objects.filter(game_instance=self.game_instance,variable=stock)[0]
            result = []
            for b in self.model_definition.stock_bunches:
                result.append(vrd_map[b.name].value)
            return result

    def eval_formula(self, formula):
# c = c_init
# c_init = c_b
# c_b = 400
# in this case, this function returns 400 for the input 'c_init'
        causes = self.find_vars(formula)
        for var in causes:
            formula_of_cause = self.eqns_writer.dict_scipy[var]
            exec(var+'='+str(self.eval_formula(formula_of_cause)))
        exec('result='+formula)
        return result

    def find_vars(self, formula):
        # match variables, exclude function calls and 't'
        # eg: 'max(x) + t' match: 'x' exclude 'max' 't'
        # eg: 'scipy.interpolate.UnivariateSpline(pts_x_0)' match: 'pts_x_0' exclude 'scipy.interpolate.UnivariateSpline'
# todo: keywordleri disaridan al
        variable_name_pattern = re.compile(r'((?!\bin\b|\bfor\b|\bif\b|\belse\b|\barray\b|\b__x\b|\b__y\b)(?!\b(?=\D)\w+(\.\w+)*\s*(?=\())(?!\bt\b)\b(?=\D)\w+)')
        return [item[0] for item in variable_name_pattern.findall(formula)]

    @property
    def eqns_sorted(self): return self.eqns_writer.eqns_sorted
    @property
    def differentials(self): return self.model_definition.differentials
    @property
    def stock_bunches(self): return self.model_definition.stock_bunches
    @property
    def variables(self):
        # dict[var_name,formula]
        if not hasattr(self, '_variables_cache'):
            self._variables_cache = dict([(var.name, var.formula) for var in self.variableinstance_set.all()])
            self._variables_cache['time_step'] = str(0.5)
        return self._variables_cache

    @property
    def levels(self): return self.model_definition.levels
    @property
    def stock_names(self): return self.model_definition.stock_names
    @property
    def stocks(self): return self.model_definition.stocks
    @property
    def time_step(self): return self.model_definition.time_step
    @property
    def decision_period(self): return self.model_definition.decision_period
    @property
    def record_period(self): return self.model_definition.record_period
    @property
    def output_groups(self): return self.model_definition.output_groups
    @property
    def stock_names(self): return self.model_definition.stock_names
    @property
    def stock_map(self): return self.model_definition.stock_map

class VariableInstance(models.Model):
    variable = models.ForeignKey(Variable)
    model_instance = models.ForeignKey(ModelInstance)
    formula = models.CharField(max_length=2000)
    @property
    def name(self): return self.variable.name
    @property
    def is_initial(self): return self.variable.is_initial
    @property
    def is_decision(self): return self.variable.is_decision
    @property
    def is_stock(self): return self.variable.is_stock
    @property
    def init_value(self): return self.variable.init_value

    def __unicode__(self):
        return u"%s" % self.name

class InitialVariableInstance(models.Model):
    variable = models.ForeignKey(Variable)
    model_instance = models.ForeignKey(ModelInstance)
    value = models.FloatField(blank=True,default=0.0)
    @property
    def name(self): return self.variable.name

class SiteProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    nick = models.CharField(max_length=30)