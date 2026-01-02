#Problem 4 without comment
import os

def print_directory_contents(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing the directory '{path}'.")
#Select the directory whose content you want to list
directory_path = '/YouTube'

print_directory_contents(directory_path)
