Title: Upgrading PostgreSQL 9.0 to 9.1 with pg_upgrade
Date: 2012-06-19 00:00
Slug: upgrading-postgresql-90-to-91-with-pg_upgrade

<section>
</p>
<span>Upgrading PostgreSQL 9.0 to 9.1 with pg\_upgrade</span>
=============================================================

</p>
<div class="row">

</p>
<div class="span12 post">

</p>
Recently, I updated all of the packages I have installed via
[Homebrew](https://github.com/mxcl/homebrew) and ran into some issues
with the PostgreSQL package. I was getting this error:

</p>
    The data directory was initialized by PostgreSQL version 9.0, which is not compatible with this version 9.1.4

</p>
A quick search took me to this
[page](http://www.postgresql.org/docs/9.1/static/pgupgrade.html),
however the docs left a lot to be desired to say the least. Here's a
step-by-step to how I eventually fixed it using pg\_upgrade.

</p>
First, change directories to your Postgres data directory.

</p>
    $ cd /usr/local/var

</p>
Next, create a new directory for the new data directory.

</p>
    $ mkdir postgres9

</p>
Use `initdb` to initialize the new Postgres cluster in the new data
directory you created above.

</p>
    $ initdb /usr/local/var/postgres9

</p>
Run `pg_upgrade` with the following arguments:

</p>
    $ pg_upgrade -d /usr/local/var/postgres/ -D /usr/local/var/postgres9 -b /usr/local/Cellar/postgresql/9.0.4/bin/ -B /usr/local/Cellar/postgresql/9.1.4/bin/ -v

</p>
If all goes without error, you can switch the data directories so
Postgres will point to the right source.

</p>
    $ mv postgres postgres9.0.1$ mv postgres9 postgres

</p>
You can delete the script left behind by `pg_upgrade`:

</p>
    $ rm delete_old_cluster.sh

</p>
I actually had my old Postgres instance running, so I had to stop it
before restarting the new one:

</p>
    $ pg_ctl -D /usr/local/var/postgres9.0.1 stop -m fast

</p>
Then I restarted the new Postgres instance:

</p>
    $ launchctl unload -w homebrew.mxcl.postgresql.plist$ launchctl load -w homebrew.mxcl.postgresql.plist

</p>
And you're done - this should fix the PostgreSQL incompatible data
directory issue.

</p>
<p>

</div>

</p>
<div class="post-date">

</p>
<span>-- Jun 19, 2012</span>

<p>

</div>

</p>
<p>

</div>

</p>
<p>
</section>
</p>

