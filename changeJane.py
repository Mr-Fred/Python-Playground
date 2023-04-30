#!/usr/bin/env python3

import sys
import subprocess

# Read the list of file names from the text file
with open(sys.argv[1]) as file:
    lines = file.readlines()
    file_names = [line.strip() for line in lines]
    #print(file_names)

# Create a list of new file names by replacing 'jane' with 'jdoe'
new_names = [name.replace('jane', 'jdoe') for name in file_names]
#print(new_names)

# Rename each file with its corresponding new name using subprocess.run()
for old_name, new_name in zip(file_names, new_names):
    if "jane_" in old_name:
        subprocess.run(["mv", old_name, new_name])
