+++
title = "Paredit Basics"
author = ["Jonathan Chu"]
date = 2019-08-15T00:00:00-04:00
draft = false
+++

The `|` character is where our cursor is for purposes of visualizing where to invoke these methods.


## `paredit-wrap-round` {#paredit-wrap-round}

Let's wrap the `2` here.

```emacs-lisp
(+ 1 |2 3 4)
;; Keybinding M-(
(+ 1 (2) 3 4)
```


## `paredit-forward-slurp-sexp` {#paredit-forward-slurp-sexp}

And after we wrap the `2`, we type `*` and want to slurp in the `3`.

```emacs-lisp
(+ 1 (* |2) 3 4)
;; Keybinding C-)
(+ 1 (* 2 3) 4)
```


## `paredit-forward-barf-sexp` {#paredit-forward-barf-sexp}

Oops, we slurped in the `4` by accident!  Let's unslurp it by barfing it out.

```emacs-lisp
(+ 1 (* 2 3 |4))
;; Keybinding C-}
(+ 1 (* 2 3) 4)
```
