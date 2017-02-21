from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'test.db.sqlite3'),
        }
    }
}

AUTHENTICATION_BACKENDS = (
    'nlm.occs.casauth.backends.CASBackend',
    # 'django.contrib.auth.backends.ModelBackend',
)

CAS_SERVER_URL = 'https://logindev.nlm.nih.gov/cas/'

# for desktop only

CSRF_COOKIE_HTTPONLY = False

CSRF_COOKIE_SECURE = False
