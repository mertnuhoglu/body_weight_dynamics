from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.views.generic.list_detail import object_list

from sim.simulator import Simulator
from sim.bunch import Bunch
from sim.modelparser_mapsys import ModelParser
from sim import graphics
from sim.modelreader import ModelReader

from palamut.models import *
from palamut.service import *
from palamut.pforms import *
import django.views.generic.list_detail
from django.contrib.auth.decorators import login_required

@login_required
def model_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            file_content = ''.join([chunk for chunk in f.chunks()])
            model_python = SimManager().convert_vensim_file(file_content)
            request.session['model_python.id'] = model_python.id
            request.session['game_definition.id'] = model_python.game_definition.id
            model = model_python.model_definition
            request.session['model.id'] = model.id
            return HttpResponseRedirect(reverse('verify_model'))
    if request.method == 'GET':
        form = UploadFileForm()
        return render_to_response('model_upload.html', {'form': form})

@login_required
def verify_model(request):
    if request.method == 'POST':
        form = GameDefinitionForm(request.POST, instance=gd(request))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('define_initial_params'))
    if request.method == 'GET':
        model_python = ModelPython.objects.get(pk=request.session['model_python.id'])
        form_model_python = VerifyModelForm(instance=model_python)
        form_game_definition = GameDefinitionForm(instance=md(request))
        return render_to_response('verify_model.html', {'form_model_python': form_model_python, 'form_game_definition': form_game_definition})

@login_required
def define_initial_params(request):
    if request.method == 'POST':
        form = DefineInitialParamsForm(md(request), request.POST)
        if form.is_valid():
            initial_params_ids = form.cleaned_data['initial_params']
            initial_params = Variable.objects.filter(pk__in=initial_params_ids)
            non_initial_params = Variable.objects.exclude(pk__in=initial_params_ids).filter(model=md(request))
            SimManager().set_initial_params(initial_params, non_initial_params)
            return HttpResponseRedirect(reverse('define_time_settings'))
    else:
        form = DefineInitialParamsForm(md(request))
    return render_to_response('define_initial_params.html', {'form': form})

@login_required
def define_time_settings(request):
    if request.method == 'POST':
        try:
# don't allow more than one instance per model_definition
            time_settings = TimeSettings.objects.get(model=md(request))
        except TimeSettings.DoesNotExist, err:
            time_settings = TimeSettings(model=md(request))
        form = DefineTimeSettings(request.POST, instance=time_settings)
        if form.is_valid():
            time_settings = form.save()
            SimManager().set_variables(md(request),{'time_step': str(time_settings.time_step)})
            return HttpResponseRedirect(reverse('define_decision_params'))
    if request.method == 'GET':
        form = DefineTimeSettings()
        return render_to_response('define_time_settings.html', {'form': form})

@login_required
def define_decision_params(request):
    if request.method == 'POST':
        form = DefineDecisionParams(md(request), request.POST)
        if form.is_valid():
            decision_params_id = form.cleaned_data['decision_params']
            decision_params = Variable.objects.filter(pk__in=decision_params_id)
            non_decision_params = Variable.objects.exclude(pk__in=decision_params_id).filter(model=md(request))
            SimManager().set_decision_params(decision_params, non_decision_params)
            return HttpResponseRedirect(reverse('define_outputs'))
    if request.method == 'GET':
        form = DefineDecisionParams(md(request))
        return render_to_response('define_decision_params.html', {'form': form})

@login_required
def define_outputs(request):
    return object_list(request, queryset = OutputGroup.objects.filter(model=md(request)))

@login_required
def define_new_output_group(request):
    if request.method == 'POST':
        form = DefineNewOutputGroupForm(md(request), request.POST)
        if form.is_valid():
            output_group = form.save(commit=False)
            output_group.model = md(request)
            output_group.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('define_outputs'))
    if request.method == 'GET':
        form = DefineNewOutputGroupForm(md(request))
        return render_to_response('define_new_output_group.html', {'form': form})

