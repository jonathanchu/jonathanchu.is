+++
title = "Dark mode toggle for iTerm and Emacs"
author = ["Jonathan Chu"]
description = "\"How to do dark and light mode toggle with iTerm and Emacs“"
date = 2020-07-12T00:00:00-04:00
tags = ["emacs"]
draft = true
+++

For most of my life, I've always preferred a dark theme when it comes to coding whether I'm in Emacs or the terminal. Lately though, the past two years specifically, I've switched to a light theme for both Emacs and iTerm. I really don't have a better rationale other than I feel like the lighter theme means it's "work" time and helps me focus, whereas a dark theme would be more suitable if I was coding at night and wanted to save some eye strain from a full day of looking at a computer screen.

With that said, I've definitely utilized Mac OS X's dark mode toggle and the one thing that has bothered me was the white glare of my Emacs and terminal when I was coding at night.  I wrote up a series of scripts inspired by Anantha Kumaran's excellent post on this exact issue called [Dark Mode Toggle](https://ananthakumaran.in/2020/05/09/dark-mode-toggle.html).

Now, I can type a single command in terminal and it would change to a dark theme in both Emacs and iTerm.

{{< figure src="/images/emacs-iterm-light-dark-toggle.gif" >}}

And here are the scripts that I wrangled together to achieve this:

Toggle to a dark Emacs theme:

Filename: emacs-dark-theme

<a id="code-snippet--emacs-dark-theme"></a>
```bash
#!/bin/sh
set -e

if pgrep Emacs > /dev/null; then
    emacsclient --eval "(load-theme 'doom-one t)" > /dev/null
fi
```

Toggle to a dark iTerm color scheme using AppleScript and iTerm's Python API:

Filename: iterm2\_dark\_theme.py

<a id="code-snippet--iterm2-dark-theme.py"></a>
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import iterm2

async def main(connection):
    # Get the color preset we'd lik
    preset = await iterm2.ColorPreset.async_get(connection, "One Dark")
    profiles = await iterm2.PartialProfile.async_query(connection)
    for partial in profiles:
        # Fetch the full profile and then set the color preset in it
        profile = await partial.async_get_full_profile()
        await profile.async_set_color_preset(preset)

iterm2.run_until_complete(main)
```

Call the iTerm Python script via AppleScript:

Filename: iterm-dark-theme

<a id="code-snippet--iterm-dark-theme"></a>
```bash
tell application "iTerm2"
    launch API script named "iterm2_dark_theme.py"
end tell
```

I combine calling these scripts with one command like so:

Filename: dark-mode

<a id="code-snippet--dark-mode"></a>
```bash
#!/bin/sh
set -e

/bin/bash /Users/jonathan/projects/dotfiles/bin/emacs-dark-theme
osascript /Users/jonathan/projects/dotfiles/bin/iterm-dark-theme
```

And now this all can be ran with just:

```shell
$ dark-mode
```

The same workflow can be done for switching back to a light theme by creating a new set of these scripts and modifying to the light theme you want!

Thank you to [Anantha Kumaran](https://ananthakumaran.in/2020/05/09/dark-mode-toggle.html) for this first post and all credit goes to him!

Happy (night) hacking!
