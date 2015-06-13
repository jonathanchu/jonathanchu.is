Title: Getting Started with Emacs and Clojure on OS X
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

<!-- PELICAN_END_SUMMARY -->

1) Install Homebrew - [http://brew.sh/](http://brew.sh/)

I won't go into too much detail here, aside from providing the
[link](http://brew.sh/) where you can find all the resources on
installing this. I highly recommend using Homebrew for your packaging
needs on OS X. The one liner to install looks like this:

```console
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

We'll be using Homebrew to install some of the necessary programs and
libraries.

2) Install Homebrew Cask

Next, we'll need to install Java, as Clojure runs on the Java Virtual
Machine (JVM). You'll need to install the Java Development Kit (JDK).

[Java from Oracle](http://www.oracle.com/technetwork/java/index.html)

You can go to the Java website above to download it and install
manually, but I prefer to let package managers do that for me. It is
recommended to download at least version 6 of the JDK.

For this, we can install the JDK through Homebrew Cask, which we will
need to install:

```console
brew install caskroom/cask/brew-cask
```

3) Install Java

Now that we have Homebrew Cask installed, we can install the JDK by
simply doing:

```console
brew cask install java
```

This will pull the latest version of the JDK according to Homebrew
Casks and install it on your machine.

4) Install Leiningen

[Leiningen](http://leiningen.org/) is a user interface to the Clojure
library that helps you automate projects and manage dependencies,
while setting up `lein` and Clojure for you.

```console
brew install leiningen
```

5) Configure Emacs

This is mostly an optional step if you already haven't done this. Make
sure you have something like this in your Emacs config:

```elisp
(add-to-list 'exec-path "/usr/local/bin")
```

If your Homebrew install is standard, this is where your binaries
should be located. If not, adjust the path as necessary.

6) Install Emacs packages `cider`

<kbd>m-x</kbd> `package-install` <kbd>RET</kbd> `cider`

Optionally, if you want to do [4clojure](https://www.4clojure.com/)
problems in Emacs, also install `4clojure.el`:

<kbd>m-x</kbd> `package-install` <kbd>RET</kdd> `4clojure`

7) Add a `profiles.clj`

In your home directory, create a new `profiles.clj` in `~/.lein/` and put this barebones config to start with:

```clojure
{:user {:plugins [[cider/cider-nrepl "0.9.0-SNAPSHOT"]]
        :dependencies [[org.clojure/tools.nrepl "0.2.10"]]}}
```

*Note - modify the `cider-nrepl` and `tools.nrepl` versions if you
 have issues. It should match what you installed above.

And there you have it! You should be able to fire up Emacs and start a
Clojure REPL through `cider` and even answer a few
[4clojure](https://www.4clojure.com/) questions.
