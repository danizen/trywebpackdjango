'''
Temporarily overlay casauth_decorator() to check whether the URL for the request is within the 
protected namespace of django-cas-ng, and raise ImproperlyConfigured if it is not.

Created on May 4, 2016

@author: davisda4
'''
from functools import wraps
from django.conf import settings
from django.utils.decorators import available_attrs
from django.contrib.auth.decorators import user_passes_test
from nlm.occs.decorators import check_remote_isadmin
from nlm.occs.errors import RemoteIsNotAdminError, CASUserError


def casauth_required(view_func):
    '''
    Tests that:
        (a) The request is coming from a valid IP range,
        (b) The user is not anonymous,
        (c) The URL for this view is in the admin range used by django-cas-ng
    '''
    @wraps(view_func, assigned=available_attrs(view_func))
    def _wrapped_view(request, *args, **kwargs):
        if not check_remote_isadmin(request):
            raise RemoteIsNotAdminError
        nonlocal view_func
        if request.user.is_anonymous():
            raise CASUserError       
        admin_prefix = getattr(settings, 'CAS_ADMIN_PREFIX', None)
        if admin_prefix and not request.path.startswith(admin_prefix):
            raise CASUserError("This request is not in the admin URL")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def group_required(*group_names):
    '''
    Requires user membership in at least one of the groups passed in.
    Emits a 403 if user is unauthenticated or authorization fails.
    '''
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) or u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)
