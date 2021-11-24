#!/usr/bin/env python3

# This is the configuration file for termDash, and is also
# in Python, as it's very easy to look at and understand


import datetime
import os

# Text for the Status Bar
# default : datetime.datetime.now().strftime("%A %d %B %Y")
#    Output: Tuesday 23 November 2021

StatusBar_CustomText=datetime.datetime.now().strftime("%A %d %B %Y")

# Splash Text for The Top of termDash
SplashText="termDash from Kimitzuni"

# Settings Related to Package Management
PackageManager="apt"
InstallSyntax="install"
UpdateSyntax="update"
UpgradeSyntax="upgrade"
SearchSyntax="search"
RemoveSyntax="remove"

# Terminal Editor
# default : nano
TerminalEditor="nano"

Skip_ShellReturnText = False
