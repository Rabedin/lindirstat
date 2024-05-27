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

# Directory function
def check_file(file_path):
    # Start by checking if the file exists
    if os.path.exists(file_path):
        print("file exists")
    else:
        print("file does not exist")
    # Then check if it's a directory
    if os.path.isdir(file_path):
        # What to do if target is Directory
        dir_contents = os.listdir(file_path)
        print(file_path, "is a directory")
        # print(dir_contents)
        for file in dir_contents:
            current_path = file_path + file # TODO Need to test if concat'd path is correct
            check_file(current_path)
            print(indent, file) # TODO Need to init indent
    # Finally check if it's a file
    if os.path.isfile(file_path):
        # What to do if target is file
        get_file_info(file_path)
        print(file_path, "is a file")

check_file(file_path)
