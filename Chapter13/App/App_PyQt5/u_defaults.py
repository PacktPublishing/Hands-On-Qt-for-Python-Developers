# -*- coding: utf-8 -*-         #   PYTHON 3   #
import os                                      # Imports stdlib os module.

def txt_file(state=False):                     # Writes default colors.
    colors = "rgba(0,41,59,140) rgba(0,41,59,255) rgba(1,255,217,140) rgba(1,255,217,255)"
    if os.path.exists("settings.txt") is state:
        wstyle = open("settings.txt", "w")     # If the file does not exist,
        wstyle.write(colors)                   # creates default file, writes
        wstyle.close()                         # the colors. Close object.
