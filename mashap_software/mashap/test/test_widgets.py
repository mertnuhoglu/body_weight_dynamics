"""
Based on http://www.djangosnippets.org/snippets/595/
by sopelkin
"""

from django.forms import *
from palamut.models import Variable
from sim.bunch import Bunch
from django.utils.html import escape, conditional_escape
from django.utils.encoding import StrAndUnicode, force_unicode
from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

_variables = {
    'body_weight':Bunch(name='body_weight',unit='g',formula='0')
}

class CommaSeparatedUserInput(widgets.Input):
    input_type = 'text'

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        elif isinstance(value, (list, tuple)):
            value = (', '.join([user.username for user in value]))
        return super(CommaSeparatedUserInput, self).render(name, value, attrs)



class CommaSeparatedUserField(forms.Field):
    widget = CommaSeparatedUserInput

    def clean(self, value):
        super(CommaSeparatedUserField, self).clean(value)
        if not value:
            return ''
        if isinstance(value, (list, tuple)):
            return value

        names = set(value.split(','))
        names_set = set([name.strip() for name in names])
        users = list(User.objects.filter(username__in=names_set))
        unknown_names = names_set ^ set([user.username for user in users])
        if unknown_names:
            raise forms.ValidationError(_(u"The following usernames are incorrect: %(users)s") % {'users': ', '.join(unknown_names)})

        return users


class DescriptionAfterInput(widgets.Input):
    input_type = 'text'

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        return super(DescriptionAfterInput, self).render(name, value, attrs) + \
            conditional_escape(force_unicode('after <>soguk'))

class DescriptionAfterField(forms.Field):
    widget = DescriptionAfterInput

    def clean(self, value):
        super(DescriptionAfterField, self).clean(value)
        if not value:
            return ''
        if isinstance(value, (list, tuple)):
            return value

        names = set(value.split(','))
        names_set = set([name.strip() for name in names])
        users = list(User.objects.filter(username__in=names_set))
        unknown_names = names_set ^ set([user.username for user in users])
        if unknown_names:
            raise forms.ValidationError(_(u"The following usernames are incorrect: %(users)s") % {'users': ', '.join(unknown_names)})

        return users

class DescribedVariableInput(widgets.Input):
    input_type = 'text'

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        if isinstance(value, Bunch):
            variable = value
        description = ' [%s]' % variable.unit
        return super(DescribedVariableInput, self).render(name, variable.formula, attrs) + \
            conditional_escape(force_unicode(description))

class DescribedVariableField(forms.Field):
    widget = DescribedVariableInput

    def clean(self, value):
        super(DescribedVariableField, self).clean(value)
        if not value:
            return ''
        if isinstance(value, Bunch):
            return value

        variable = _variables[self.label]
        variable.formula = value
        return variable

class ModelVariableInput(widgets.Input):
    input_type = 'text'

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        if isinstance(value, Variable):
            variable = value
            description = ' [%s]' % variable.unit
            return super(ModelVariableInput, self).render(name, variable.formula, attrs) + \
                conditional_escape(force_unicode(description))

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

