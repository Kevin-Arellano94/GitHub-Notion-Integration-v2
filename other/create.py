from config_notion import json, requests, token
import datetime

url = "https://api.notion.com/v1/pages"

page_location = '7c13352c753c4cb79f2f5a625e8231a1'
date = f' [{ datetime.datetime.now() }]'
date = ''
folder_title = 'adr'

headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json",
    "Authorization": f"Bearer { token }"
}

payload = {
    "parent":
    {
        "page_id": f"{page_location}"
    },
    "properties":
    {
        "title": [
            {
                "text":
                {
                    "content": f"{folder_title}{date}"
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

response_info = json.loads(response)

print(json.dumps(response_info, indent=4))