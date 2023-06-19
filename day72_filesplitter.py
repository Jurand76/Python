import glob
import os
import shutil

current_dir = os.getcwd()
split_dir = current_dir + r"\files_to_split"
print("Source directory  : ",split_dir)

os.chdir(split_dir)

file_pattern = "*.*"
files = glob.glob(file_pattern)

fileext_array = []

for file in files:                                              # check unique extensions
    filename,fileext = os.path.splitext(file)
    if fileext in fileext_array:
        print("Extension ", fileext," exists")
    else:
        print("Extension new: ",fileext)
        fileext_array.append(fileext)

for extension in fileext_array:                                 # make new directories if not exists
    new_directory = split_dir + "\\" + extension.replace(".","")
    print("New directory: ", new_directory)
    if os.path.exists(new_directory):
        print("Directory ", new_directory, " already exists")
    else:
        os.mkdir(new_directory)

for file in files:                                              # copies new files to directories
    filename,fileext = os.path.splitext(file)
    source = split_dir + "\\" + file
    destination = split_dir + "\\" + fileext.replace(".","") + "\\" + file
    
    print("Old filename: ", source) 
    print("New filename: ", destination) 

    if os.path.exists(destination):
        print("File already copied")
    else:
        shutil.copy(source,destination) 

   