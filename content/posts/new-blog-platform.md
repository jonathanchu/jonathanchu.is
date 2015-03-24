Title: New Blog Platform
Date: 2011-01-18 00:00
Slug: new-blog-platform

<section>
</p>
<span>New Blog Platform</span>
==============================

</p>
<div class="row">

</p>
<div class="span12 post">

</p>
After a long blogging hiatus, I recently decided to switch over my
custom Django blog to a static site generator, following the trend that
[many](https://github.com/mojombo/jekyll)
[others](https://github.com/lakshmivyas/hyde) have started. What made
the switch so appealing, going from a full-featured blogging engine to a
simple static site generator, was that I could write my blog entries in
a text editor of my choice and keep everything under version control
with Git. A simple push to the production server would serve my static
pages up via Nginx, which in the end would take up far less resources
and memory than a Django-powered blog application or even Wordpress. So
with that, I decided to search for a static site generator that would
suit me. I did some research and narrowed my choices down to three
static site generators:

</p>
-   [Jekyll](https://github.com/mojombo/jekyll) (Ruby-based)
-   [Hyde](http://ringce.com/hyde) (Python-based)
-   [Growl](https://github.com/xfire/growl) (Python-based)

</p>
Jekyll is the creation of [@mojombo](http://twitter.com/#!/mojombo), in
which he refers to it as ["Blogging Like a
Hacker"](http://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker.html)
as he so eloquently put it in his article. He pretty much hit the nail
on the head; blogging becomes a bit of a hassle when you use a
complicated blogging engine like Wordpress and the likes.
[Many](https://github.com/mojombo/jekyll/wiki/sites) are using Jekyll
and seem to be very happy with it.

</p>
In the end, I decided to go with
[Growl](https://github.com/xfire/growl). I chose Growl because it was
pure Python, had support for [Jinja2](http://jinja.pocoo.org/), and was
extremely lightweight with few dependencies. I decided not to go with
Jekyll, arguably the most popular static site generator currently out
there, because I wasn't too fond of the templating language. Also, I
decided not to go with Hyde simply because I prefer Jinja2 over Django
templates, which is utilized in Hyde.

</p>
[Growl](https://github.com/xfire/growl) is written by [Rico
Schiekel](http://downgra.de/) and "shamelessly stole some really cool
ideas from Jekyll", which is absolutely awesome in my opinion. I think
it's great that software can be created from borrowing the best parts of
other pieces of software, regardless of language.

</p>
This blog is written and compiled with a slightly modified version of
[Growl](https://github.com/jonathanchu/growl). So far, I'm loving the
writing process:

</p>
-   Write the article in Emacs
-   Commit to Git repository
-   Rsync the changes to my production server
-   ...and that's it!

</p>
You can find out more about
[Growl](https://github.com/jonathanchu/growl) by reading its
documentation. Here are some of the main features of Growl:

</p>
-   Pages and posts have a YAML header
-   Pages and posts are written in Markdown
-   Layouts are written in HTML and Jinja2

</p>
The basic structure of my blog looks something like this:

</p>
![Jontourage Directory
Structure](/img/articles/jontourage_dir_structure.png)  

</p>
-   `_hooks` contains Python scripts that extend Growl
-   `_layout` contains the basic layouts for your site
-   `_libs` contains any third party libraries you want to use
-   `_posts` contains all the posts
-   `css` and `img` contain all the stylesheets and site media,
    respectively

</p>
All files that end with an underscore, such as `index.html_` for
example, get processed by Growl as a page. All processed pages and media
assets get dumped in the `deploy` directory, which serves up your static
site.

</p>
Posts need to be named in the following structure:

</p>
    2011-01-18-new-blog-platform.md2

</p>
When the posts are processed by Growl, the date `2011-01-18` gets parsed
and the directory structure is created -
http://jontourage.com**/2011/01/18/new-blog-platform/**

</p>
As for the post content itself, it simply is a mix of YAML and Markdown.
Here's an example of what a post header looks like:

</p>
    ---layout: posttitle: New Blog Platformpublish: false---

</p>
And the rest of the post is just Markdown! When I'm done writing the
article, I simply push to GitHub and sync up the production server using
a rsync hook:

</p>
    $ growl.py --deploy jontourage

</p>
And that's it! You can checkout my blog and the structure in more detail
[here](https://github.com/jonathanchu/jontourage).

</p>
<p>

</div>

</p>
<div class="post-date">

</p>
<span>-- Jan 18, 2011</span>

<p>

</div>

</p>
<p>

</div>

</p>
<p>
</section>
</p>

