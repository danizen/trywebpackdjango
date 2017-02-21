import nlm.occs

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.nlm.nih.gov']

# Modify the following sections to use the QA Oracle schema and user
# for this project.

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
