# Static Files, Template Tags, runserver, and Apache

## Template tags

We have three kinds of template tags for serving static files. Each one includes some mechanism for  rendering the path to a static file.

- `{% static PATH %}` is the standard Django tag.
- `{% nlm_static PATH %}` serves from the root of `www.nlm.nih.gov`.
- `{% assets_static PATH %}` is specifically for static files within the `assets.cms.gov` distribution.

## File Finding with the `assets_static` tag

The Visible application uses a (highly-recommended) collection of resources gathered by cms.gov to help the creation of §508-compliant websites related to the Affordable Care Act. These are the files meant to be served using the `assets_static` tag. You can read more about them at `http://assets.cms.gov`. The collection includes:

* Bootstrap 3
* FontAwesome icons font
* jQuery
* jQuery-ui
* Some CMS JavaScript utilities for accessibility
* JavaScript utilties like modernizr, underscore, lodash, and require.js

There are two settings for handing `assets.cms.gov`.

### `ASSETS_STATIC_REMOTE_PREFIX`

We don't have a permanent home for these files, but there is a temporary home at `assets-qa.nlm.nih.gov`. Visible therefore comes with this setting in `base.py`:

`ASSETS_STATIC_REMOTE_PREFIX = '//assets-qa.nlm.nih.gov/assets/3.4.1/'`

This tag tells the `assets_static` tag to append the specific asset name you want (i.e. `jquery/jquery.js`) to the actually static resource (i.e. `http://www.example.com/assets/3.4.1/jquery/jquery.js` should get you a copy of jQuery).

### `ASSETS_STATIC_LOCAL`

If for some reason you'd rather use a local copy of these files, you can instead use `ASSETS_STATIC_LOCAL`.
That means, for now:

- Download or copy the assets.cms.gov zip file into the Django project directory. That is, if your main project directory is `PROJECT_DIR`, such that there is for example a file `PROJECT_DIR/passenger_wsgi.py`, then create the directory `PROJECT_DIR/assets`, copy the zip file into that directory, and then expand it. When you're done, there should be something like, for example, `PROJECT_DIR/assets/3.4.1/backbone/backbone.js`.
- Make sure that your `.gitignore` file is set up to ignore the `assets` subdirectory so that you don't check it all into git.
- Add `ASSETS_STATIC_URL = os.path.join(BASE_DIR, "../assets/3.4.1")` (for whichever version) into your settings.

## File Finding with the `nlm_static` tag

This one is simple, and doesn't change depending on the stage of development. `{% nlm_static PATH %}` is *always* `www.nlm.nih.gov/PATH`.

## File Finding with the `static` tag

This part is plain ol' Django, but it's worth a little more explaination because it can be confusing.

The most important thing to know is that that the way static files are found and served differs depending on the value of `DEBUG`. 

### `DEBUG` = `True`

`runserver` includes what even Django docs call a "quick and dirty" static file server, thoroughly meant for development only ("grossly inefficient and probably insecure"). It's a crutch.

In this case, `{% static PATH %}` will resolve (as determined by the setting `STATICFILES_FINDERS`) by looking
- in any directories you've specified in `STATICFILES_DIRS`, and
- in the `static` subdirectories of all the apps listed in `INSTALLED_APPS`.
It serves the first one it finds.

### Transition: `collectstatic`

The commandline `manage.py collectstatic` will use the methods of the `DEBUG` = `True` case to gather all the static files it can spot using its static file finders, and copy them into a directory specified by `STATIC_ROOT`.

Then deploying the static files to whatever becomes simply a matter of copying the `STATIC_ROOT` directory there, or else setting up Apache (or nginx) to serve from that directory.

### `DEBUG` = `False`

When `DEBUG` = `False`, the crutch static server goes away, and you will need to have configured some alternate way of serving the static files.

## Naming convention for your static files and templates

Inside apps (not your project, but the apps inside it), use this layout for templates and static files. 

* *app_name*
    - `templates`
        - *app_name* 
            - *.html
    - `static`
        - `js`
            - *app_name* 
                - *.js
        - `css`
            - *app_name* 
                - *.css
        - `images`
            - *app_name* 
                - *.jpg
                - *.png

This avoids name conflicts, which is important; if you have two apps, both of which have a `app_name/static/images/pic.jpg`, then `manage.py collectserver` will try to put them both at `/public/images/pic.jpg` and one will be overwritten. 

## What the settings mean

### `STATIC_ROOT`

This setting is an absolute path to the directory into which `manage.py collectstatic` will harvest a project's static files. There's no default; we have to spell it out directly. Here it tends to be `BASE_DIR/public/`.

### `STATIC_URL`

This setting is used by the `static` tag to generate the URLs for static files. `{% static PATH %}` will generate `STATIC_URL/PATH`. For example, if `STATIC_URL` is `/static/`, then `{% static 'img/home.png' %}` will generate `/static/img/home.png`, and that's the path that the browser will expect the resource to be at.

When `DEBUG` is `True`, `views.serve` will serve the files whose locations it's resolved using the various finders *as if* they were all in the directory `STATIC_URL` even though they're not. That is, it'll act *as if* you've already run a `collectstatic` and are serving everything from the resulting directory. It's very helpful in development, but it makes it a little harder to understand what happens with static files when you `collectstatic` and then switch `DEBUG` off.

### `STATICFILES_DIRS`

This setting lists directories to be searched by `AppDirectoriesFinder`, part of the default static file resolver.

The default is `[]`.

### `STATICFILES_STORAGE`

If you want to serve the static files from some other CDN or cloud service, changing this default to some a custom file storage backend would allow `collectstatic` to deliver the files right to the offsite location ready to serve. 

I haven't played with this and am probably not going to.

### `STATICFILES_FINDERS`

This setting specifies which static file finders runserver's internal `views.serve` will use when `DEBUG` is `True`, and therefore where the static files should be. The default is to use two finders defined in `django.contrib.staticfiles.finders`. 
- `FileSystemFinder` tells the resolver to look in the directories designated by the `STATICFILES_DIRS` setting.
- `AppDirectoriesFinder` tells the resolver to look in the `static` subdirectory of each app.
It's possible to override these algorithms by changing the `STATICFILES_FINDERS` setting, but again, I haven't had a reason to change this.
