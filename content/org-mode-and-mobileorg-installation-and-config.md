Title: Org-Mode and MobileOrg Installation and Config
Date: 2013-07-10 00:00
Slug: org-mode-and-mobileorg-installation-and-config

<section>
</p>
<span>Org-Mode and MobileOrg Installation and Config</span>
===========================================================

</p>
<div class="row">

</p>
<div class="span12 post">

</p>
![MobileOrg](/img/articles/mobileorg_placeit.png)  

</p>
Intro
-----

</p>
Throughout the years, I've flipped back and forth between Org-Mode and
applications such as [Drafts (iOS)](http://agiletortoise.com/drafts/),
[Evernote](https://evernote.com/), [Simplenote](http://simplenote.com/),
and even plain ol' [text
files](http://lifehacker.com/166299/geek-to-live--list-your-life-in-txt)
(with the [Notational Velocity](http://notational.net/) and
[nValt](http://brettterpstra.com/projects/nvalt/)) for my most basic
note-taking needs; however, I've always found myself coming back to
Org-Mode in the end for another spin around the block. The one positive
thing that kept me coming back to Org-Mode, and perhaps the same thing
that Emacs is often criticized for, is the fact that it has a lot of
functionality under the hood - almost *too* much. Org-Mode is a very
feature-rich application. For my basic needs, I use Org-Mode primiarly
for three things:

</p>
-   Basic note-taking and outlines
-   TODO lists
-   Tracking and clocking time

</p>
Here Comes MobileOrg
--------------------

</p>
When I first learned about [MobileOrg](http://mobileorg.ncogni.to/), I
was really stoked that I would be able to record notes, update TODO
statuses, and even just view my org files on the go. Unfortunatley, I
found that the basic setup instructions on their website left a few
minor things out for someone new to MobileOrg, and this is my attempt to
supplement that to help others with the same issues I faced with setup.

</p>
Org-Mode Configuration
----------------------

</p>
First off, it should be noted that I'm using Emacs 24 with Org-Mode
already baked in. If you're using an earlier version of Emacs that
doesn't have Org-Mode by default, please install it according to your
own preference (which we won't get into here since there are a few
different ways to install Org-Mode).

</p>
My root directory for all of my org files is kept in Dropbox in a
directory called `org`:

</p>
    ~/Dropbox/org

</p>
I've found that this setup fits my workflow best since I also work off a
second laptop at times and would like all my org files to be synced
across all machines with as little effort as possible.

</p>
MobileOrg Setup
---------------

</p>
Next, install MobileOrg from the [App
Store](https://itunes.apple.com/us/app/mobileorg/id634225528?mt=8). I
chose the path of least resistance and decided to use Dropbox as the
source for server config, so when you first open the application, click
on the Dropbox option, click to link account, and allow authentication
with Dropbox to proceed. It should have created a new directory for you
under:

</p>
    ~/Dropbox/Apps/MobileOrg

</p>
Emacs Configuration for MobileOrg
---------------------------------

</p>
You will need a few more lines of code to get this all working with your
local org files and MobileOrg. This is my basic config based on the two
main directories above that will need to go in your Emacs config:

</p>
    ;; mobileorg settings(setq org-directory "~/Dropbox/org")(setq org-mobile-inbox-for-pull "~/Dropbox/org/inbox.org")(setq org-mobile-directory "~/Dropbox/Apps/MobileOrg")(setq org-mobile-files '("~/Dropbox/org"))

</p>
Finally, from within Emacs - edit any org file located in
`~/Dropbox/org/` and save those changes. Then send these changes to
MobileOrg to sync up:

</p>
    M-x org-mobile-push

</p>
With any luck, you should be able to go back to MobileOrg on your mobile
device and click the refresh button to see your org file(s) all there.

</p>
Happy hacking!

</p>
<p>

</div>

</p>
<div class="post-date">

</p>
<span>-- Jul 10, 2013</span>

<p>

</div>

</p>
<p>

</div>

</p>
<p>
</section>
</p>

