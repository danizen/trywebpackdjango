# Django Example Project Layout

A guide to what's where and why. 

## Assumptions

### I assume you've cloned the example project.

I'm going to signify the root directory of the project source as `ROOT` in the various paths below.

## The basic tree

The tree below omits the various appearances of `__init__.py` and `__pycache__`, which are standard parts of the python package mechanism.

* `docs`, some documentation, including this document, in Markdown format.
* `moviedb`, my sample app
	* `apps.py`, auto-generated
	* `data`, where I put any data fixtures (sample data in JSON for importing into the project)
	* `edit_views.py`, a set of generic View classes with some extra sauce for the CRUD pattern.
	* `forms.py`, a set of Form classes for editing various Model types
	* `migrations`, where `manage.py makemigrations` and `manage.py migrate` store (some) of their migration information.
	* `models.py`, where the app's models are declared.
	* `static`, a folder for static files (js, css, images) specific to the application
	* `templates/moviedb`, a folder for templates specific to the application
* `public`, a directory you may not have yet; see below for the gory details.
* `conf` (or whatever you've named your project)
	* `db.sqlite3` (if that's what you're developing with locally, although it may not be there until you do your first migrate)
	* `urls.py`, the mapping of URLs onto Django views
	* `wsgi.py`, the `WSGI` application, for when you're running `manage.py runserver`
	* `settings`
		* `base.py`, where most of the Django settings are
		* `dev_oracle.py`, `dev_sqlite3.py`, `integration.py`, `qa.py`, and `prod.py`, containing only the settings differences required for the various stages of development and deployment; each one of these inherits almost all of its settings from `base.py`.
* `deploy.json`, a file containing deployment configuration information used by `passenger_wsgi.py`.
* `manage.py`, a command-line utility for all sorts of Django tasks, including `manage.py runserver` and `manage.py migrate`.
* `passenger_wsgi.py`, the WSGI interface used by the integration, qa, and production servers.

	 
## Gory Details

### `public`

A Django project is going to be in one of two states, depending on the value of the `DEBUG` flag in settings. 

If `DEBUG` is `True`, then Django figures you're still in development, and probably still using the `manage.py runserver` command. Accordingly, when it needs to serve a static file of some sort (an image, or some JavaScript) via the `static` template tag, it will look at each of the apps listed in settings (`INSTALLED_APPS`) and look for a `static` directory in each app, serving up the first file that matches the specified file.

When `DEBUG` isn't `True`, Django assumes you're in production, that you no longer are using the `manage.py runserver`, and that Apache (or whatever server you're using) will deliver static files separately. Accordingly, it will no longer search app directories for static files.

To prepare for that switch, the `manage.py collectstatic` command can copy all the static files into one directory, which is specified as `STATIC_ROOT` in settings. Then Apache (or whatever) can serve the static files straight from that directory.
