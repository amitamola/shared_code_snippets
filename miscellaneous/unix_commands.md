## Download a google drive file from a link via terminal
**The best and easiest working solution**
```
git clone https://github.com/chentinghao/download_google_drive.git

cd download_google_drive/

python download_gdrive.py FILE_ID DESTINATION_PATH
```
*********************************************************
## STORAGE information Commands
**File system storage info**  
```df -h```

**Size info of each folder in the current directory**  
```du -h --max-depth=1```

**Numerically sorted human readable disk usage**  
```du -x --max-depth=1 | sort -n | awk '{ print $2 }' | xargs du -hx --max-depth=0```

*********************************************************
## COPY, REMOVE/DELELTE Commands
**Copy from one directory to other**  
```cp -rfv source_dir/*.jpg target_dir/```  
```cp -rfv tiles_out/*.jpg data/tiles_out/```  

**Remove a directory**  
```rm -rf dir_name```

**If your files have lot more files to delete and the above doesn't work, go inside the folder and then type**
```find . -maxdepth 1 -name "*.txt" -print0 | xargs -0 rm```

```find . -maxdepth 1 -name "*.jpg" -print0 | xargs -0 rm```

### Notice that we are mentioning file type with extention as .txt or .jpg

*********************************************************
## Some Miscellaneous Commands

**Number of files in a directory**  
```ls -1 | wc -l```

**making zip of a folder**  
```zip -r zip_name.zip dir```  
```Example - zip -r ECS.zip ECS```  

**unzip a zip file**  
```unzip zip_name.zip```  

**unzip inside a folder**  
```unzip /path/to/file.zip -d folder_name```
