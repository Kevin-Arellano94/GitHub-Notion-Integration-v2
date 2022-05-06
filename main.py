from config import PROD
from modules import call_github
from modules import call_notion

import os
import dotenv

dotenv.load_dotenv()
notionParentFolder = os.getenv('notionParentFolder')
githubMainFolderName = os.getenv('githubMainFolderName')
githubParentFolderName = os.getenv('githubParentFolderName')

githubFolders = call_github.get_folders()
notionFolders = call_notion.get_folders()

lengthGitHubFolders = len(githubFolders)
lengthNotionFolders = len(notionFolders)

def main():
    steps = 1

    step_one(steps)
    steps += 1
    step_two(steps)

def step_one(steps):
    if (steps == 1):
        createParentPageInNotion(steps, githubFolders, notionFolders)

def step_two(steps):
    if (steps == 2): # TO-DO only go thorugh this step for the sub directories.  Add another step to loop through sub directories and add pages
        createSubPageInNotion(steps, githubFolders, notionFolders)

def createParentPageInNotion(steps, githubFolders, notionFolders):
    do_once = 0
    for notionFolder in notionFolders:
        notionURL = notionFolder[1]
        notionListCount = len(notionFolders)

        for githubFolder in githubFolders:
            githubURL = githubFolder[1]
            githubMainDirectoryName = githubURL.replace(f'{ githubMainFolderName }', '').split('/')[0]
            githubFolderName = githubURL.replace(f'{ githubParentFolderName }', '').split('/')[0]

            if (notionListCount == 1):

                if (steps > do_once):
                    notionParentURL = notionURL
                    githubFolderName = githubMainDirectoryName
                    notionParentPageUUID = notionParentURL.split('-')[-1]
                    createPagInNotion(notionParentPageUUID, githubFolderName)
                    do_once += 1

def createSubPageInNotion(steps, githubFolders, notionFolders):
    for githubFolder in githubFolders:
        githubDirectory = githubFolder[0]
        githubURL = githubFolder[1]
        githubMainDirectoryName = githubURL.replace(f'{ githubMainFolderName }', '').split('/')[0]
        githubFolderName = githubURL.replace(f'{ githubParentFolderName }', '').split('/')[0]

        for notionFolder in notionFolders:
            notionFolderName = notionFolder[0]
            notionURL = notionFolder[1]

            if (notionFolderName != notionParentFolder):
                    
                if(githubDirectory == 6):
                    notionParentURL = notionURL
                    print(githubDirectory, githubURL)
                    print(notionFolderName, notionURL)
                    print(notionParentURL)
                
                if(githubDirectory == 7):
                    notionParentURL = notionURL
                    if(notionURL):
                        notionParentPageUUID = notionParentURL.split('-')[-1]
                        createPagInNotion(notionParentPageUUID, githubFolderName)

def createPagInNotion(notionParentPageUUID, githubFolderName):
    import json, requests, token
    import datetime

    token = os.getenv('token')

    url = "https://api.notion.com/v1/pages"

    # date = f' [{ datetime.datetime.now() }]'
    date = ''

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": f"Bearer { token }"
    }

    payload = {
        "parent":
        {
            "page_id": f"{ notionParentPageUUID }"
        },
        "properties":
        {
            "title": [
                {
                    "text":
                    {
                        "content": f"{ githubFolderName }{ date }"
                    }
                }
            ]
        }
    }

    response = requests.post(
        url,
        json = payload,
        headers = headers
    ).text

    # response_info = json.loads(response)

    # print(json.dumps(response_info, indent=4))
    print(f'{ githubFolderName } created')

if __name__ == "__main__":
    main()
    print()