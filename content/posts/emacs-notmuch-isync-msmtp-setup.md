+++
title = "Emacs, Notmuch, isync, and msmtp Setup"
author = ["Jonathan Chu"]
description = "\"How to setup notmuch, isync, and msmtp with Emacs.“"
date = 2020-06-23T00:00:00-04:00
tags = ["emacs"]
draft = false
+++

I've been meaning to move my email management to Emacs for the past year and finally made the jump after see [Mike Zamansky's](https://cestlaz.github.io/stories/emacs/) video on this ([YouTube](https://www.youtube.com/watch?v=GlrsoIwJ-UM)). Here are my notes on how I got this all setup and configured.

This is an opinionated setup based on Mac OS X and Fastmail. First, make sure you have [Homebrew](https://brew.sh/) installed to install the packages needed.


## Receiving email {#receiving-email}

[Notmuch](https://notmuchmail.org/) requires email to be stored on your local filesystem and one message per file. We'll be using `isync` for this.

```shell
$ brew install isync
```

<http://isync.sourceforge.net/>

You'll need to start out with an initial config which you can copy directly to your home directory.

My `.mbsyncrc` file looks like this:

```nil
# First section: remote IMAP account
IMAPAccount fastmail
Host imap.fastmail.com
Port 993
User jonathanchu@fastmail.com
# For simplicity, this is how to read the password from another file.
# For better security you should use GPG https://gnupg.org/
PassCmd "cat ~/.mbsync-fastmail"
SSLType IMAPS
SSLVersions TLSv1.2

IMAPStore fastmail-remote
Account fastmail

# This section describes the local storage
MaildirStore fastmail-local
Path ~/Maildir/
Inbox ~/Maildir/INBOX
SubFolders Verbatim

# This section a "channel", a connection between remote and local
Channel fastmail
Master :fastmail-remote:
Slave :fastmail-local:
Patterns *
Expunge None
CopyArrivalDate yes
Sync All
Create Slave
SyncState *
```

The contents of `.mbsync-fastmail` contains my email password, which is probably not the best way to do store a password like this locally so I should fix this in the near future.

Once this is configured and saved in your home directory, you can then run run `mbsync` to pull your email down locally:

```shell
$ mbsync -a
```

Note, you'll have to run this each time to retrieve new mail. I know some folks might elect to have this as a running cron job every x minutes - this can be entirely based on your preference and email workflow.


## Viewing and writing email {#viewing-and-writing-email}

We're going to use `Notmuch`, specifically in Emacs, to view our mail. First, you need to install `Notmuch` on your OS:

```shell
$ brew install notmuch
```

Then, in your Emacs configuration, you can install `notmuch-emacs` by including the following:

```elisp
(use-package notmuch
  :ensure t
  :defer t)
```

TODO Run notmuch setup and/or copy over `.notmuch-config` as an example.

Then, you can run `m-x notmuch-hello` and you will be greeted with the `notmuch` starting screen.

<a id="org3502202"></a>

{{< figure src="/images/notmuch-hello.png" caption="Figure 1: m-x notmuch-hello" >}}

<a id="orgd823806"></a>

{{< figure src="/images/notmuch-unread.png" caption="Figure 2: notmuch unread" >}}


## Sending email {#sending-email}

Next, we'll need to send our mail with something, so I chose `msmtp` because of how easy it was to configure.

```shell
$ brew install msmtp
```

The contents of my `.msmtprc` file looks like this:

```nil
defaults
auth on
protocol smtp
tls on

account fastmail
host smtp.fastmail.com
port 465
user jonathanchu@fastmail.com
passwordeval "cat ~/.mbsync-fastmail"
tls_starttls off
from jonathanchu@fastmail.com

account default : fastmail
```

This article will be updated as I refine my email process and work out the bugs, but at this point you should have working email with Notmuch in Emacs!
