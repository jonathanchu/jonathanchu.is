Title: Upgrading to Jinja2 Templates in Django 1.8 With Admin
Date: 2015-04-26 00:00
Slug: upgrading-jinja2-templates-django-18-with-admin
Category: Python
Tags: python, django


In Django 1.8, a new template system was introduced along with the
ability to choose a templating engine, with Jinja2 having built-in
support. I tried this out on a newly created Django 1.8 project and
getting setup with Jinja2 was trivial following the docs; however,
having a working Django admin was not really covered explicitly and I
thought I'd share how I got it working.

First, here is the docs for the upgrade path to use the new templating system:
https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/

In my `settings.py`, here is how I defined my `TEMPLATES` list:

```
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
```

You need to define both backends in the `TEMPLATES` setting to be able
to use the Django Admin.  The Djang Admin does not ship with Jinja2
templates.

Next, create a `jinja2` directory in your project's `templates`
directory.  This is where we are going to put all our Jinja2
templates.

Finally, create a file called `jinja2.py` under your project directory (should be at the same level as your `settings.py`) and put this in there:

```
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
```

This makes `static` and `url` available in your Jinja2 templates.
