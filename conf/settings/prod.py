import nlm.occs

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.nlm.nih.gov']

# Modify the following sections to use the PRODUCTION Oracle schema
# and user.

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

# Logging

logdir = os.environ.setdefault('DJANGO_LOG_DIR', os.path.join(BASE_DIR, "logs"))

if not os.path.exists(logdir):
    os.mkdir(logdir)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'full': {
            'format': '[%(asctime)s] %(levelname)s %(name)s %(message)s',
        },
    },
    'handlers': {
        'file': {
            'formatter': 'full',
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'encoding': 'UTF-8',
            'when': 'H',
            'interval': 1,
            'filename': os.path.join(logdir, 'changing.log'),
        },
        'console': {
            'formatter': 'full',
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        # Use this for a custom app:
        #
        # 'app_name': {
        #    'handlers': ['file', 'console'],
        #    'level': 'INFO',
        #    'propogate': True,
        # },
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propogate': True,
        },
    },
}
