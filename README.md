<a id="orgc08c443"></a>

# termDash

termDash is a handy little program, written in the Python 3 language, and is a small little dashboard for your terminal, designed to be a utility to help people, as well as helping new users get used to the terminal.

# Table of Contents

1.  [termDash](#orgc08c443)
    1.  [Configuration Options](#orge286326)
        1.  [StatusBar_CustomText](#orgf367878)
        2.  [SplashText](#org13a671d)
        3.  [Package Manager Settings](#org6a37a0b)
        4.  [Skip_ShellReturnText](#org373cba2)
    2.  [License](#orgf00e278)

<a id="orge286326"></a>

## Configuration Options

Configuration of termDash can be done by opening the `termDashCFG.py` file in a graphical text editor, or a terminal text editor, such as `nano` or `vim`.


<a id="orgf367878"></a>

### StatusBar_CustomText

The variable `StatusBar_CustomText` referrs to the custom text on the status bar, the 3rd part of the status bar. By default it is set to

    StatusBar_CustomText=datetime.datetime.now().strftime("%A %d %B %Y")

And this will output the date and year, for example `Wednesday 24 November 2021`. You can change this formatting by taking a look at the valid `strftime` strings, which you can find on the [Python `strftime` Cheatsheet](https://strftime.org/).


<a id="org13a671d"></a>

### SplashText

This variable referrs to the text displayed at the top of termDash, and by default it is set to

    SplashText = "termDash from Kimitzuni"

This can be anything, you can even make it the same as the `StatusBar_CustomText` Variable, simply by doing this

    SplashText = StatusBar_CustomText


<a id="org6a37a0b"></a>

### Package Manager Settings

The next 6 variables in the config file all refer to package management, and by default, they are set to Debian/Ubuntu defaults - The apt Package Manager

    PackageManager="apt"
    InstallSyntax="install"
    UpdateSyntax="update"
    UpgradeSyntax="upgrade"
    SearchSyntax="search"
    RemoveSyntax="remove"
    
However, if you are using, say Manjaro Linux (or any other Arch Linux based distribution), you should set them to this:

    PackageManager="pacman"
    InstallSyntax="-S"
    UpdateSyntax="-Sy"
    UpgradeSyntax="-Syu"
    SearchSyntax="-Ss"
    RemoveSyntax="-Runs"


<a id="org373cba2"></a>

### Skip_ShellReturnText</sub>

This variable is a `bool`, meaning it can either be `True` or `False`. When set to `False`, and you select the *[S] Run the Shell* option, you will get a handy little piece of text telling you how to exit back to termDash

    To return to termDash, type 'exit' or press CTRL + D
    
    [rtw@tuxedo ~]$


<a id="orgf00e278"></a>

## License

termDash is licensed under the GNU General Public License, version 2.0

