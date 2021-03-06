# GitHub to Notion Integration
This application will do the following:
1. Grab Notion API
   1. Filter out 'title' and 'url' from API
2. Grab GitHub repo directory tree with glob module
   1. Filter out directory location via counting slashes '\'
3. Check if "FOLDER" exists in Notion
   1. if not?
      1. Create folder - create.py
      2. Grab URL of new folder
   2. if exists?
      1. Grab URL
4. Chcek if "FILE" exists
   1. if not?
      1. Create file - create.py
   2. if exists?
      1. Update file - update.py

README file will explain each process for installation and execution.

## Clone Repo

GitHub account ( create and acess )
GitHub CLI
Git SCM

## Python3

This application will read the directory it's located in.  It will need to be updated if it's moved inside it's config file.

Python3 [Installation](https://www.python.org/download/releases/3.0/)
```PS
py -m pip install pip3
py -m pip install --upgrade pip3
```
Note: Verify your Environment Variables point to the correct PATH

## Run the application

Navigate to the location of the 'main.py' file inside your terminal.

PS C:\Users\kevin
```PS
cd .\Documents\GitHub\eHawk-Inc\documentation\GitHub Notion Integration\
```

PS C:\Users\kevin\Documents\GitHub\eHawk-Inc\documentation>

Run the Python command.
```PS
py .\main.py
```

## Edit the application

Requirement: Python's Virtual Environment
```PS
py -m venv venv
```

To activate VENV
```PS
.\venv\Scripts\Activate.ps1
```

To deactivate VENV
```PS
deactivate
```

## Application Breakdown

Similar commands:
```PS
ls
```
```PS
Get-ChildItem | Select Name
```
```PS
tree
```

```
GitHub Notion Integration
│   .env
│   config.py
│   main.py
│   README.md
│
└─── modules
│   │   config.py
└─── venv
└─── __pycache__
```
[Directory Structure "how-to"](https://stackoverflow.com/questions/19699059/representing-directory-file-structure-in-markdown-syntax)#   G i t H u b - N o t i o n - I n t e g r a t i o n  
 