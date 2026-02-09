+++
title = "Introducing magit-gh"
author = ["Jonathan Chu"]
description = """
  "Introducing magit-gh, a lightweight Emacs package that brings GitHub CLI pull request commands into Magit"
  """
date = 2026-02-08T00:00:00-05:00
tags = ["emacs", "magit", "github"]
draft = false
+++

After recently releasing [magit-git-toolbelt](https://github.com/jonathanchu/magit-git-toolbelt), a Transient interface for [git-toolbelt](https://github.com/nvie/git-toolbelt) in [magit](https://github.com/magit/magit), I'm happy to share another Magit extension I've been working on -- [magit-gh](https://github.com/jonathanchu/magit-gh), an Emacs package that integrates the [GitHub CLI](https://cli.github.com) (`gh`) into [Magit](https://magit.vc/). Similar to my former package, it provides a Transient menu interface to list, checkout, and view pull requests directly from Emacs without leaving your workflow.


## Why I wrote this {#why-i-wrote-this}

If you work with pull requests on GitHub every day, you know the git checkout dance: you're deep in flow and in a Magit buffer, you need to check on a PR, so you switch to a browser, find the repo, navigate to the PR tab, and then maybe come back to checkout the branch in eshell or even your terminal. It's a small context switch, but it adds up.

[Forge](https://github.com/magit/forge) has been the defacto and established solution for this and it's a fantastic and comprehensive package for interacting with Git forges from within Magit -- it has all the bells and whistles for this workflow. If you need deep integration -- tracking issues, managing pull requests, reading and writing comments, all stored locally in a light database -- Forge is the right tool. **I would highly recommend Forge over this package if that is your use case**.

`magit-gh` takes a different approach. It delegates to the [GitHub CLI](https://cli.github.com) (`gh`) for all GitHub interaction, which means:

-   **No local database** -- Forge maintains a local SQLite database via `emacsql`, which can be tricky to set up (compiling native modules, resolving binary availability issues). `magit-gh` stores nothing locally.
-   **No token management** -- Forge requires a GitHub personal access token stored in your `authinfo` file (ideally encrypted with GPG). `magit-gh` piggybacks on `gh auth login`, which you have already configured from authenticating the first time.
-   **Minimal dependencies** -- just Magit, Transient, and the `gh` CLI.

The trade-off is that `magit-gh` is far less featureful than Forge. It is intentionally a lightweight alternative for users who primarily want to list, checkout, and view pull requests without additional setup overhead.


## Installation {#installation}

You'll need the [GitHub CLI](https://cli.github.com) installed and authenticated first:

```sh
# macOS
brew install gh

# Linux (Fedora / RHEL / CentOS)
sudo dnf install gh

# Then authenticate
gh auth login
```

Then install `magit-gh` from MELPA:

`M-x package-install RET magit-gh RET`

Or with `use-package`:

```emacs-lisp
(use-package magit-gh
  :ensure t
  :after magit)
```


## Usage {#usage}

From any Magit status buffer, press `,` to bring up the `magit-gh` Transient menu. You can also invoke it directly with `M-x magit-gh`. The menu is organized into Pull Request commands:

```text
magit-gh
└── Pull Requests
    ├── l  List open PRs
    ├── c  Checkout PR
    └── v  View PR in browser
```

When you list open PRs (`l`), a dedicated buffer opens showing PR number, title, author, and branch name. From that buffer you can checkout a PR with `RET` or `c`, open it in your browser with `v`, refresh the list with `g`, or close the buffer with `q`.

{{< figure src="https://raw.githubusercontent.com/jonathanchu/magit-gh/refs/heads/main/screenshots/20260203_magit_gh_demo.gif" >}}

If you don't like the `,` key binding, you can set a custom one. Note that the variable must be set **before** the package loads so it needs to be in the init section:

```emacs-lisp
(use-package magit-gh
  :ensure t
  :after magit
  :init
  (setq magit-gh-key ";")) ; Example setting key to ";" instead of the default ","
```

To increase the number of PRs fetched (default 30):

```emacs-lisp
(use-package magit-gh
  :ensure t
  :after magit
  :custom
  (magit-gh-pr-limit 50))
```


## What's next {#what-s-next}

Aside from bugs and visual improvements to the TUI, I would consider this package mostly feature complete. The current feature set is intentionally small, but I have plans to add support for listing closed/merged PRs, creating new PRs, viewing diffs and CI status, and eventually issue management -- all through the `gh` CLI. You can track progress on the [GitHub repo](https://github.com/jonathanchu/magit-gh).

If you use Magit and the GitHub CLI, give `magit-gh` a try! It's available on [MELPA](https://melpa.org/#/magit-gh) and the source is on [GitHub](https://github.com/jonathanchu/magit-gh). Contributions and feedback are always welcome! Hope this is useful!
