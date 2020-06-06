# __script_4_you__
This project contains scripts that automate some of the most boring yet time consuming and essential tasks. 


Folder Manager:

CLI tool that allows user to arrange and compress directories  

Requirements:

Python 3.x

Usage:

1. Arrange by extension:

-e or --ext

python "path"\folder_manager.py -e "absolute path of directory to be arranged"

2. Arrange by name:

-n or --name

python "path"\folder_manager.py -n  "absolute path of directory to be arranged"

3. Deep arrange:

-d or --deep

"path"\folder_manager.py -d "mode" "absolute path of directory to be arranged"
    
    mode 1. arrange by name-> arrange by ext
    mode 2. arrange by ext-> arrange by name

4. Compress

-c or --compress

"path"\folder_manager.py -c "type of archive" "absolute path of directory to be arranged"

Supported archives:
    1. "xztar"  Slowest but maximum compression is achieved. Supported by default in linux only
    2. "gztar"
    3. "zip"    Fastest and supported in windows, linux and mac. Lowest level of compression is achieved

example:python folder_manager.py -c zip E:\Desktop\python_programming\beginner_projects\dummyFolder       

This would create an archived file of the specified directory in its parent folder. You may now choose to delete the original directory 

Note : 
1. all the operations work for valid directory paths, not Files 
2. Currently only absolute path of directory is supported 