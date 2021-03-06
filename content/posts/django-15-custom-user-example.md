+++
date = 2013-09-23T00:00:00-04:00
title = "Django 1.5 Custom User Example"
description = ""
slug = "django-15-custom-user-example"
tags = ["python", "django"]
categories = ["python"]
externalLink = ""
series = []
+++

With Django 1.5, one of the biggest changes introduced was the ability
to configure the user model. Anyone who has coded a Django app with a
business requirement of adding a birthday field, an arbitrary checkbox
to the user registration fields, or even making the signup process
email-only with no usernames, knows the awkward feeling of implementing
their own custom user and feeling a little less Django-esque when all is
said and done. This configurable user model change alone was enough for
me to 1) upgrade all my Django sites to 1.5 and to 2) swap out my
customer user code for the way it should be done now with the
configurable user model.

The Django docs are *fantastic*. It is one of the most comprehensive
and, most important, user-friendly documentations out there for
programmers of all skill levels. I highly encourage you to read through
the
[docs](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms)
first on customizing the user model, but isn't required to understand
this walk-through.

If you're anything like me, you sometimes like to skim or even skip the
docs altogether, and turn to Google to try and find a solid example
online. I found a few, but none of them really seemed to show me a full
example of configuring the user model. As a result, I decided to write
my own and put it all together in an example Django project to show how
I handled the custom user model. Here is the [link to the repo on
Github](https://github.com/jonathanchu/django-custom-user-example).

This is going to be a brief walk-through in running this example
codebase. It is opinionated, but (hopefully!) easily understood - so
this would enable you to modify this example codebase slightly to fit
your business requirements.

Also, this custom user example is inspired from [Dr. Russell
Keith-Magee's](https://twitter.com/freakboy3742) great talk at DjangoCon
US 2013 titled ["Red User, Blue User, MyUser,
auth.User"](https://speakerdeck.com/freakboy3742/red-user-blue-user-myuser-auth-dot-user)
and should serve as a good example for how you can change the core
fields of auth.User.

Please note - this walk-through will assume you have pip and virtualenv
installed locally, as we'll be using that to create the environment for
the example Django project.

**[View the source on
Github](https://github.com/jonathanchu/django-custom-user-example)**

First, clone the example custom user project and change directory into
it:

    $ git clone https://github.com/jonathanchu/django-custom-user-example.git
    $ cd django-custom-user-example

Then, create your virtual environment. We'll only be installing Django
(v1.5.4):

    $ mkvirtualenv customuser(customuser)
    $ pip install django

After Django is installed, let's run `syncdb` to create our test DB and
first superuser. This is configured out-of-the-box to use SQLite3 for
simplicity, but feel free to change to whatever database backend you
feel more comfortable with. Create your superuser now and follow the
prompts:

    (customuser) $ python manage.py syncdb...::Follow prompts to create a superuser::

Then we can run `runserver` to checkout how the custom users in the
admin looks:

    (customuser) $ python manage.py runserver

And open up your browser to http://127.0.0.1:8000/admin and log in with
the superuser you just created. Under "Accounts", you will see our
custom "Users" there. Try it out, take it for a spin, create additional
users from the admin, change passwords, etc. This all works nicely with
our custom user model!

![Django Custom User Screenshot](https://i.imgur.com/uaG4qaH.png)

Hopefully this is helpful to some out there looking for a solid example
on customizing the User model. Any issues with the codebase, please use
the repo's [issues
tracker](https://github.com/jonathanchu/django-custom-user-example/issues)
on Github. Happy hacking!

-- Sep 23, 2013
