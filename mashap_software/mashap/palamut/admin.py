from palamut.models import *
from django.contrib import admin
admin.autodiscover()

class GameInstanceInline(admin.TabularInline):
    model = GameInstance
    
admin.site.register(GameDefinition)
admin.site.register(ModelPython)
admin.site.register(ModelDefinition)
admin.site.register(Variable)
admin.site.register(OutputGroup)
admin.site.register(GameManagementSettings)
admin.site.register(TimeSettings)
admin.site.register(GameInstance)
admin.site.register(VariableRunData)
admin.site.register(OutputInstance)
admin.site.register(ModelInstance)
admin.site.register(VariableInstance)
admin.site.register(InitialVariableInstance)