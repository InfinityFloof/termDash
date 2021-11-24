#!/usr/bin/env python3

import curses
import sys
import os
import datetime

# Modules of termDash
import termDashCFG as config

VersionInfo="termDash git-0.1"

def draw(screen):
    k = 0
    cursor_x = 0
    cursor_y = 0


    screen.clear()
    screen.refresh()

    # Colours
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)


    while (k != ord('q')):
        screen.clear()
        height, width = screen.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1

        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1

        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1

        elif k == ord('s'):
            screen.clear()
            curses.endwin()
            os.system("clear")
            if (config.Skip_ShellReturnText == False):
                print()
                print("To return to termDash, type 'exit' or press CTRL + D")
            os.system("$SHELL -c 'cd ~; $SHELL'")

        elif k == ord('e'):
            screen.clear()
            curses.endwin()
            os.system(f"{config.TerminalEditor}")

        elif k == ord('o'):
            screen.clear()
            curses.endwin()
            os.system(f"$SHELL -c '{config.TerminalEditor} termDashCFG.py'")

        elif k == ord('x'):
            screen.clear()
            curses.endwin()
            print(f"Running command: sudo {config.PackageManager} {config.UpdateSyntax}")
            os.system(f"sudo {config.PackageManager} {config.UpdateSyntax}; sleep 5")

        elif k == ord('i'):
            screen.clear()
            curses.endwin()
            print(f"What package would you like to install?")
            Package = input("$ ")

            os.system(f"sudo {config.PackageManager} {config.InstallSyntax} {Package}; sleep 5")

        elif k == ord('r'):
            screen.clear()
            curses.endwin()
            print(f"What package would you like to remove?")
            Package = input("$ ")

            os.system(f"sudo {config.PackageManager} {config.RemoveSyntax} {Package}; sleep 5")

        elif k == ord('t'):
            screen.clear()
            curses.endwin()
            print(f"Running command: sudo {config.PackageManager} {config.UpgradeSyntax}")

            os.system(f"sudo {config.PackageManager} {config.UpgradeSyntax}; sleep 5")

        elif k == ord('z'):
            screen.clear()
            curses.endwin()
            print(f"What would you like to search for?")
            Package = input("$ ")

            os.system(f"{config.PackageManager} {config.SearchSyntax} {Package}; sleep 5")

        cursor_x = max(0, cursor_x)
        cursor_x = min(width - 1, cursor_x)
        
        cursor_y = max(0, cursor_y)
        cursor_y = min(height - 1, cursor_y)

        title = f"{config.SplashText}"[:width-1]
        sbartext = f"{VersionInfo} | Press 'q' to Exit | {config.StatusBar_CustomText}"

        menuOpt1 = "[S] Run the Shell"
        menuOpt2 = "[U] Update termDash"
        menuOpt3 = "[E] Terminal Editor"
        menuOpt4 = "[O] termDash Options"
        menuOpt5 = "[?] Terminal Help"
        quitCMD  = "[Q] Exit termDash"

        pkgManTitle = ">>> Package Management <<<"
        pkgManOpt1 = "[X] Update Package Cache"
        pkgManOpt2 = "[I] Install a Package"
        pkgManOpt3 = "[R] Remove a Package"
        pkgManOpt4 = "[T] Upgrade Packages"
        pkgManOpt5 = "[Z] Search for a Package"

        screen.attron(curses.A_BOLD)
        screen.attron(curses.color_pair(1))
        screen.addstr(1, 1, title)

        screen.attron(curses.color_pair(3))

        screen.addstr(height - 1, 0, sbartext)
        screen.addstr(height - 1, len(sbartext), " " * (width - len(sbartext) - 1))

        screen.attroff(curses.color_pair(3))
        screen.attroff(curses.A_ITALIC)

        screen.addstr(4, 1, menuOpt1)
        screen.addstr(4, 25, menuOpt2)
        screen.addstr(5, 1, menuOpt3)
        screen.addstr(5, 25, menuOpt4)
        screen.addstr(6, 1, menuOpt5)
        screen.addstr(6, 25, quitCMD)

        screen.attron(curses.color_pair(1))
        screen.attron(curses.A_ITALIC)

        screen.addstr(9, 1, pkgManTitle)

        screen.attroff(curses.color_pair(1))
        screen.attroff(curses.A_ITALIC)

        screen.addstr(11, 1, pkgManOpt1)
        screen.addstr(11, 28, pkgManOpt2)
        screen.addstr(12, 1, pkgManOpt3)
        screen.addstr(12, 28, pkgManOpt4)
        screen.addstr(13, 1, pkgManOpt5)
        

        screen.move(cursor_y, cursor_x)
        screen.refresh()

        k = screen.getch()

def main():
    curses.wrapper(draw)

if __name__ == "__main__":
    main()
