Title: Virtualenv and pip Basics
Date: 2011-02-09 00:00
Slug: virtualenv-and-pip-basics

<section>
</p>
<span>Virtualenv and pip Basics</span>
======================================

</p>
<div class="row">

</p>
<div class="span12 post">

</p>
When doing any kind of Python development, one tool I find indispensable
is [virtualenv](http://pypi.python.org/pypi/virtualenv). Virtualenv,
along with
[virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)
and [pip](http://pypi.python.org/pypi/pip), make for a great way to
completely isolate your development environment.

</p>
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

</p>
Getting started with Virtualenv and pip
---------------------------------------

</p>
The first thing you will need to do is install pip. If you have
setuptools installed, which you most likely will with most modern
platforms, you can install pip through easy\_install:

</p>
    easy_install pip

</p>
Next, you'll need to install virtualenv with pip:

</p>
    pip install virtualenv

</p>
Finally, I would highly recommend installing virtualenvwrapper as it
makes it much easier to create and start virtual environments:

</p>
    pip install virtualenvwrapper

</p>
As part of the install instructions for virtualenvwrapper, you need to
add this to your .bash\_profile

</p>
    # virtualenvexport WORKON_HOME=$HOME/.virtualenvssource /Library/Frameworks/Python.framework/Versions/2.7/bin/virtualenvwrapper.sh

</p>
> </p>
> > </p>
> > \*Please note that this path may differ depending on what version of
> > Python you have. Also, I like to keep all my virtualenvs in a
> > directory called `.virtualenvs` in my home directory, but this may
> > differ for you if you choose to keep your virtual environments in a
> > different directory.
> >
> > </p>
> > <p>
>
> </p>
> <p>

</p>
Make sure you source your new `.bash_profile`

</p>
    source ~/.bash_profile

</p>
...and that's it! Now you're all set to start using virtual
environments!

</p>
Creating a Virtual Environment
------------------------------

</p>
A few handy aliases I have in my `.bash_profile` are found on [Doug
Hellmann's
blog](http://blog.doughellmann.com/2010/01/virtualenvwrapper-tips-and-tricks.html)
and listed below:

</p>
    # virtualenv aliases# http://blog.doughellmann.com/2010/01/virtualenvwrapper-tips-and-tricks.htmlalias v='workon'alias v.deactivate='deactivate'alias v.mk='mkvirtualenv --no-site-packages'alias v.mk_withsitepackages='mkvirtualenv'alias v.rm='rmvirtualenv'alias v.switch='workon'alias v.add2virtualenv='add2virtualenv'alias v.cdsitepackages='cdsitepackages'alias v.cd='cdvirtualenv'alias v.lssitepackages='lssitepackages'

</p>
This saves some keystrokes, especially since I always create new virtual
environments with the `--no-site-packages` switch to ensure a completely
clean environment.

</p>
To create and start a new virtual environment with `--no-site-packages`,
enter:

</p>
    $ v.mk myvirtualenvNew python executable in myvirtualenv/bin/pythonInstalling setuptools............done.(myvirtualenv) $

</p>
This creates and virtual environment and makes it active. To deactivate
it, you can simply type:

</p>
    (myvirtualenv) $ deactivate$

</p>
So let's go ahead and start our virtual environment once again and
install some packages to it.

</p>
    $ v myvirtualenv(myvirtualenv) $

</p>
We're going to install Python package `Yolk` as it is a useful command
line utility that lists the packages installed for the environment.

</p>
    $ v myvirtualenv(myvirtualenv) $(myvirtualenv) $ pip install yolkDownloading/unpacking yolk  Downloading yolk-0.4.1.tar.gz (80Kb): 80Kb downloaded  Running setup.py egg_info for package yolkRequirement already satisfied (use --upgrade to upgrade): setuptools in /Users/jonathan/.virtualenvs/myvirtualenv/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg (from yolk)Installing collected packages: yolk  Running setup.py install for yolk    Installing yolk script to /Users/jonathan/.virtualenvs/myvirtualenv/binSuccessfully installed yolkCleaning up...

</p>
Now you can use `yolk -l` to list the packages installed for this
virtual environment:

</p>
    (myvirtualenv) $ yolk -lPython          - 2.7.1        - active development (/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload)pip             - 0.8.1        - activesetuptools      - 0.6c11       - activewsgiref         - 0.1.2        - active development (/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7)yolk            - 0.4.1        - active

</p>
Here is a brief one-line example showing how to create a virtualenv and
install Django, MySQL Python, South, Python Imaging Library (PIL), and
ImageKit using pip:

</p>
    $ v.mk newdjangoenv(newdjangoenv) $ pip install django MySQL-python south pil django-imagekit

</p>
When you have your requirements installed, it's always good to take a
snapshot of the requirements and the current versions. You can do this
by typing `freeze` and specifying an output file:

</p>
    (newdjangoenv) $ pip freeze > requirements.txt

</p>
And finally, you can use the `requirements.txt` file so that your
environment is completely and easily replicable:

</p>
    $ pip install -r requirements.txt

</p>
And there you have it -- you can now create and test your Python
applications in completely isolated environments!

</p>
For more on pip and virtualenv, check out this great post by [Salty
Crane](http://www.saltycrane.com/blog/2009/05/notes-using-pip-and-virtualenv-django/)
which got me started on all this.

</p>
<p>

</div>

</p>
<div class="post-date">

</p>
<span>-- Feb 09, 2011</span>

<p>

</div>

</p>
<p>

</div>

</p>
<p>
</section>
</p>

