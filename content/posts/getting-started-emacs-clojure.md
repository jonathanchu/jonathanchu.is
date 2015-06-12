Date: 2015-06-12 00:00
Slug: getting-started-emacs-clojure-mac-osx
Category: Emacs
Tags: emacs, clojure


I've been learning Clojure in my spare time and coming from a
predominantly Python-focused career, I wanted to chronicle my
experiences with learning Clojure and integrating it witin my Emacs
config.

This article will be geared towards beginners, like me, looking to get
started with Clojure and Emacs on OS X.

1) Install Homebrew - [http://brew.sh/](http://brew.sh/)

I won't go into too much detail here, aside from providing the link
where you can find all the resources on installing this. I highly
recommend using Homebrew for your packaging needs on OS X. The one
liner to install looks like this:

```console
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2) Install Homebrew Cask


3) brew cask install java
4) brew install leiningen
5) Make sure exec path setup in emacs (ex. `/usr/local/bin`)
6) package-install cider, 4clojure
7) profiles.clj
8) What to do for message about "WARNING: CIDER requires nREPL 0.2.7 to work properly"
