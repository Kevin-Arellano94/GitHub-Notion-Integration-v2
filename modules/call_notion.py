import os
import dotenv
import requests
import json

dotenv.load_dotenv()
token = os.getenv('token')

counter = 0

url = "https://api.notion.com/v1/search"

payload = {"page_size": 100}

headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json",
    "Authorization": f"Bearer { token }"
}

response = requests.post(
    url,
    json = payload,
    headers = headers
).text

response_info = json.loads(response)

def get_folders():
    notion_folders = []
    
    for items in response_info['results']:
        the_title = items["properties"]["title"]["title"][0]["plain_text"]
        the_url = items['url']

        notion_folders.append(
            (
                the_title,
                the_url
            )
        )
    
    return notion_folders