@login_required
def define_game_management_settings(request):
    if request.method == 'POST':
        g = GameManagementSettings(model=md(request))
        form = DefineGameManagementSettingsForm(request.POST, instance=g)
        if form.is_valid():
            g = form.save()
            return HttpResponseRedirect(reverse('access_data'))
    if request.method == 'GET':
        form = DefineGameManagementSettingsForm()
        return render_to_response('define_game_management_settings.html', {'form': form})

@login_required
def access_data(request):
    if request.method == 'GET':
        game_url = gd(request).get_absolute_url()
        return render_to_response('access_data.html', {'game_url': game_url})

@login_required
def introduce_game(request, slug):
    if request.method == 'GET':
        game_definition = GameDefinition.objects.get(slug = slug)
        model_python = game_definition.modelpython_set.all()[0]
        request.session['game_definition.id'] = game_definition.id
        request.session['model_python.id'] = model_python.id
        model = model_python.model_definition
        request.session['model.id'] = model.id
        return render_to_response('introduce_game.html', {'game_definition': game_definition})

@login_required
def input_initial_values(request):
    if request.method == 'POST':
        initial_variables = Variable.objects.filter(model=md(request),is_initial=True)
        form_class = get_define_initial_params_form(initial_variables)
        form = form_class(request.POST)
        if form.is_valid():
            game_instance = SimManager().build_game_instance(gd(request), request.user)
            request.session['game_instance.id'] = game_instance.id
            request.session['model_instance.id'] = game_instance.model_instance.id
            initial_variables = Variable.objects.filter(model=md(request),is_initial=True)
            initial_variable_instances = []
            for var in initial_variables:
                var_instance = VariableInstance.objects.get(variable=var,model_instance=mi(request))
                var_instance.formula = form.cleaned_data[var.name]
                var_instance.save()
            return HttpResponseRedirect(reverse('game_basic'))
    if request.method == 'GET':
        initial_variables = Variable.objects.filter(model=md(request),is_initial=True)
        form_class = get_define_initial_params_form(initial_variables)
        form = form_class()
        return render_to_response('input_initial_values.html', {'form': form, 'initial_variables': initial_variables})

@login_required
def game_basic(request):
    if request.method == 'POST':
        decision_variables = Variable.objects.filter(model=md(request),is_decision=True)
        form_class = get_game_basic_form_v3(decision_variables)
        form = form_class(request.POST)
        if form.is_valid():
            decision_values = {}
            for var in decision_variables:
                decision_values[var.name] = str(form.cleaned_data[var.name])
            is_end = SimManager().set_decision_values(mi(request), decision_values)
            if is_end:
                return HttpResponseRedirect(reverse('game_results'))
            return HttpResponseRedirect(reverse('game_basic'))
    if request.method == 'GET':
        decision_variables = Variable.objects.filter(model=md(request),is_decision=True)
        form_class = get_game_basic_form_v3(decision_variables)
        form = form_class()
        graphic_paths = SimManager().get_graphic_paths(md(request), gi(request))
        return render_to_response('game_basic.html', {'form': form, 'graphic_paths': graphic_paths,
                                                      'decision_variables':decision_variables})

@login_required
def game_detailed(request):
    if request.method == 'POST':
        form = DefineGameManagementSettingsForm(request.POST)
        if form.is_valid():
            g = form.save()
            return HttpResponseRedirect(reverse('game_results'))
    if request.method == 'GET':
        form = DefineGameManagementSettingsForm()
        return render_to_response('game_detailed.html', {'form': form})

@login_required
def game_results(request):
    if request.method == 'GET':
        graphic_paths = SimManager().get_graphic_paths(md(request), gi(request))
        return render_to_response('game_results.html', {'graphic_paths': graphic_paths})

@login_required
def show_results(request):
    return render_to_response('show_results.html')

@login_required
def result_data(request):
    return HttpResponse('hi')

@login_required
def equations(request):
    return HttpResponse('hi')

def test(request):
    return render_to_response('test.html')

def gi(request):
    return GameInstance.objects.get(pk = request.session['game_instance.id'])
def gd(request):
    return GameDefinition.objects.get(pk = request.session['game_definition.id'])
def md(request):
    return ModelDefinition.objects.get(pk = request.session['model.id'])
def mi(request):
    return ModelInstance.objects.get(pk = request.session['model_instance.id'])
