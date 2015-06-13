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

Next, we'll need to install Java, as Clojure runs on the Java Virtual
Machine (JVM). You'll need to install the Java Development Kit (JDK).

(Java from Oracle)[http://www.oracle.com/technetwork/java/index.html]

You can go to the Java website to download it and install manually,
but I prefer to let package managers do that for me.

For this, we can install the JDK through Homebrew Cask:

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

[Leiningen](http://leiningen.org/) is a user interface to the Clojure library that helps you
automate projects and manage dependencies, while setting up `lein` and
Clojure for you.

```console
brew install leiningen
```

5) Make sure exec path setup in emacs (ex. `/usr/local/bin`)
6) package-install cider, 4clojure
7) profiles.clj
8) What to do for message about "WARNING: CIDER requires nREPL 0.2.7 to work properly"
