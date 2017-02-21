import nlm.occs

from .base import *

# integration server = development server = "Groucho"

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'project_hostname.nlm.nih.gov']

# Modify the following sections to use the correct Oracle schema and
# user for the integration phase of this project.

password = nlm.occs.getpass('user_name', 'database_name')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'database_name',
        'USER': 'user_name',
        'PASSWORD': password,
        'HoST': '',
        'PORT': '',
        # 'TEST': { },
    }
}
