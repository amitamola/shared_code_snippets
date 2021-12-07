# Code to copy files from one folder to other:
import os
from shutil import copy2
from glob import glob

path = 'folder/subfolder1'
copy_path = 'folder/subfolderYouWantToCopyTo'

# In case file type doesn't matter and you want to copy the content of one folder to other:
for file in glob(path+'/*'):
    copy2(file, copy_path)

'''
# If you want to perform this for certain type of files like jpg in a folder, you only need to add file extention to glob command, for example:
for file in glob(path+'/*jpg'):
    copy2(file, copy_path)
'''
