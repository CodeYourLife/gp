"""
WSGI config for gerloff_painting project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
import django
path='/Users/TaroliFamily/work_projects/gerloff_painting'

if path not in sys.path:
  sys.path.append(path)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerloff_painting.settings')
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
