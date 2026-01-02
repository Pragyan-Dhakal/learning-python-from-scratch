import os

# Function to print the contents of a directory
def print_directory_contents(path):
    try:
        # List all files and directories in the specified path
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing the directory '{path}'.")

# Specify the directory path (can be changed to any path)
directory_path = '/YouTube/Facebook'  # Current directory

# Call the function to print the directory contents
print_directory_contents(directory_path)
