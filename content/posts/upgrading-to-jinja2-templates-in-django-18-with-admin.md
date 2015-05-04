Title: Upgrading to Jinja2 Templates in Django 1.8 With Admin
Date: 2015-04-26 00:00
Slug: upgrading-jinja2-templates-django-18-with-admin
Category: Python
Tags: python, django


In Django 1.8, a new template system was introduced along with the
ability to choose a templating engine, with Jinja2 having built-in
support. I tried this out on a newly created Django project and
getting setup with Jinja2 was trivial following the docs; however,
upon checking the `/admin` page, I was greeted with this:

<img src="/images/django_admin_error_screenshot.png" alt="Django Admin error screenshot" width="510px" class="centered">

Ah, right! The contrib app Admin does not ship with Jinja2 templates.
I read through the docs and did not see any mention of using a
different template engine in combination with the Django Admin, so I
thought I'd share how I solved this to get Jinja2 and the Django Admin
templates to work together.

## Jinja2 + Django Templates for Admin

First, here is a link for the upgrade path to use the new templating
system:
[https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/](https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/)

*Take note of the section that tells you when you can remove things
 like `TEMPLATE_DIRS`, `TEMPLATE_CONTEXT_PROCESSORS`, etc.*

##### Install Jinja2

Make sure `Jinja2` is installed:

    $ pip install jinja2

##### In `settings.py`

In my `settings.py`, here is how I defined my `TEMPLATES` list:

    :::python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.jinja2.Jinja2',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates/jinja2'),
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'environment': 'myproject.jinja2.environment',
            },
        },
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]


You need to define both backends in the `TEMPLATES` setting to be able
to use the Django Admin.

##### Create directory for `jinja2` templates

Next, create a `jinja2` directory in your project's `templates`
directory.  This is where we are going to put all our Jinja2
templates.

    $ cd <path_to_project>/templates && mkdir jinja2

##### Create `jinja2.py`

Finally, create a file called `jinja2.py` under your project directory
(should be at the same level as your `settings.py`):

    $ cd myproject && touch jinja2.py

And put this in there:

    :::python
    from django.contrib.staticfiles.storage import staticfiles_storage
    from django.core.urlresolvers import reverse
    from jinja2 import Environment


    def environment(**options):
        env = Environment(**options)
        env.globals.update({
            'static': staticfiles_storage.url,
            'url': reverse,
        })
        return env

This makes `static` and `url` available in your Jinja2 templates.

Here's a [tree](http://mama.indstate.edu/users/ice/tree/) of the final project structure:

    $ tree myproject
    myproject
    ├── myproject
    │   ├── __init__.py
    │   ├── jinja2.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── templates
    │   └── jinja2
    │       ├── base.html
    │       ├── home.html


##### PR0FIT!

And that should do it!  If you go to `/admin/` you should see a
working admin login.  Additionally, whatever templates you put in the
`templates/jinja2` directory will be processed by the Jinja2 template
engine.
