#!/usr/bin/env python
# coding: utf-8

# Pre-Process Today.txt to Identify Overlong Entries

# Import libraries
import pandas as pd
import os

# Identify file path
todayfile = "/Users/victor/Downloads/Today.txt"

# Check to see of file exists
try:
    # Using pipe as separator because it is not likely to be used in the outline
    todayfile_df = pd.read_csv(todayfile, sep = "|")
except FileNotFoundError:
    print('+----------------------------------------------------+')
    print('| *** The Today.txt file has not been generated! *** |')
    print('+----------------------------------------------------+')
    exit()

# This works but doesn't stop being prompted in Excel - maybe chown and sudo?
os.chmod ("/Users/victor/Downloads/Today.txt", 0o777)

# Loop through the exported Today.txt file to find any entries that are too long
# Initialize row counter to help retrieve bad row
rownum = 0
# Loop through file using index
for line in todayfile_df.index: 
    # Pulling out current field entry
    currline = todayfile_df['Outline: Today'][line]
    # Stripping leading spaces
    currline = currline.lstrip()
    # Checking for correct start of line 
    if currline[0:1] != '-':
        # Showing incorrect extra line
        print(currline)
        # Getting too long line number
        badrow = rownum - 1
        # Displaying too long line
        print(todayfile_df.iloc[[badrow]])
    # incrementing row number
    rownum = rownum + 1

# Testing if there were any bad rows to display final status message
try:
    badrow
except NameError:
    print('+-------------------------------------------------------+')
    print('| The Today.txt file is good and ready to be processed. |')
    print('+-------------------------------------------------------+')
else:
    print('+----------------------------------------------------------------------------+')
    print('| *** The above item(s) are too long to export and need to be addressed! *** |')
    print('+----------------------------------------------------------------------------+')


