from config_notion import json, requests, token

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

notion_page_title = []
notion_page_url = []

for item in response_info['results']:
    the_title = item["properties"]["title"]["title"][0]["plain_text"]
    the_url = item['url']

    notion_page_title.append(the_title)
    notion_page_url.append(the_url)

    print(f'grab_notion_api.py', the_title, the_url)