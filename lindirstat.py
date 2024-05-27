# Imports here
import os

# Function to get file name and size
def get_file_info(file_path):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    # Print function info
    print(file_name, "is", file_size, "bytes")

# Debug function with input
print("What file:")
file_input = input()
initial_file_path = file_input
file_path = initial_file_path

# Function to act according to file/directory/none
def check_file(file_path):
    # Start by flagging if the file doesn't exist
    if os.path.exists(file_path) == False:
        print("file does not exist")

    # Then check if it's a directory
    if os.path.isdir(file_path):
        dir_contents = os.listdir(file_path)
        get_file_info(file_path)
        # if directory path does not end with /, add that
        if file_path[-1] != "/":
            file_path = file_path + "/"
        # Check each file in directory
        for file in dir_contents:
            current_path = file_path + file
            check_file(current_path)

    # Finally check if it's a file
    if os.path.isfile(file_path):
        # What to do if target is file
        get_file_info(file_path)

check_file(file_path)
