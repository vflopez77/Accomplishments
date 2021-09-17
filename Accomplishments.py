#!/usr/bin/env python
# coding: utf-8

# 1. Import processed tasks to dataframe
# 2. Summarize status by type/date
# 3. Summarize weight by type/date
# 4. Calculate Dones and ToDos
# 4. Export summary file for Excel import

# Import Dependencies
import pandas as pd
import csv
import os
from datetime import datetime

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
