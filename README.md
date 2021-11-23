<a id="org76b86a4"></a>

# termDash

termDash is a handy little program, written in the Python 3 language, and is a small little dashboard for your terminal.


# Table of Contents

1.  [termDash](#org76b86a4)
    1.  [Intended Use](#orga754ff5)
    2.  [Configuration](#org4038baf)
    3.  [Compiling to C](#orgeadcb1e)


<a id="orga754ff5"></a>

## Intended Use

termDash is intended to be used when you start the terminal, and would typically be placed in your `.shellrc` file, like so

```bash
    ...................
    export PS1="[\u@\h \W]$ "
    alias vim="emacsclient -c -a 'emacs'" # Just some bantering
    alias nano="vim" # Because Vim > Nano

    python3 ~/termDash.py
```

termDash was also designed to be both a piece of eyecandy, and a piece of software to ease new users into the command line, as there aren&rsquo;t that many tools that are new-user friendly and command line based.


<a id="org4038baf"></a>

## Configuration

Configuration of termDash is done in a simple Python file, name `termDashCFG.py`. This file is also commented so that people aren&rsquo;t just guessing what it does. Currently, it&rsquo;s nothing that special, but does have some options, such as package managment settings - which are set to Debian/Ubuntu defaults.


<a id="orgeadcb1e"></a>

## Compiling to C

This is an optional step, but is included here. If you so choose to, you can compile termDash into a C Program via the help of `cython`. Simply install Cython via Pip, as well as the GNU C Compiler (gcc), and simply run the `make` command.
