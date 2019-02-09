from django import forms
from palamut.models import *
from django.forms import widgets
from sim.bunch import Bunch
from django.utils.html import escape, conditional_escape
from django.utils.encoding import StrAndUnicode, force_unicode

class ModelVariableInput(widgets.Input):
    input_type = 'text'

    def render(self, name, value, attrs=None):
        import ipdb; ipdb.set_trace()
        if value is None:
            value = ''
        if isinstance(value, Variable):
            variable = value
            description = ' [%s]' % variable.unit
            return super(ModelVariableInput, self).render(name, variable.formula, attrs) + \
                conditional_escape(description)

class ModelVariableField(forms.CharField):
    widget = ModelVariableInput

    def __init__(self, model_definition=None, *args, **kwargs):
        self.model_definition = model_definition
        super(ModelVariableField, self).__init__(*args, **kwargs)

    def clean(self, value):
        super(ModelVariableField, self).clean(value)
        if not value:
            return ''
        if isinstance(value, Bunch):
            return value

        variable = Variable.objects.get(model=self.model_definition,name=self.label)
        variable.formula = value
        return variable

class UploadFileForm(forms.Form):
    file = forms.FileField()

class VerifyModelForm(forms.ModelForm):
    class Meta:
        model = ModelPython
        exclude = ('game_definition')

class GameDefinitionForm(forms.ModelForm):
    class Meta:
        model = GameDefinition
        exclude = ('slug', 'original_text')

class DefineInitialParamsForm(forms.Form):
    initial_params = forms.MultipleChoiceField(widget=widgets.CheckboxSelectMultiple)

    def __init__(self, model_definition, *args, **kwargs):
        super(DefineInitialParamsForm, self).__init__(*args, **kwargs)
        import operator
        varmap_tuples = sorted(model_definition.constant_vars_idmap.items(), key=operator.itemgetter(1))
        choices=[(var_id, var_name) for (var_id, var_name) in varmap_tuples]
        self.fields['initial_params'].choices = choices

class DefineTimeSettings(forms.ModelForm):
    class Meta:
        model = TimeSettings
        exclude = ('model')

class DefineDecisionParams(forms.Form):
    decision_params = forms.MultipleChoiceField(widget=widgets.CheckboxSelectMultiple)

    def __init__(self, model_definition, *args, **kwargs):
        super(DefineDecisionParams, self).__init__(*args, **kwargs)
        import operator
        varmap_tuples = sorted(model_definition.constant_vars_idmap.items(), key=operator.itemgetter(1))
        choices = [(var_id, var_name) for (var_id, var_name) in varmap_tuples]
        self.fields['decision_params'].choices = choices

class DefineNewOutputGroupForm(forms.ModelForm):
    def __init__(self, model_definition, *args, **kwargs):
        super(DefineNewOutputGroupForm, self).__init__(*args, **kwargs)
        self.fields['variables'].queryset = Variable.objects.filter(model=model_definition)
        self.fields['variables'].widget.attrs = {'size':'40'}
        
    class Meta:
        model = OutputGroup
        exclude = ('model')

class DefineGameManagementSettingsForm(forms.ModelForm):
    class Meta:
        model = GameManagementSettings
        exclude = ('model')

def get_define_initial_params_form(initial_variables):
    fields = {}
    for var in initial_variables:
        fields[var.name] = forms.FloatField()
    return type('InputInitialValuesForm', (forms.BaseForm,), {'base_fields': fields})

def get_game_basic_form_new(model_definition, game_instance):
    decision_variables = Variable.objects.filter(model=model_definition,is_decision=True)
    fields = {}
    for var in decision_variables:
        fields[var.name] = ModelVariableField(model_definition=model_definition)
# GraphicsField gibi bir alan ekleyecek miyim?   
    return type('GameBasicForm', (forms.BaseForm,), {'base_fields': fields})

def get_game_basic_form_old(model_definition, game_instance):
    decision_variables = Variable.objects.filter(model=model_definition,is_decision=True)
    fields = {}
    for var in decision_variables:
        fields[var.name] = forms.FloatField()
# GraphicsField gibi bir alan ekleyecek miyim?
    return type('GameBasicForm', (forms.BaseForm,), {'base_fields': fields})

def get_game_basic_form_v3(decision_variables):
    fields = {}
    for var in decision_variables:
        fields[var.name] = forms.FloatField()
# GraphicsField gibi bir alan ekleyecek miyim?
    return type('GameBasicForm', (forms.BaseForm,), {'base_fields': fields})

