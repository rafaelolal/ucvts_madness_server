"""
WSGI config for ucvts_madness_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os, sys

# add the virtualenv site-packages path to the sys.path
site_packages = '/home/rafaelolal/envs/ucvts_madness_server_env/lib/python3.10/site-packages'
if site_packages not in sys.path:
    sys.path.append(site_packages)

project_path = '/home/rafaelolal/ucvts_madness_server'
project_path2 = '/home/rafaelolal/ucvts_madness_server/ucvts_madness_server'

if project_path not in sys.path:
    sys.path.append(project_path)
if project_path2 not in sys.path:
    sys.path.append(project_path2)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ucvts_madness_server.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()