PROD = False

import glob
from module import check_folder

domain  = r'https://raw.githubusercontent.com'
user    = r'/Kevin-Arellano94'
repo    = r'/documentation'
branch  = r'/main'

if (PROD): path = r"D:/a/documentation-action/documentation-action"
if (not PROD): path = r"C:/Users/kevin/Documents/GitHub/eHawk-Inc/documentation"

files = glob.glob(path + '*/**/*.md', recursive = True)

for items in files:
    new_items = items.replace('\\', '/')

    raw_url = new_items.replace(f'{ path }', domain + user + repo + branch)

    # check_folder(raw_url)
    directory = raw_url.count('/')

    # Check if all folders exist

    # print(directory, raw_url)

print(f'completed...')

exit(0)