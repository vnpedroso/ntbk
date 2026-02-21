# ntbk
> : _a book of plain paper or paper with lines, for writing on_

yeap, a notebook, but in your terminal.
no dbs involved, just txt files.

---

## installation


The project was created using [uv](https://docs.astral.sh/uv/). Easiest way to to install it, which requires no code changes, is by having `uv` installed and runnin the following:

```shell
uv tool install . 
```

After installation, you can run `ntbk` to check if installation was successful. Expected output:

```shell
Usage: ntbk [OPTIONS] COMMAND [ARGS]...

  Your terminal based personal notebook application

Options:
  --help  Show this message and exit.

Commands:
  erase    deletes a note by ID
  new      ntbk new page: creates a new page ntbk new note: creates a new...
  read     read all notes in the specified page, uses bookmark if no page...
  rip      rips a page from the notebook
  summary  shows all pages, highlights the bookmarked page
```

To uninstall it, you can run

```shell
uv tool uninstall ntbk
```

---

## concepts

### the bookmark

The bookmark is the most important concept of the tool. And it has a simple definition:  ***The bookmark is the latest page to be modified***. 

Except by the `summary` command, all the other commands have the power to change the bookmark.

The intention for this design choice is to reduce the typing from the user. For instance, consider the following examples:

```shell
ntbk new note
```
* creates a new note under the current bookmark page 

```shell
ntbk new note --page <page_name>
```
* creates a new note under the page inputed after the `--page` option, ***and moves the bookmark to it***.

---

## commands

A detailed guide of the tool's commands

### summary
*todo*

### new 
*todo*

### read
*todo*

### erase
*todo*

### rip
*todo*

### edit
*todo*
---

## next steps

* create the `edit` commands
* finish this README
* add tests
