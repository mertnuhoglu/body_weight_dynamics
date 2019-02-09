from django.test import TestCase
from django.test import Client
from django import template
from django.db.models import get_model
c = Client()
class Testmaker(TestCase):
	#fixtures = ["palamut"]

	def test_mashap_126018164731(self): 
		r = c.get('/mashap/', {})
		self.assertEqual(r.status_code, 302)

	def test_accountslogin_126018166041(self): 
		r = c.get('/accounts/login/', {'next': '/mashap/'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["site_name"]), u"example.com")
		self.assertEqual(unicode(r.context[-1]["site"]), u"example.com")
		self.assertEqual(unicode(r.context[-1]["form"]), u"<tr><th><label for="id_username">Username:</label></th><td><input id="id_username" type="text" name="username" maxlength="30" /></td></tr>
<tr><th><label for="id_password">Password:</label></th><td><input type="password" name="password" id="id_password" /></td></tr>")
		self.assertEqual(unicode(r.context[-1]["next"]), u"/mashap/")
		tmpl = template.Template(u"""{% load i18n %}{% trans 'Log in' %}""")
		context = template.Context({})
		self.assertEqual(tmpl.render(context), u"Log in")
		tmpl = template.Template(u"""{% load i18n %}{% trans "Forgot password" %}""")
		context = template.Context({})
		self.assertEqual(tmpl.render(context), u"Forgot password")
		tmpl = template.Template(u"""{% load i18n %}{% trans "Not member" %}""")
		context = template.Context({})
		self.assertEqual(tmpl.render(context), u"Not member")

	def test_stylecss_126018166186(self): 
		r = c.get('/style.css', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_126018166211(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_accountslogin_12601893978(self): 
		r = c.get('/accounts/login/', {'next': '/mashap/'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["site_name"]), u"example.com")
		self.assertEqual(unicode(r.context[-1]["site"]), u"example.com")
		self.assertEqual(unicode(r.context[-1]["form"]), u"<tr><th><label for="id_username">Username:</label></th><td><input id="id_username" type="text" name="username" maxlength="30" /></td></tr>
<tr><th><label for="id_password">Password:</label></th><td><input type="password" name="password" id="id_password" /></td></tr>")
		self.assertEqual(unicode(r.context[-1]["next"]), u"/mashap/")
		tmpl = template.Template(u"""{% load i18n %}{% trans 'Log in' %}""")
		context = template.Context({})
		self.assertEqual(tmpl.render(context), u"Log in")
		tmpl = template.Template(u"""{% load i18n %}{% trans "Forgot password" %}""")
		context = template.Context({})
		self.assertEqual(tmpl.render(context), u"Forgot password")
		tmpl = template.Template(u"""{% load i18n %}{% trans "Not member" %}""")
		context = template.Context({})
		self.assertEqual(tmpl.render(context), u"Not member")

	def test_stylecss_126018940258(self): 
		r = c.get('/style.css', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_126018940277(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_accountslogin_126018940894(self): 
		r = c.post('/accounts/login/', {'username': 'admin''password': 'admin''next': '/mashap/'})

	def test_mashap_126018941013(self): 
		r = c.get('/mashap/', {})
		self.assertEqual(r.status_code, 302)

	def test_mashap_126018948784(self): 
		r = c.get('/mashap/', {})
		self.assertEqual(r.status_code, 302)

	def test_faviconico_126018949097(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126018949303(self): 
		r = c.get('/mashap/', {})
		self.assertEqual(r.status_code, 302)

	def test_mashap_126018968611(self): 
		r = c.get('/mashap/', {})
		self.assertEqual(r.status_code, 302)

	def test_mashap_126019059548(self): 
		r = c.get('/mashap/', {})
		self.assertEqual(r.status_code, 302)

	def test_faviconico_126019061289(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126019072967(self): 
		r = c.get('/mashap/', {})
		self.assertEqual(r.status_code, 302)

	def test_faviconico_126019093889(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126019095834(self): 
		r = c.get('/mashap/', {})
		self.assertEqual(r.status_code, 302)

	def test_faviconico_126019097892(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126019101069(self): 
		r = c.get('/mashap/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"22140.999794")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashap_126019118678(self): 
		r = c.get('/mashap/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"2968.99986267")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126019119058(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126019119533(self): 
		r = c.post('/mashap/', {'upload_button': 'Upload'})

	def test_mashapverify_model_126019131614(self): 
		r = c.get('/mashap/verify_model/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapverify_model_126019141802(self): 
		r = c.post('/mashap/verify_model/', {'game_description': 'test01 described''name': 'test01''submit': 'Submit''purpose': 'do it'})

	def test_mashapdefine_initial_params_126019142073(self): 
		r = c.get('/mashap/define_initial_params/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapdefine_initial_params_126019150528(self): 
		r = c.post('/mashap/define_initial_params/', {'initial_params': '238''submit': 'Submit'})

	def test_mashapdefine_time_settings_126019156578(self): 
		r = c.get('/mashap/define_time_settings/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"16.0000324249")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashap_126019532714(self): 
		r = c.get('/mashap/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"12328.0000687")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126019534177(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126019537466(self): 
		r = c.get('/mashap/', {'profile': ''})

	def test_mashap_12601964830(self): 
		r = c.get('/mashap/', {'profile': ''})

	def test_mashap_126019823678(self): 
		r = c.get('/mashap/', {'profile': ''})

	def test_mashap_126019867305(self): 
		r = c.get('/mashap/', {'profile': ''})

	def test_mashap_126019911248(self): 
		r = c.get('/mashap/', {'profile': ''})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"10967.9999352")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126019912678(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126019933444(self): 
		r = c.get('/mashap/', {'profile': ''})

	def test_faviconico_126019978088(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126019978375(self): 
		r = c.get('/mashap/', {'profile': ''})

	def test_mashap_126020017788(self): 
		r = c.get('/mashap/', {'profile': ''})

	def test_mashap_126020024567(self): 
		r = c.get('/mashap/', {'profile': ''})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"6342.99993515")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_12602002553(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126020153478(self): 
		r = c.get('/mashap/', {'profile': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"3921.99993134")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126020153959(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126020207184(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"3717.99993515")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126020210033(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126026193567(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"12235.0001335")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126026194988(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_12602629930(self): 
		r = c.get('/mashap/', {'profile': ''})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"2655.99989891")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashap_126026430175(self): 
		r = c.get('/mashap/', {'profile': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"2875.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"0")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126026430559(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126026841453(self): 
		r = c.get('/mashap/', {'profile': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"20500.0")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126026843597(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126027277578(self): 
		r = c.get('/mashap/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"14812.0000362")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashap_126027279144(self): 
		r = c.get('/mashap/', {'profile': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"30.9998989105")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashap_12602727917(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"16.0000324249")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashap_126027478816(self): 
		r = c.get('/mashap/', {'prof': ''})

	def test_mashap_12602748282(self): 
		r = c.get('/mashap/', {'prof': ''})

	def test_mashap_126027484048(self): 
		r = c.get('/mashap/', {'prof': ''})

	def test_mashap_126027492181(self): 
		r = c.get('/mashap/', {'prof': ''})

	def test_mashap_126027497898(self): 
		r = c.get('/mashap/', {'prof': ''})

	def test_mashap_126027536542(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"16.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0574960470049")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"27828.0000687")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126027539613(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126027551103(self): 
		r = c.get('/mashap/', {'prof': ''})

	def test_mashap_126027554989(self): 
		r = c.get('/mashap/', {'prof': ''})

	def test_mashap_126027569605(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"2546.99993134")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126027569944(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_12603573165(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"12859.000206")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126035733114(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126035954848(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"15.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.551876392858")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"2717.99993515")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126035955197(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126035958506(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"15.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0125147047815")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"119858.999968")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashap_126035989309(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"6437.00003624")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126035990206(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126036151223(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (11, 'SQL'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"18515.0001049")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126036153959(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126036803077(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"2453.00006866")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_faviconico_126036803405(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashap_126044659019(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"16.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.144430401705")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"11078.0000687")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_accountslogin_126044660295(self): 
		r = c.get('/accounts/login/', {'next': '/mashap/?prof'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"500.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"3")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")
		tmpl = template.Template(u"""{% load i18n %}{% trans 'Log in' %}""")
		context = template.Context({})
		self.assertEqual(tmpl.render(context), u"Log in")
		tmpl = template.Template(u"""{% load i18n %}{% trans "Forgot password" %}""")
		context = template.Context({})
		self.assertEqual(tmpl.render(context), u"Forgot password")
		tmpl = template.Template(u"""{% load i18n %}{% trans "Not member" %}""")
		context = template.Context({})
		self.assertEqual(tmpl.render(context), u"Not member")

	def test_stylecss_126044660386(self): 
		r = c.get('/style.css', {})
		self.assertEqual(r.status_code, 404)

	def test_accountslogin_126044663405(self): 
		r = c.post('/accounts/login/', {'username': 'admin''password': 'admin''next': '/mashap/?prof'})

	def test_mashap_126044663427(self): 
		r = c.get('/mashap/', {'prof': ''})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"47.000169754")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashap_126044665878(self): 
		r = c.post('/mashap/', {'upload_button': 'Upload'})

	def test_mashapverify_model_126044666292(self): 
		r = c.get('/mashap/verify_model/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapverify_model_126044669364(self): 
		r = c.post('/mashap/verify_model/', {'game_description': 'test01 description''name': 'test01''submit': 'Submit''purpose': 'purpose test01'})

	def test_mashapdefine_initial_params_126044669381(self): 
		r = c.get('/mashap/define_initial_params/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapdefine_initial_params_12604467940(self): 
		r = c.post('/mashap/define_initial_params/', {'initial_params': '18''submit': 'Submit'})

	def test_mashapdefine_time_settings_126044679961(self): 
		r = c.get('/mashap/define_time_settings/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapdefine_time_settings_126044681814(self): 
		r = c.post('/mashap/define_time_settings/', {'record_period': '1''time_step': '0.5''total_game_time': '100''time_between_decision_steps': '7''submit': 'Submit'})

	def test_mashapdefine_decision_params_126044681834(self): 
		r = c.get('/mashap/define_decision_params/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapdefine_decision_params_126044684319(self): 
		r = c.post('/mashap/define_decision_params/', {'decision_params': '75''submit': 'Submit'})

	def test_mashapdefine_outputs_126044684873(self): 
		r = c.get('/mashap/define_outputs/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapdefine_new_output_group_126044685225(self): 
		r = c.get('/mashap/define_new_output_group/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"15.9997940063")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapdefine_new_output_group_126044686766(self): 
		r = c.post('/mashap/define_new_output_group/', {'variables': '86''name': 'body weight''submit': 'Submit'})

	def test_mashapdefine_outputs_126044686784(self): 
		r = c.get('/mashap/define_outputs/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapdefine_game_management_settings_12604468713(self): 
		r = c.get('/mashap/define_game_management_settings/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapdefine_game_management_settings_126044688109(self): 
		r = c.post('/mashap/define_game_management_settings/', {'notification_email_address': 'mm@mm.com''submit': 'Submit'})

	def test_mashapaccess_data_126044688133(self): 
		r = c.get('/mashap/access_data/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapintroduce_game200912101404_test01_126044688673(self): 
		r = c.get('/mashap/introduce_game/200912101404_test01/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapinput_initial_values_126044689102(self): 
		r = c.get('/mashap/input_initial_values/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"16.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"99.9997973446")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"16.0000324249")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapinput_initial_values_126044690345(self): 
		r = c.post('/mashap/input_initial_values/', {'pi_0': '500''ci_0': '1500''submit': 'Submit''fi_0': '1000''baseline_bodyweight': '73000'})

	def test_mashapgame_basic_126044690727(self): 
		r = c.get('/mashap/game_basic/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapgame_basic_126044692341(self): 
		r = c.post('/mashap/game_basic/', {'pi_input': '1000''ci_input': '1200''activity_level': '60''fi_input': '300''submit': 'Submit'})

	def test_mashapgame_basic_12604469277(self): 
		r = c.get('/mashap/game_basic/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_site_mediaimagesbody_weight_1png_126044692802(self): 
		r = c.get('/site_media/images/body_weight_1.png', {})
		self.assertEqual(r.status_code, 200)

	def test_mashapgame_basic_12604469402(self): 
		r = c.post('/mashap/game_basic/', {'pi_input': '950''ci_input': '1200''activity_level': '45''fi_input': '340''submit': 'Submit'})

	def test_mashapgame_basic_126044694338(self): 
		r = c.get('/mashap/game_basic/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapgame_basic_126044694578(self): 
		r = c.get('/mashap/game_basic/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["query_time"]), u"16.0")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["query_percentage"]), u"99.9997973446")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"16.0000324249")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_site_mediaimagesbody_weight_1png_126044694613(self): 
		r = c.get('/site_media/images/body_weight_1.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_126044694638(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_mashapgame_basic_126044697459(self): 
		r = c.post('/mashap/game_basic/', {'pi_input': '340''ci_input': '1200''activity_level': '30''fi_input': '490''submit': 'Submit'})

	def test_mashapgame_basic_126044697711(self): 
		r = c.get('/mashap/game_basic/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_mashapgame_basic_126044697869(self): 
		r = c.get('/mashap/game_basic/', {})
		self.assertEqual(r.status_code, 302)
		self.assertEqual(unicode(r.context[-1]["logging_show_hints"]), u"True")
		self.assertEqual(unicode(r.context[-1]["logging_log_sql"]), u"False")
		self.assertEqual(unicode(r.context[-1]["logging_show_metrics"]), u"True")
		self.assertEqual(unicode(r.context[-1]["levels"]), u"[(0, 'NOTSET'), (10, 'DEBUG'), (20, 'INFO'), (30, 'WARNING'), (40, 'ERROR'), (50, 'CRITICAL')]")
		self.assertEqual(unicode(r.context[-1]["elapsed_time"]), u"0.0")
		self.assertEqual(unicode(r.context[-1]["records"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["query_count"]), u"2")
		self.assertEqual(unicode(r.context[-1]["LANGUAGE_CODE"]), u"en-us")
		self.assertEqual(unicode(r.context[-1]["hints"]), u"{}")

	def test_site_mediaimagesbody_weight_1png_12604469790(self): 
		r = c.get('/site_media/images/body_weight_1.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_126044697925(self): 
		r = c.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)
