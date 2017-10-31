#
# menu_debug.py
# A program to print a restaurant menu
# This version of the program provides only the initial elements
# and directs the output to the Python shell
# Tested with Python 3.3.0 on Windows 7
# 
# Fri Apr 5, 2013
# Copyright 2009-2015 National Academy Foundation. All rights reserved.
#

###################################################################
# BLOCK 1 FOR DEBUGGING
# This section should only be included while you are debugging to the Python shell
# import the system module
from sys import *
# temporarily set the menu print file to the Python shell
menu_file = stdout
###################################################################

###################################################################
# MAIN PART OF THE PROGRAM BEGINS

#
# Define and print the menu text graphic
#

#
# Programming tip: When you are drawing graphics with characters, make
# sure you do not end a line with a '\' character.
# Instead, add an extra space after the '\' character.
# Otherwise Python will interpret the '\' as a
# line continuation character and ruin your graphic when it is printed.
#

# define the menu text graphic
# use triple quotes for multi-line text graphics
menu_text_graphic="""
     __  ___  _____  ___   __   _    ___
    /  |/   | | ___| |  \  | | | |  |   |
   / /|  /| | | |__  |   \ | | | |  |   |
  / / |_/ | | |  __| | |\ \| | | |  |   |
 / /      | | | |__  | | \   | |  \_|   |
/_/       |_| |____| |_|  \_ |  \____/|_|
"""

# print the menu text graphic
# send the output to a file (indicated by >>)
print(menu_text_graphic, file=menu_file)

#
# Define and print the face text graphic
#

# define the face text graphic
face_text_graphic="""
  _____
/      \ 
| *  * |
|  O   |
\ \__/ /
 \____/            
"""

# print the face text graphic
print(face_text_graphic, file=menu_file)

#
# Print information about the restaurant
#

# print the restaurant name in uppercase
print("Joe's Cafe".upper(), file=menu_file)
# print a blank line
print(file=menu_file)
# print additional information about the restaurant
# *** To be added ***

#
# Print the menu items and prices
#

# *** To be added ***

# MAIN PART OF THE PROGRAM ENDS
###################################################################

###################################################################
# BLOCK 2 FOR DEBUGGING
# When you are finished debugging, replace this section of your menu.py file
###################################################################

