from django.conf import settings
from django.http import HttpResponse
import sys, StringIO, os
import re
import cProfile
import pstats

PROFILE_DATA_DIR = "./profile"
class ProfileMiddleware(object):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        if (settings.DEBUG or request.user.is_superuser):
            path = getattr(settings, 'PROFILE_DIR', PROFILE_DATA_DIR)
            self.profname = "%s.prof" % (request.path.strip("/").replace('/', '.'))
            self.profname = os.path.join(PROFILE_DATA_DIR, self.profname)
            callback_args = (request,) + callback_args
            params = {'callback': callback, 'callback_args': callback_args, 'callback_kwargs':callback_kwargs}
            cProfile.runctx('callback(*callback_args, **callback_kwargs)', {}, params, filename=self.profname)

    def process_response(self, request, response):
        if settings.DEBUG:
            out = StringIO.StringIO()
            old_stdout, sys.stdout = sys.stdout, out
            stats = pstats.Stats(self.profname)
            stats.strip_dirs().sort_stats('time').print_stats(20)
            sys.stdout = old_stdout

            close_body_re = re.compile("(</body>)", re.M | re.I)
            new_content = '<pre>%s</pre> </body>' % out.getvalue()
            response.content = close_body_re.sub(new_content, response.content)
        return response