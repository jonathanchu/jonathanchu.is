+++
title = "Emacs Lisp Basics"
author = ["Jonathan Chu"]
date = 2026-02-11T00:00:00-05:00
draft = false
+++

Must-know Emacs Lisp functions to practice and internalize. These are the building blocks for writing your own commands, customizing Emacs, and reading other people's configs.


## Variables &amp; Scope {#variables-and-scope}


### `setq` {#setq}

Set the value of a variable.

```emacs-lisp
(setq my-name "Jonathan")
(setq x 1 y 2 z 3) ;; set multiple at once
(message "x: %d" x) ;; format %d for number
(message "y: %s" y) ;; format %s for any character
(message "%d" z)
```


### `let` / `let*` {#let-let}

Bind local variables. `let*` allows later bindings to reference earlier ones.

```emacs-lisp
;; all bindings are evaluated in parallel
;; x and y do not know about each other
(let ((x 10)
      (y 20))
  (+ x y)) ;; => 30

;; bindings are evaluated sequentially
(let* ((x 10)
       (y (* x 2)))  ;; without let*, this would be an error
  y) ;; => 20
```


### `defvar` / `defcustom` {#defvar-defcustom}

Define a variable. `defvar` won't overwrite an existing value and is intended for internal state. `defcustom` creates a user-customizable variable -- something they can configure later.

```emacs-lisp
(defvar my-default-directory "~/projects"
  "Default directory for projects.")

(defcustom my-line-spacing 0.1
  "Line spacing for my setup."
  :type 'float
  :group 'my-config)
```


## Functions {#functions}


### `defun` {#defun}

Define a named function.

```emacs-lisp
(defun greet (name)
  "Greet someone by NAME."
  (message "Hello, %s!" name))

(greet "world") ;; => "Hello, world!"

(defun poke (thing)
  "Poke a THING."
  (message "Poke, %s!" thing))

(poke "bear") ;; => "Poke, bear!"
```


### `lambda` {#lambda}

Create an anonymous function.

```emacs-lisp
(mapcar (lambda (x) (* x x)) '(1 2 3 4)) ;; => (1 4 9 16)
```


### `interactive` {#interactive}

Make a function callable via `M-x`.

```emacs-lisp
(defun insert-current-date ()
  "Insert today's date at point."
  (interactive)
  (insert (format-time-string "%Y-%m-%d")))
```


### `funcall` / `apply` {#funcall-apply}

Call a function stored in a variable. `apply` spreads a list as arguments.

```emacs-lisp
(funcall #'+ 1 2 3) ;; => 6
(apply #'+ '(1 2 3)) ;; => 6
```


## Lists &amp; Cons Cells {#lists-and-cons-cells}


### `car` / `cdr` / `cons` {#car-cdr-cons}

`car` returns the first element, `cdr` returns the rest, `cons` constructs a new cons cell.

```emacs-lisp
(car '(a b c))   ;; => a
(cdr '(a b c))   ;; => (b c)
(cons 'a '(b c)) ;; => (a b c)
```


### `list` / `append` {#list-append}

`list` creates a new list. `append` concatenates lists.

```emacs-lisp
(list 1 2 3)           ;; => (1 2 3)
(append '(1 2) '(3 4)) ;; => (1 2 3 4)
```


### `nth` / `length` {#nth-length}

`nth` returns the element at index n (0-based). `length` returns the list length.

```emacs-lisp
(nth 0 '(a b c))    ;; => a
(nth 2 '(a b c))    ;; => c
(length '(a b c))   ;; => 3
```


### `push` / `pop` {#push-pop}

`push` adds to the front of a list (mutates). `pop` removes and returns the first element.

```emacs-lisp
(setq my-list '(b c))
(push 'a my-list) ;; my-list is now (a b c)
(pop my-list)     ;; => a, my-list is now (b c)
```


### `assoc` / `alist-get` {#assoc-alist-get}

Look up a key in an association list.

```emacs-lisp
(setq my-alist '((name . "Jonathan") (editor . "Emacs")))
(assoc 'name my-alist)      ;; => (name . "Jonathan")
(alist-get 'name my-alist)  ;; => "Jonathan"
```


## Predicates {#predicates}


### Type checking {#type-checking}

```emacs-lisp
(numberp 42)      ;; => t
(stringp "hello") ;; => t
(listp '(1 2))    ;; => t
(symbolp 'foo)    ;; => t
(functionp #'+)   ;; => t
(null nil)        ;; => t
(null '())        ;; => t
```


### Equality {#equality}

```emacs-lisp
(eq 'foo 'foo)          ;; => t  (same object / symbol)
(equal '(1 2) '(1 2))   ;; => t  (structural equality)
(string= "abc" "abc")   ;; => t  (string comparison)
(= 1 1.0)               ;; => t  (numeric equality)
```


## Control Flow {#control-flow}


### `if` / `when` / `unless` {#if-when-unless}

```emacs-lisp
(if (> 3 2)
    "yes"    ;; then
  "no")      ;; else

(when (> 3 2)
  (message "this runs") ;; implicit progn, no else branch
  "yes")

(unless (> 2 3)
  (message "2 is not greater than 3")
  "correct")
```


