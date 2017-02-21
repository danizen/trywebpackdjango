# Django Example Project Installation

A guide to getting started with python-django-visible.

To create a new project from the `visible` template, do the following:


## Make sure your Python/Django environment is set up. 

You'll find information on how to install and set up the Python/Django environment on [the NLM-OCCS wiki](https://wiki.nlm.nih.gov/confluence/display/OCCS/Python+Getting+Started).


*Note: You will need to make sure you're using Python 3.5 minimum. 

## Create and log into a virtual Python environment.
This step is optional but highly recommended.
* [Windows guidelines](http://www.voidynullness.net/blog/2014/06/19/install-python-setuptools-pip-virtualenvwrapper-for-powershell-pyside-on-windows/)
* [Mac tips](http://exponential.io/blog/2015/02/10/install-virtualenv-and-virtualenvwrapper-on-mac-os-x/)
* [Linux instructions](http://exponential.io/blog/2015/02/10/install-virtualenv-and-virtualenvwrapper-on-ubuntu/)

## Create your project.

There are two different ways to do use the project's zip file as a project template. You can specify the zip file to `django-admin` by giving a URL, or you can download the zip file and then use it as a template. We'll describe both methods.

*Note! That zip file isn't quite a Django application; expanding it directly probably won't get you what you think. It's a Django application __template__, with some text macros that need to be resolved by the `django-admin startproject` command described below.*
 
### Method One: Specify the zip file by URL.

Go into the directory you'll be developing in, and enter the following:

`django-admin startproject --template https://occspydev.nlm.nih.gov/templates/python-django-visible.zip project-name`

### Method Two: Get the python-django-visible code as a zip file.

#### Get the zip file.

Navigate to the project's repository directly [with this link](https://git-scm.nlm.nih.gov/projects/PYTHON/repos/python-django-visible/browse). Click the "..." icon to the far left, and choose "download."

To minimize typing, you can move the python-django-visible archive to the directory where you store your code.

#### Create your project.

Run the following, which will create a new project using the code in python-django-visible as the template:

`django-admin startproject your-project-name --template /location/of/template/if/different/python_django_visible_downloaded_archive_name.zip`

You should see a new directory by the name specified in your-project-name.
You can delete the compressed template now if you like.


### Make sure you've installed the `nlm-occs` library.

If you used the "Easy Button" described on [the NLM-OCCS wiki](https://wiki.nlm.nih.gov/confluence/display/OCCS/Python+Development+Environment), you should have this package installed already. Otherwise:

* [download python-nlm-occs archive](https://git-scm.nlm.nih.gov/projects/PYTHON/repos/python-nlm-occs/browse)

* Click on the "..." icon to the left and download.

* `cd ~/Downloads`

* `pip install python-nlm-occs.zip`


### Install the other requirements:

* `cd <Wherever you put your code>`

* `pip install -r requirements/develop.txt`

### Sqlite3 versus Oracle

Django can work with either Oracle or sqlite3 (although it works with other SQL DBs as well).

* If you're using sqlite3, Django will use a file in your project Django directory as the data store. It will probably be called `db.sqlite3`. Make sure that you're not checking it into git by including it in your `.gitignore` file.
* If you're using an Oracle database, you'll need to specify the connection details in the file `conf/settings/dev_oracle.`

### OPTIONAL: Set the DJANGO_SETTINGS_MODULE path so you won't have to specify it every time you run a command.

#### In virtualenv:

* Navigate to the virtual environment's home. Modify postactivate. Commands put here will fire every time you start the environment.


* `export DJANGO_SETTINGS_MODULE=conf.settings.dev_sqlite3` or `...dev_oracle`

* If you'd like to automatically be taken to your code on startup, add this:
		* `cd ~/your/code/location/your-project-name`

* In postdeactivate file, if desired, unset the settings.
		* `unset DJANGO_SETTINGS_MODULE`

#### If you're not using virtualenv:

This will vary by which IDE you're using, but find your IDE's favorite way to add the environment setting
 
	* `DJANGO_SETTINGS_MODULE=conf.settings.dev_sqlite3` or 
	* `DJANGO_SETTINGS_MODULE=conf.settings.dev_oracle`


If you successfully pointed to the development settings using one of the methods above, you should be able to run everything below as-is. However, if you have problems setting `DJANGO_SETTINGS_MODULE`, you can specify them when you run the commands by adding ` --settings=conf.settings.dev_sqlite3` to the end of each `manage.py` command.

### Create the database

Django should be able to automatically create the tables for you:

* `python manage.py makemigrations`
* `python manage.py migrate`

If you're using sqlite3, it will also create the file it uses for the data store if it doesn't already exist.

### Load some data into the app

There is some sample data to load into the app in the form of a JSON file.

* `python manage.py loaddata moviedb/data/moviedb.json` 


### Create some administrative users

Authorization and authentication in our environment is done via users and groups. 
The Visible application is set up to require a user to be part of group `editor` in order
to create or edit information. (Look in `conf/urls.py` to see how that's specified
using Python decorators.) So to get to those pages, we'll need to set up some initial
permissions.

* `python manage.py creategroup --group admin`
* `python manage.py creategroup --group editor`
* `python manage.py createuserinteractive` (this is an interactive command that will prompt you for information)
* `python manage.py addusertogroup --username` _username_ `--group admin`
* `python manage.py addusertogroup --username` _username_ `--group editor`

Users in group `editor` have the ability to add and change information in movie database.

Users in group `admin` have the ability to add or remove users in the `editor` group through the application using the path _site_:`/admin/users/list`.

You'll only need to use the command-line commands when you're first setting up the application; from there on out, you can do it through the website.

### Run the application unit tests

*Note: the Django test framework runs unit tests in a separate database. This isn't a problem for sqlite, but for Oracle this means that in `dev_oracle.py` you'll need to specify the test database as well as the regular one; see [this page](https://code.djangoproject.com/wiki/OracleTestSetup) for some tips.*

* `python manage.py test`

There might be a whole mess of messages that make you think things are failing. However, as long as the end result includes, "Ran XX tests in xxxxs" without "Test failed" errors you should be ok.

### Run the application

* `python manage.py runserver`

This command starts a (development only!) webserver at `127.0.0.1:8000`. Point your browser there and you should see the application running.

## That's it!
If you made it this far, you are the proud owner of a shiny new NIH-Approved Django App. Go forth and be codeful.

You'll find some more documents about the `Visible` project's innards in the project's `docs` directory.