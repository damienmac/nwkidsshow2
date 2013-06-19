# The Most Minimal main.py
# import os
# from google.appengine.ext.webapp import util
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
# from django.core.handlers import wsgi
#
# def main():
#     app = wsgi.WSGIHandler()
#     util.run_wsgi_app(app)
#
# if __name__ == '__main__':
#     main()

import os,sys

#sys.path.append('C:\\Users\\Damien\\PycharmProjects\\nwkidsshow')
#print sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'nwkidsshow.settings'
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


# Force Django to reload its settings.
from django.conf import settings
settings._target = None

import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch

# Log errors.
#import logging
#def log_exception(*args, **kwds):
#    logging.exception('Exception in request:')
#
#django.dispatch.Signal.connect(
#    django.core.signals.got_request_exception, log_exception)

# Unregister the rollback event handler.
django.dispatch.Signal.disconnect(
    django.core.signals.got_request_exception,
    django.db._rollback_on_exception)

app = django.core.handlers.wsgi.WSGIHandler()
