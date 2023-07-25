import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()
varName = os.getenv("varName")



# Load the data
labor_df = pd.read_csv('/Users/mikes/Desktop/files/labor.csv')

# Display the first few rows of the data
labor_df.head()

# Drop the 'Work Order' column
labor_df = labor_df.drop(columns=['Work Order'])

# Display the first few rows of the updated data
labor_df.head()

# Group the data by 'Task' and sum the 'Hours', then sort in descending order
task_hours = labor_df.groupby('Task')['Hours'].sum().sort_values(ascending=False)

# Get the task with the most hours spent
most_hours_task = task_hours.idxmax()
most_hours = task_hours.max()

most_hours_task, most_hours

# Filter the data for the specific task '02000400 Branch Wire & Conduit'
task_specific_df = labor_df[labor_df['Task'] == '02000400 Branch Wire & Conduit'].copy()

# Convert the 'Date' column to datetime
task_specific_df['Date'] = pd.to_datetime(task_specific_df['Date'])



# Calculate the total number of unique dates (days) the task was performed
total_days = task_specific_df['Date'].nunique()

# Calculate the total hours spent on the task
total_hours = task_specific_df['Hours'].sum()

# Calculate the average hours per day spent on the task
average_hours_per_day = total_hours / total_days

average_hours_per_day

# Adjust the total hours considering only 8 hours of work per day
total_hours_adjusted = total_days * 8

# Calculate the average hours per day spent on the task after adjustment
average_hours_per_day_adjusted = total_hours / total_hours_adjusted

print(f"The average hours per day spent on the task '02000400 Branch Wire & Conduit' after adjustment is {average_hours_per_day_adjusted} hours.")
