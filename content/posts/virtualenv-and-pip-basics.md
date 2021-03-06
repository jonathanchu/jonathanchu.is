+++
date = 2011-02-09T00:00:00-04:00
title = "Virtualenv and pip Basics"
description = ""
slug = "virtualenv-and-pip-basics"
tags = ["python", "virtualenv", "pip"]
categories = ["python"]
externalLink = ""
series = []
+++

When doing any kind of Python development, one tool I find indispensable
is [virtualenv](http://pypi.python.org/pypi/virtualenv). Virtualenv,
along with
[virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)
and [pip](http://pypi.python.org/pypi/pip), make for a great way to
completely isolate your development environment.

When I first started out developing Django sites, I used to use
[easy\_install](http://packages.python.org/distribute/easy_install.html)
to install all packages I needed to the system-wide `site-packages`
directory. Even as a newbie to Django, I knew this wasn't good practice,
but it ensured that commonly used libraries such as `MySQL-python` was
available without any extra configuration with new projects. Regardless,
completely isolating your environment with virtualenv ensures that a)
you don't install conflicting packages and b) any bugs introduced in
your project can be traced back directly to the packages you installed.
Also, a huge benefit is that it makes installing multiple versions of
Python super easy without having to create any symlinks.

Getting started with Virtualenv and pip
---------------------------------------

The first thing you will need to do is install pip. If you have
setuptools installed, which you most likely will with most modern
platforms, you can install pip through easy\_install:

    easy_install pip

Next, you'll need to install virtualenv with pip:

    pip install virtualenv

Finally, I would highly recommend installing virtualenvwrapper as it
makes it much easier to create and start virtual environments:

    pip install virtualenvwrapper

As part of the install instructions for virtualenvwrapper, you need to
add this to your .bash\_profile

    # virtualenv
    export WORKON_HOME=$HOME/.virtualenvs
    source /Library/Frameworks/Python.framework/Versions/2.7/bin/virtualenvwrapper.sh

> Please note that this path may differ depending on what version of
> Python you have. Also, I like to keep all my virtualenvs in a
> directory called `.virtualenvs` in my home directory, but this may
> differ for you if you choose to keep your virtual environments in a
> different directory.

Make sure you source your new `.bash_profile`

    source ~/.bash_profile

...and that's it! Now you're all set to start using virtual
environments!

Creating a Virtual Environment
------------------------------

A few handy aliases I have in my `.bash_profile` are found on [Doug
Hellmann's
blog](http://blog.doughellmann.com/2010/01/virtualenvwrapper-tips-and-tricks.html)
and listed below:

    # virtualenv aliases
    # http://blog.doughellmann.com/2010/01/virtualenvwrapper-tips-and-tricks.html
    alias v='workon'
    alias v.deactivate='deactivate'
    alias v.mk='mkvirtualenv --no-site-packages'
    alias v.mk_withsitepackages='mkvirtualenv'
    alias v.rm='rmvirtualenv'
    alias v.switch='workon'
    alias v.add2virtualenv='add2virtualenv'
    alias v.cdsitepackages='cdsitepackages'
    alias v.cd='cdvirtualenv'
    alias v.lssitepackages='lssitepackages'

This saves some keystrokes, especially since I always create new virtual
environments with the `--no-site-packages` switch to ensure a completely
clean environment.

To create and start a new virtual environment with `--no-site-packages`,
enter:

    $ v.mk myvirtualenv
    New python executable in myvirtualenv/bin/pythonInstalling setuptools............done.
    (myvirtualenv) $

This creates and virtual environment and makes it active. To deactivate
it, you can simply type:

    (myvirtualenv) $ deactivate
    $

So let's go ahead and start our virtual environment once again and
install some packages to it.

    $ v myvirtualenv
    (myvirtualenv) $

We're going to install Python package `Yolk` as it is a useful command
line utility that lists the packages installed for the environment.

    (myvirtualenv) $ pip install yolk
    Downloading/unpacking yolk
      Downloading yolk-0.4.1.tar.gz (80Kb): 80Kb downloaded
      Running setup.py egg_info for package yolk

    Requirement already satisfied (use --upgrade to upgrade): setuptools in /Users/jonathan/.virtualenvs/myvirtualenv/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg (from yolk)
    Installing collected packages: yolk
      Running setup.py install for yolk

        Installing yolk script to /Users/jonathan/.virtualenvs/myvirtualenv/bin

    Successfully installed yolk
    Cleaning up...

Now you can use `yolk -l` to list the packages installed for this
virtual environment:

    (myvirtualenv) $ yolk -l
    Python          - 2.7.1        - active development
    (/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload)
    pip             - 0.8.1        - active
    setuptools      - 0.6c11       - active
    wsgiref         - 0.1.2        - active development
    (/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7)
    yolk            - 0.4.1        - active

Here is a brief one-line example showing how to create a virtualenv and
install Django, MySQL Python, South, Python Imaging Library (PIL), and
ImageKit using pip:

    $ v.mk newdjangoenv
    (newdjangoenv) $ pip install django MySQL-python south pil django-imagekit

When you have your requirements installed, it's always good to take a
snapshot of the requirements and the current versions. You can do this
by typing `freeze` and specifying an output file:

    (newdjangoenv) $ pip freeze > requirements.txt

And finally, you can use the `requirements.txt` file so that your
environment is completely and easily replicable:

    $ pip install -r requirements.txt

And there you have it -- you can now create and test your Python
applications in completely isolated environments!

For more on pip and virtualenv, check out this great post by [Salty
Crane](http://www.saltycrane.com/blog/2009/05/notes-using-pip-and-virtualenv-django/)
which got me started on all this.
