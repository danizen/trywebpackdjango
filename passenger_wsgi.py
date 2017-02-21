"""
This passenger_wsgi.py is coded so that it should work for almost all NLM OCCS Django projects.
If your wsgi file has some other path, please update it.   Do not hard code:
   - the log directory
   - the settings module
Bamboo, DevTools, and DevOps install deploy.json so code will not need to be changed.
"""

import os
import json
from django.core.exceptions import ImproperlyConfigured

deploy_file = open('deploy.json')
if not deploy_file:
    raise ImproperlyConfigured('Must have file deploy.json')
deploy = json.loads(deploy_file.read())
deploy_file.close()

if 'log_dir' not in deploy:
    raise ImproperlyConfigured('Must provide "log_dir" in deploy.json')
if 'settings' not in deploy:
    raise ImproperlyConfigured('Must provide "settings" in deploy.json')

os.environ['DJANGO_LOG_DIR'] = deploy['log_dir']
os.environ['DJANGO_SETTINGS_MODULE'] = deploy['settings']

import conf.wsgi
application = conf.wsgi.application
