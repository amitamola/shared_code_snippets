# Python code to remove files from a folder:
import os
from glob import glob

copy_path = 'folder/subfolder'

for f in glob(copy_path+'/*'):
    os.remove(f)
    
# In case you want to remove only certain type of files, use file extension as shown below:
for f in glob(copy_path+'/*jpg'):
    os.remove(f)
