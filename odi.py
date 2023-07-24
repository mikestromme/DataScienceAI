from zipfile import ZipFile
import os

# Path of the zip file
zip_path = "data/O2Ring_20230724.zip"
unzip_folder = "data/unzipped"

# Create a folder to unzip the files into
os.makedirs(unzip_folder, exist_ok=True)

# Unzip the file
with ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(unzip_folder)

# List the files in the unzipped folder
unzipped_files = os.listdir(unzip_folder)
unzipped_files


import pandas as pd

# Load the first CSV file as a sample
sample_file_path = os.path.join(unzip_folder, unzipped_files[0])
sample_data = pd.read_csv(sample_file_path)

# Display the first few rows of the sample data
sample_data.head()

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
