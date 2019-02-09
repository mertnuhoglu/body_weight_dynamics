from sim.converter import Converter
from sim import graphics
from sim import modelreader
from sim.simulator import Simulator
from palamut.models import *
from numpy import array

class SimManager(object):
    def build_game_instance(self, game_definition, user):
        model_definition = game_definition.model_definition
        game_instance = self.store_game_instance(game_definition, user)
        model_instance = self.store_model_instance(game_instance, model_definition)
        self.store_output_instances(game_instance, model_definition)
        self.store_variable_instances(model_instance)
        return game_instance

    def store_model_instance(self, game_instance, model_definition):
        model_instance = ModelInstance()
        model_instance.game_instance = game_instance
        model_instance.model_definition = model_definition
        model_instance.save()
        return model_instance

    def store_game_instance(self, game_definition, user):
        game_instance = GameInstance()
        game_instance.game_definition = game_definition
        game_instance.user = user
        game_instance.save()
        return game_instance

    def store_variable_instances(self, model_instance):
        initial_variables = Variable.objects.filter(model=model_instance.model_definition,is_stock=False)
        for var in initial_variables:
            self.store_variable_instance(model_instance, var)

    def store_variable_instance(self, model_instance, var):
        var_value = VariableInstance()
        var_value.variable = var
        var_value.model_instance = model_instance
        var_value.formula = var.formula
        var_value.save()

    def store_output_instances(self, game_instance, model_definition):
        output_groups = model_definition.outputgroup_set.all()
        stored_variables = {}
        for output_group in output_groups:
            output_instance = OutputInstance()
            output_instance.output_group = output_group
            output_instance.game_instance = game_instance
            output_instance.save()
            variables = output_group.variables.all()

    def set_variables(self, model_definition, variable_values):
        """
        variable_values = dict[var_name, new_value]. puts these values into the variable objects
        changes are persistent in Variable objects
        """
        for (var_name, new_value) in variable_values.items():
            variable = model_definition.variable_set.get(name=var_name)
            variable.formula = new_value
            variable.save()

    def set_decision_values(self, model_instance, variable_values):
        """
        # variable_values = dict[var_name, new_value]. puts these values into the dict_scipy
        changes are transient (only for decision period in simulate method)
        returns True when time is up
        """
        model_instance.set_decision_values(variable_values)
        Simulator(model_instance).simulate()
        gi = model_instance.game_instance
        output_instances = OutputInstance.objects.filter(game_instance = gi)
        self.draw_graph(output_instances)
        if gi.advance_time() >= gi.time_settings.total_game_time:
            return True

    def get_graphic_paths(self, model_definition, game_instance):
        output_groups_basic = OutputGroup.objects.filter(model=model_definition)
        graphic_paths = []
        for group in output_groups_basic:
            oi = OutputInstance.objects.get(output_group=group,game_instance=game_instance)
            graphic_paths.append(oi.path)
        return graphic_paths

    def draw_graph(self, output_instances, path='./run.png'):
        for oi in output_instances:
            X, time, var_names = oi.build_data()
            oi.path = oi.make_path()
            oi.save()
            path = 'C:/projects/cinar-agaci-01/ari-kovani-01/python-01/tez-01/mashap/palamut/' + oi.path
            graphics.draw_graph(array(X), array(time), var_names, oi.output_group.name, path)

    def build_model_python(self, game_definition):
        model_python, mappings_in = game_definition.build_model_python()
        model_python.save()
        self.build_model(model_python, mappings_in)
        return model_python

    def convert_vensim_file(self, file_content):
        game_definition = GameDefinition(original_text = file_content)
        game_definition.save()
        return self.build_model_python(game_definition)

    def build_model(self, model_python, mappings_in):
        return modelreader.build_model_from_model_python(model_python, mappings_in)

    def simulate(self, model, model_instance):
        simulator = Simulator(model_instance)
        X = simulator.simulate()
        stock_bunches = model_instance.stock_bunches
        self.write_files(X[1], model, simulator, model_instance)

    def write_files(self, results, model, simulator, model_instance):
        run_data = open('C:/java/python/Python25/Lib/site-packages/django/contrib/admin/media/run_data.txt', 'wb')
        run_data.write(str(results.tolist()))
        run_data.close( )

        equations = open('C:/java/python/Python25/Lib/site-packages/django/contrib/admin/media/equations_scipy.txt', 'wb')
        eqns_scipy = [var + ' = ' + model.dict_scipy[var] for var in model.levels]
        equations.write("\n".join(eqns_scipy))
        equations.close( )

        equations = open('C:/java/python/Python25/Lib/site-packages/django/contrib/admin/media/equations_readable.txt', 'wb')
        equations.write("\n".join(model_instance.eqns_sorted))
        equations.close( )

        converter = Converter(model)
        equations_matlab = open('C:/java/python/Python25/Lib/site-packages/django/contrib/admin/media/equations_matlab.txt', 'wb')
        equations_matlab.write("\n".join(converter.matlab_eqns))
        equations_matlab.close( )

        self.draw_graph('C:/java/python/Python25/Lib/site-packages/django/contrib/admin/media/body_weight.png')

    def set_initial_params(self, initial_params, non_initial_params):
        for var in initial_params:
            var.is_initial = True
            var.save()
        for var in non_initial_params:
            var.is_initial = False
            var.save()

    def set_decision_params(self, decision_params, non_decision_params):
        for var in decision_params:
            var.is_decision = True
            var.save()
        for var in non_decision_params:
            var.is_decision = False
            var.save()

def path(file_name):
    return 'C:/java/python/Python25/Lib/site-packages/django/contrib/admin/media/' + file_name