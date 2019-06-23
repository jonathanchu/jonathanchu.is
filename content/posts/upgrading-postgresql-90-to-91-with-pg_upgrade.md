+++
date = 2012-06-19T00:00:00-04:00
title = "Upgrading PostgreSQL 9.0 to 9.1 with pg_upgrade"
description = ""
slug = "upgrading-postgresql-90-to-91-with-pg_upgrade"
tags = ["postgresql"]
categories = ["databases"]
externalLink = ""
series = []
+++

Recently, I updated all of the packages I have installed via
[Homebrew](https://github.com/mxcl/homebrew) and ran into some issues
with the PostgreSQL package. I was getting this error:

    The data directory was initialized by PostgreSQL version 9.0, which is not compatible with this version 9.1.4

A quick search took me to this
[page](http://www.postgresql.org/docs/9.1/static/pgupgrade.html),
however the docs left a lot to be desired to say the least. Here's a
step-by-step to how I eventually fixed it using pg\_upgrade.

First, change directories to your Postgres data directory.

    $ cd /usr/local/var

Next, create a new directory for the new data directory.

    $ mkdir postgres9

Use `initdb` to initialize the new Postgres cluster in the new data
directory you created above.

    $ initdb /usr/local/var/postgres9

Run `pg_upgrade` with the following arguments:

    $ pg_upgrade -d /usr/local/var/postgres/ -D /usr/local/var/postgres9 -b /usr/local/Cellar/postgresql/9.0.4/bin/ -B /usr/local/Cellar/postgresql/9.1.4/bin/ -v

If all goes without error, you can switch the data directories so
Postgres will point to the right source.

    $ mv postgres postgres9.0.1
    $ mv postgres9 postgres

You can delete the script left behind by `pg_upgrade`:

    $ rm delete_old_cluster.sh

I actually had my old Postgres instance running, so I had to stop it
before restarting the new one:

    $ pg_ctl -D /usr/local/var/postgres9.0.1 stop -m fast

Then I restarted the new Postgres instance:

    $ launchctl unload -w homebrew.mxcl.postgresql.plist
    $ launchctl load -w homebrew.mxcl.postgresql.plist

And you're done - this should fix the PostgreSQL incompatible data
directory issue.
