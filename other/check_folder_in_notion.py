from modules.grab_notion_api import notion_page_title, notion_page_url
# from modules.grab_github_repo_tree import slash_count, raw_url

# from config_notion import json, requests, token

def checking(x, y):
    number_of_slashes = 6

    y = y.replace('https://raw.githubusercontent.com/Kevin-Arellano94/', '')

    if (x == number_of_slashes):
        new_y = y.replace('', '').split('/')[0]
        print(new_y)
        is_in_notion(new_y, notion_page_url)
    
    if (x == (number_of_slashes + 1)):
        new_y = y.replace('documentation/main/', '').split('/')[0]
        print(new_y)
        is_in_notion(new_y, notion_page_url)
    
    if (x == (number_of_slashes + 2)):
        new_y = y.replace('documentation/main/', '').split('/')[1]
        print(new_y)
        is_in_notion(new_y, notion_page_url)
    
    if (x == (number_of_slashes + 3)):
        new_y = y.replace('documentation/main/', '').split('/')[2]
        print(new_y)
        is_in_notion(new_y, notion_page_url)

def is_in_notion(y, x):
    counter = 0
    for z in x:
        if y in z:
            value = 'header'
            update(value, z)
            counter += 1

    if (counter == 0):
        creator = 'value'
        create(x)

def update(x, y):
    print(f'update.py')
    print(x)
    print(y)
    print()

def create(x):
    print(f'create.py')
    print(x)
    print()