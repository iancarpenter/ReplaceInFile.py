# Ian Carpenter 19/01/2017
# Loop through the specified directory for files
# of interest.
# For each file found, replace target string with
# replace_with
import os

directory = ''
target = ''
replace_with = ''
file_type = '.txt'

for filename in os.listdir(directory):
    
    if filename.endswith(file_type):

        path_and_name = os.path.join(directory, filename)

        # read in the file
        filedata = None
        with open(path_and_name, 'r') as file:
            filedata = file.read()

        # replace the target string
        filedata = filedata.replace(target, replace_with)

        # write the file out
        with open(path_and_name, 'w') as file:
            file.write(filedata)
    else:
        continue
