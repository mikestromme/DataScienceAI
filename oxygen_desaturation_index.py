from zipfile import ZipFile
import os
import pandas as pd
import numpy as np
from datetime import datetime

# Path of the zip file
zip_path = "data/O2Ring.zip"
unzip_folder = "data/unzipped"

# Create a folder to unzip the files into
os.makedirs(unzip_folder, exist_ok=True)

# Unzip the file - does not duplicate files
with ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(unzip_folder)

# List the files in the unzipped folder
unzipped_files = os.listdir(unzip_folder)
unzipped_files


# Load the first CSV file as a sample
sample_file_path = os.path.join(unzip_folder, unzipped_files[0])
sample_data = pd.read_csv(sample_file_path)

# Display the first few rows of the sample data
print(sample_data.head())


# Initialize an empty DataFrame
all_data = pd.DataFrame()

# Load all the data from all the CSV files
for file in unzipped_files:
    file_path = os.path.join(unzip_folder, file)
    data = pd.read_csv(file_path)
    
    # Add the data from this file to all_data
    all_data = pd.concat([all_data, data])

# Display the size of all_data and the first few rows
print(f"Size of all data: {all_data.shape}")
all_data.head()


# Remove data with an Oxygen Level of 255
filtered_data = all_data[all_data['Oxygen Level'] != 255]

# Display the size of filtered_data and the first few rows
print(f"Size of filtered data: {filtered_data.shape}")
filtered_data.head()


# Calculate the baseline oxygen level
baseline_oxygen_level = filtered_data['Oxygen Level'].median()

# Identify the dips in oxygen level that are greater than 4% from the baseline
dips = (filtered_data['Oxygen Level'] < baseline_oxygen_level - 4)

# Display the baseline oxygen level and the first few values of dips
baseline_oxygen_level, dips.head()


# Calculate the baseline oxygen level
baseline_oxygen_level = filtered_data['Oxygen Level'].median()

# Identify the dips in oxygen level that are greater than 4% from the baseline
dips = (filtered_data['Oxygen Level'] < baseline_oxygen_level - 4)

# Display the baseline oxygen level and the first few values of dips
baseline_oxygen_level, dips.head()


# Count the number of dips
num_dips = np.sum((dips.diff() == 1) & dips)

# Calculate the total duration of sleep in hours
# First, convert the 'Time' column to datetime
filtered_data = all_data[all_data['Oxygen Level'] != 255].copy()
filtered_data['Time'] = pd.to_datetime(filtered_data['Time'], format='%H:%M:%S %b %d %Y')

# Then calculate the duration from the first to the last timestamp
total_duration_hours = (filtered_data['Time'].max() - filtered_data['Time'].min()).total_seconds() / 3600

# Calculate the Oxygen Desaturation Index (ODI)
ODI = num_dips / total_duration_hours

# Display the number of dips, total duration in hours, and the ODI
num_dips, total_duration_hours, ODI

print('\n')
print(f'Number of Dips less than 4% of baseline: {str(num_dips)}')
print(f'Total Duration in Hours:  {total_duration_hours}')
print(f'Oxygen Saturation Index: {ODI}')


# Delete all files in the unzipped folder
for filename in os.listdir(unzip_folder):
    file_path = os.path.join(unzip_folder, filename)
    # Make sure the file is not a directory
    if os.path.isfile(file_path):
        os.remove(file_path)


