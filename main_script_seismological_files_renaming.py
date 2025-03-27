# Here is a Python script to rename seismological files in the following way:
# Finds files with the format: {prefix}_{YYYYMMDDHHMM}_{YYYYMMDDHHMM}_{suffix}
# Reduces the first timestamp’s minutes by 10
# Removes the second timestamp
# Works for different prefixes and suffixes 

# Author: Sushanta Ghosh
# Email: SGWIN98.research@gmail.com


import os
import re

# Set the folder path
folder_path = input("Please enter the file path: ")

# Regex pattern to match filenames
pattern = re.compile(r"^(.+?)_([0-9]{8})([0-9]{2})([0-9]{2})_([0-9]{12})_(.+)$")

# Loop through files in the folder
for filename in os.listdir(folder_path):
    match = pattern.match(filename)
    
    if match:
        prefix = match.group(1)   # Anything before the first underscore
        date1 = match.group(2)    # First date (YYYYMMDD)
        hour1 = match.group(3)    # First hour (HH)
        minute1 = match.group(4)  # First minute (MM)
        suffix = match.group(6)   # Anything after the last underscore

        # Reduce the first timestamp's minutes by 10
        new_minute1 = int(minute1) - 10
        new_minute1 = f"{new_minute1:02d}"  # Keep it two-digit format

        # Construct new filename (removing the second timestamp)
        new_filename = f"{prefix}_{date1}{hour1}{new_minute1}_{suffix}"

        # Rename the file
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

print("Renaming complete!")
