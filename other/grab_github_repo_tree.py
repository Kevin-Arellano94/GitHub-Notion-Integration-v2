from modules import check_folder_in_notion

from config import PROD, glob

domain  = r'https://raw.githubusercontent.com'
user    = r'/Kevin-Arellano94'
repo    = r'/documentation'
branch  = r'/main'

if (PROD):
    path = r"D:/a/documentation-action/documentation-action"
if (not PROD):
    path = r"C:/Users/kevin/Documents/GitHub/eHawk-Inc/documentation"

files = glob.glob(
    path +
    '*/**/*.md',
    recursive = True
)

for items in files:
    new_items = items.replace('\\', '/')

    raw_url = new_items.replace(
        f'{ path }',
        domain +
        user +
        repo +
        branch
    )
    slash_count = raw_url.count('/')

    print(raw_url)
    check_folder_in_notion.checking(slash_count, raw_url)