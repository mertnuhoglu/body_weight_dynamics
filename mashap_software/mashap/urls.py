from django.conf.urls.defaults import *
from palamut.models import OutputGroup
from django.views.generic.simple import redirect_to
from django.contrib import admin

#info_dict = {
#    'queryset': OutputGroup.objects.all(),
#}
#urlpatterns = patterns('',
#   url(r'^mashap/define_outputs/$','django.views.generic.list_detail.object_list', dict(info_dict), name='define_outputs'),
#)
admin.autodiscover()


urlpatterns = patterns('mashap.palamut.views',
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/profile/$',redirect_to, {'url': '/profiles/'}),
    (r'^accounts/', include('registration.urls')),
    (r'^profiles/', include('profiles.urls')),
    url(r'^mashap/$','model_upload',name='mashap.index'),
    url(r'^mashap/$','model_upload',name='index'),
    url(r'^mashap/$','model_upload',name='model_upload'),
    url(r'^mashap/verify_model/$','verify_model',name='verify_model'),
    url(r'^mashap/define_initial_params/$','define_initial_params',name='define_initial_params'),
    url(r'^mashap/define_time_settings/$','define_time_settings',name='define_time_settings'),
    url(r'^mashap/define_decision_params/$','define_decision_params',name='define_decision_params'),
    url(r'^mashap/define_outputs/$','define_outputs', name='define_outputs'),
    url(r'^mashap/define_new_output_group/$','define_new_output_group',name='define_new_output_group'),
    url(r'^mashap/define_game_management_settings/$','define_game_management_settings',name='define_game_management_settings'),
    url(r'^mashap/access_data/$','access_data',name='access_data'),
    url(r'^mashap/introduce_game/(?P<slug>[^\.^/]+)/$','introduce_game',name='introduce_game'),
    url(r'^mashap/input_initial_values/$','input_initial_values',name='input_initial_values'),
    url(r'^mashap/game_basic/$','game_basic',name='game_basic'),
    url(r'^mashap/game_detailed/$','game_detailed',name='game_detailed'),
    url(r'^mashap/game_results/$','game_results',name='game_results'),

    url(r'^mashap/palamut/show_results/$','show_results',name='show_results'),
    url(r'^mashap/palamut/result_data/$','result_data',name='result_data'),
    url(r'^mashap/palamut/equations/$','equations',name='equations'),

    url(r'^mashap/test/$','test',name='test'),
)

urlpatterns += patterns('',
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:/projects/cinar-agaci-01/ari-kovani-01/python-01/tez-01/mashap/palamut/site_media'}),
)
