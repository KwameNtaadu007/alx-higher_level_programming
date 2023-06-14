#!/usr/bin/python3

"""
Contains the "append after" function
"""

def append_after(filename="", search_string="", new_string=""):
    # Read the contents of the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Iterate over the lines and insert the new string after matching lines
    for i, line in enumerate(lines):
        if search_string in line:
            lines.insert(i + 1, new_string + '\n')

    # Write the modified contents back to the file
    with open(filename, 'w') as file:
        file.writelines(lines)

