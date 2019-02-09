from django.test import *
from palamut.models import *
from palamut.service import *
from palamut.pforms import *

class ServiceTest(TestCase):
    fixtures = ['model_long_07_06_01']

    def setUp(self):
        self.game_definition = GameDefinition.objects.get(pk=1)
        self.model_python = ModelPython.mobjects.get(pk=1)
        self.model_definition = ModelDefinition.objects.get(pk=1)
        self.model_instance = ModelInstance.objects.get(pk=1)
        self.time_settings = TimeSettings.objects.get(pk=1)
        self.output_groups = OutputGroup.objects.all()
        self.variables = Variable.objects.all()
        self.baseline_bodyweight = Variable.objects.get(name='baseline_bodyweight')
        self.ci_0 = Variable.objects.get(name='ci_0')
        self.fi_0 = Variable.objects.get(name='fi_0')
        self.pi_0 = Variable.objects.get(name='pi_0')
        self.fi_input = Variable.objects.get(name='fi_input')
        self.pi_input = Variable.objects.get(name='pi_input')
        self.ci_input = Variable.objects.get(name='ci_input')
        self.activ_time_param = Variable.objects.get(name='activ_time_param')
        self.initial_variables = [self.baseline_bodyweight, self.ci_0, self.fi_0, self.pi_0]
        self.decision_variables = [self.ci_input, self.fi_input, self.pi_input, self.activ_time_param]
        
    def test_convert_vensim(self):
        game_definition = GameDefinition.objects.get(pk=1)
        file_content = game_definition.original_text
        model_python = SimManager().convert_vensim_file(file_content)
        expected_mp = ModelPython.objects.get(pk=1)
        self.assertEqual(model_python.eqns,expected_mp.eqns)

    def test_set_initial_params(self):
        initial_params = Variable.objects.filter(model=self.model_definition,is_initial=True)
        initial_params_ids = [var.id for var in initial_params]
        non_initial_params = Variable.objects.exclude(pk__in=initial_params_ids).filter(model=self.model_definition)
        SimManager().set_initial_params(initial_params, non_initial_params)

    def test_set_decision_values(self):
        decision_variables = Variable.objects.filter(model=self.model_definition,is_decision=True)
        decision_values = {'activ_time_param' : 0,
                           'ci_input':1500,
                           'pi_input':500,
                           'fi_input':1000
        }
        is_end = SimManager().set_decision_values(self.model_instance, decision_values)

        