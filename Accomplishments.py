#!/usr/bin/env python
# coding: utf-8

# 1. Import process tasks to dataframe
# 2. Summarize status by type/date
# 3. Summarize weight by type/date
# 4. Calculate Dones and ToDos
# 4. Export summary file for Excel import

# Import Dependencies
import pandas as pd
import csv
import os

# Read raw tasks file and convert to dataframe
wt_tasks_csv = os.path.join("data","tasks.csv")
wt_tasks_df = pd.read_csv(wt_tasks_csv)

# Create summary dataframe for Status and Weight type(date)
sum_tasks_df = pd.DataFrame(wt_tasks_df.groupby(['Type'])['Status','Weight'].sum())

# Add Count column
sum_tasks_df['Count'] = wt_tasks_df.groupby(['Type'])['Status'].count()
#wt_tasks_df.groupby(['Type'])['Status'].count()

# Add number of ToDo tasks
sum_tasks_df['ToDo'] = wt_tasks_df.groupby(['Type'])['Status'].count()-wt_tasks_df.groupby(['Type'])['Status'].sum()

# Renaming Status as Done
sum_tasks_df.rename(columns={'Status': 'Done'}, inplace=True)

# Change to order of columns
# Currently: ['Done', 'Weight', 'Count', 'ToDo']
# We want ['Done', 'ToDo', 'Weight', 'Count']
st_cols = ['Done', 'ToDo', 'Weight', 'Count']
# Change column order
sum_tasks_df=sum_tasks_df[st_cols]

# Exporting summary dataframe to summary file
tasks_sum_csv = os.path.join('data', 'tasks_sum.csv')
sum_tasks_df.to_csv(tasks_sum_csv)
