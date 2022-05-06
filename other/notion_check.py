#!/usr/bin/env python
# https://developers.notion.com/reference/post-search

import json
import requests # pip3 install requests
import os
import dotenv # pip3 install python-dotenv

dotenv.load_dotenv()
token = os.getenv('token')

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

# print(json.dumps(response_info, indent=4))

for item in response_info['results']:
    the_title = item["properties"]["title"]["title"][0]["plain_text"]
    the_url = item['url']

    if (the_title == 'documentation'):
        print('good')
    else:
        pass

    print(the_title, the_url)

