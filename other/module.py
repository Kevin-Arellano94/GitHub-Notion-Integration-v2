def check_folder():
    # .\venv\Scripts\Activate.ps1
    # pip3 install requests
    # pip3 install python-dotenv

    import json
    import requests
    import os
    import dotenv

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
    
    for item in response_info['results']:
        the_title = item["properties"]["title"]["title"][0]["plain_text"]
        the_url = item['url']

        if (the_title == 'templates'):
            print('good')
        else:
            pass

        print(the_title, the_url)