### `cond` {#cond}

Multi-branch conditional.

```emacs-lisp
(defun describe-number (n)
  (cond
   ((< n 0) "negative")
   ((= n 0) "zero")
   ((< n 10) "small")
   (t "big")))

(describe-number 3)
```


### `progn` {#progn}

Evaluate multiple forms, return the last one.

```emacs-lisp
(progn
  (setq x 1)
  (setq y 2)
  (+ x y)) ;; => 3
```


## Iteration {#iteration}


### `dolist` / `dotimes` {#dolist-dotimes}

```emacs-lisp
(dolist (item '("a" "b" "c"))
  (message "Item: %s" item))

(dotimes (i 5)
  (message "Count: %d" i)) ;; 0 through 4

(dotimes 2)
```


### `mapcar` / `mapc` {#mapcar-mapc}

`mapcar` applies a function to each element and collects results. `mapc` does the same but for side effects (returns the original list).

```emacs-lisp
(mapcar #'upcase '("hello" "world")) ;; => ("HELLO" "WORLD")
(mapcar #'1+ '(1 2 3))               ;; => (2 3 4)

(mapc #'upcase '("Hello" "World"))
```


### `seq-filter` / `seq-reduce` {#seq-filter-seq-reduce}

```emacs-lisp
(seq-filter #'cl-evenp '(1 2 3 4 5 6)) ;; => (2 4 6)
(seq-reduce #'+ '(1 2 3 4) 0)          ;; => 10
```


## Strings {#strings}


### `concat` / `format` {#concat-format}

```emacs-lisp
(concat "Hello" ", " "world!") ;; => "Hello, world!"
(format "Name: %s, Age: %d" "Jonathan" 30) ;; => "Name: Jonathan, Age: 30"
```


### `substring` / `split-string` / `string-join` {#substring-split-string-string-join}

```emacs-lisp
(substring "Hello, world!" 0 5)  ;; => "Hello"
(split-string "a:b:c" ":")       ;; => ("a" "b" "c")
(string-join '("a" "b" "c") "-") ;; => "a-b-c"
```


### `string-match` / `replace-regexp-in-string` {#string-match-replace-regexp-in-string}

```emacs-lisp
(string-match "o+" "foobar") ;; => 1 (index of match)
(replace-regexp-in-string "[0-9]+" "N" "foo123bar456") ;; => "fooNbarN"
```


### `string-prefix-p` / `string-suffix-p` / `string-trim` {#string-prefix-p-string-suffix-p-string-trim}

```emacs-lisp
(string-prefix-p "foo" "foobar")  ;; => t
(string-suffix-p ".el" "init.el") ;; => t
(string-trim "  hello  ")         ;; => "hello"
```


## Buffer Operations {#buffer-operations}


### `point` / `goto-char` {#point-goto-char}

`point` returns cursor position. `goto-char` moves to a position.

```emacs-lisp
(point)                 ;; => current cursor position (integer)
(point-min)             ;; => 1 (beginning of buffer)
(point-max)             ;; => end of buffer
(goto-char (point-min)) ;; move to beginning
```


### `insert` / `delete-region` / `buffer-substring` {#insert-delete-region-buffer-substring}

```emacs-lisp
(insert "some text")
(delete-region (point-min) (point-max)) ;; delete everything
(buffer-substring (point-min) (point-max)) ;; get buffer contents as string
```


### `save-excursion` {#save-excursion}

Run body, then restore point and current buffer.

```emacs-lisp
(save-excursion
  (goto-char (point-min))
  (insert "Header\n")) ;; point returns to where it was
```


### `with-current-buffer` {#with-current-buffer}

Execute body in the context of another buffer.

```emacs-lisp
(with-current-buffer "*Messages*"
  (buffer-string)) ;; returns content of *Messages* buffer
```


## Hooks &amp; Advice {#hooks-and-advice}


### `add-hook` / `remove-hook` {#add-hook-remove-hook}

Attach functions to run at specific events.

```emacs-lisp
(add-hook 'emacs-lisp-mode-hook #'eldoc-mode)
(add-hook 'before-save-hook #'delete-trailing-whitespace)
(remove-hook 'before-save-hook #'delete-trailing-whitespace)
```


### `advice-add` / `advice-remove` {#advice-add-advice-remove}

Modify existing function behavior without changing the original.

```emacs-lisp
(defun my-before-save-message (&rest _)
  (message "About to save!"))

(advice-add 'save-buffer :before #'my-before-save-message)
(advice-remove 'save-buffer #'my-before-save-message)
```


## Common Patterns {#common-patterns}


### Reading user input {#reading-user-input}

```emacs-lisp
(read-string "Enter your name: ")
(completing-read "Choose: " '("option-a" "option-b" "option-c"))
(y-or-n-p "Continue? ")
```


### `message` {#message}

Print to the `*Messages*` buffer (the elisp equivalent of `print` / `console.log`).

```emacs-lisp
(message "Hello!")
(message "Value is: %s" some-var)
(message "Number: %d, String: %s, S-expr: %S" 42 "foo" '(1 2 3))
```
