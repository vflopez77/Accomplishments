#!/usr/bin/env python
# coding: utf-8

# 1. Check Today.txt file for existence
# 2. Check Today.txt file for overlong entries
# 3. Import processed tasks to dataframe
# 4. Summarize status by type/date
# 5. Summarize weight by type/date
# 6. Calculate Dones and ToDos
# 7. Export summary file for Excel import

# Import Dependencies
import pandas as pd
import csv
import os
from datetime import datetime

# Pre-Process Today.txt to Identify Overlong Entries

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
    # Exit program if file does not exist
    exit()

# This works but doesn't stop being prompted in Excel - maybe chown and sudo?
os.chmod ("/Users/victor/Downloads/Today.txt", 0o777)

# Loop through the exported Today.txt file to find any entries that are too long
# Initialize row counter to help retrieve bad row
rownum = 0
badrowcount = 0
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
        # Incrementing the bad row count
        badrowcount += 1
        # Displaying too long line
        print(todayfile_df.iloc[[badrow]])
    # incrementing row number
    rownum = rownum + 1

# Testing if there were any bad rows to display final status message
try:
    badrow
except NameError:
    # Only report a bad file and do nothing programmatically
    pass
else:
    if badrowcount > 1:
        print('+--------------------------------------------------------------------------+')
        print('| *** The above items are too long to export and need to be addressed! *** |')
        print('+--------------------------------------------------------------------------+')
    else:
        print('+-------------------------------------------------------------------------+')
        print('| *** The above item is too long to export and needs to be addressed! *** |')
        print('+-------------------------------------------------------------------------+')
    # Delete bad Today*.txt file(s) 
    os.system('bash NixToday.sh')
    # Exit program if bad lines are found
    exit()

# Read raw tasks file and convert to dataframe
wt_tasks_csv = os.path.join("data","tasks.csv")
wt_tasks_df = pd.read_csv(wt_tasks_csv)

# Create summary dataframe for Status and Weight type(date)
sum_tasks_df = pd.DataFrame(wt_tasks_df.groupby(['Type','Status'])[['ToDoW','DoneW']].sum())

# Group by date to take into account dates with Todo and Done records
sum_tasks_final_df = pd.DataFrame(sum_tasks_df.groupby(['Type'])[['ToDoW','DoneW']].sum())

# Export final summary dataframe to summary file
tasks_sum_csv = os.path.join('data', 'tasks_sum.csv')
sum_tasks_final_df.to_csv(tasks_sum_csv)

# Write Flag File with Today's Date
flag_file_txt = open(os.path.join("data", "script_completed.txt"), "w")
flag_file_txt.write(datetime.today().strftime('%Y-%m-%d'))
flag_file_txt.close()

# Open file permissions for Excel
# Check if this is necessary
os.chmod ("/Users/victor/Downloads/Today.txt", 0o777)
os.chmod("data/script_completed.txt", 0o777)
# Files are cleaned up by Excel

# Completion Notificaton
print('+-----------------------------------------------------------------------+')
print('| The Summary Data has been processed and is ready for update in Excel. |')
print('+-----------------------------------------------------------------------+')
