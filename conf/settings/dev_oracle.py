from django.test.runner import DiscoverRunner

import nlm.occs

from .base import *

DEBUG = True


class UnManagedModelTestRunner(DiscoverRunner):
    """
    Test runner that automatically makes all unmanaged models in your Django
    project managed for the duration of the test run, so that one doesn't need
    to execute the SQL manually to create them.
    """

    def setup_test_environment(self, *args, **kwargs):
        from django.apps import apps
        self.unmanaged_models = [m for m in apps.get_models()
                                 if not m._meta.managed]

        for m in self.unmanaged_models:
            m._meta.managed = True
        super(UnManagedModelTestRunner, self).setup_test_environment(*args, **kwargs)

    def teardown_test_environment(self, *args, **kwargs):
        super(UnManagedModelTestRunner, self).teardown_test_environment(*args, **kwargs)

        # reset unmanaged models
        for m in self.unmanaged_models:
            m._meta.managed = False

TEST_RUNNER = 'conf.settings.dev_oracle.UnManagedModelTestRunner'
"""
You'll need to change 'user_name' and 'database_name' to the
project's settings. Also, the nlm password lookup table must have a
corresponding entry.
DG
"""
# password = nlm.occs.getpass('user_name', 'database_name')

"""
The following is for testing with Oracle. It is recommended that, during development,
you use sqlite3 - (dev_sqlite3.py)
To make the oracle tests work, we have to split them to point at different schemas
than the regular database. Because users don't get permission to drop/create db's or schemas
here, we've turned off those options.
From here on out, we're going to try to create separate test databases for each project.
In this case, that would be test_visible or something like that. (Has to start with "test_")
If that schema hasn't been created, you can't run oracle tests.
See the Django/Python documentation here for more information:
https://wiki.nlm.nih.gov/confluence/display/OCCS/Django+Guidelines+and+Advice
Here are the settings you will need to change to make the tests work:
TBLSPACE: Usually the same name as the db where your app lives, with a "test_"
USER: The test db user name
PASSWORD: the test db password.
"""

TEST_TBLSPACE = ''
TEST_USER = ''
TEST_PASSWORD = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'oltpdevracscan.nlm.nih.gov/oltp01_dev',
        'USER': 'django2_test',
        'PASSWORD': 'testDjang0_temp',
        'TEST_NAME': 'test_django2_test',
        'TEST': {
            'CREATE_DB': False,
            'CREATE_USER': False,
            'TBLSPACE': TEST_TBLSPACE,
            'USER': TEST_USER,
            'PASSWORD': TEST_PASSWORD,
        }
    },
}

CAS_SERVER_URL = 'https://logindev.nlm.nih.gov/cas/'

# for desktop only

CSRF_COOKIE_HTTPONLY = False

CSRF_COOKIE_SECURE = False
