# Django, CSRF, HTTP, and HTTPS

## CSRF_COOKIE_SECURE

When you're using `manage.py runserver` to run Django on your desktop, 
it's being presented through the HTTP protocol. But our Linux servers 
present applications through HTTPS. Fortunately, there's not much difference 
in what you need to do to have both cases work.

If things aren't right, you'll know when you try to submit a form
and you get an error page complaining about lack of a CSRF cookie,
with a notation in the runserver log that says `Forbidden (CSRF cookie not set.)`.

### CSRF

Django forms have a built-in security mechanism to guard against
CSRF -- cross-site request forgeries -- by sending with each form
a hidden extra field with a unique (and session-specific) string, 
which is also written to a cookie. When you submit a form, Django's
form processing logic will check that hidden field from the submitted
form against the value in the cookie.

This cookie, however, is treated in slightly different ways 
under HTTP and HTTPS.

The Django docs describe the setting `CSRF_COOKIE_SECURE` like
this:

If this is set to True, the cookie will be marked as “secure,” 
which means browsers may ensure that the cookie is only sent with 
an HTTPS connection.

### Desktop: HTTP

On the settings module you use to develop on the desktop --
probably `conf.settings.dev_sqlite3` or `conf.settings.dev_oracle` --
you should make sure the setting `CSRF_COOKIE_SECURE` is set
to `False`. 

This allows the cookie to be set and read under the HTTP protocol.

### Groucho, QA, Production: HTTPS

For serving under HTTPS -- as all the Django applications are
on Groucho (or 'integration' or 'staging' or whatever you
want to call it, so I call it Groucho), on QA, and an Prod --
`CSRF_COOKIE_SECURE` needs to be set to `True`.