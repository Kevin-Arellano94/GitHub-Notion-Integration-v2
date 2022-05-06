import glob

path    = r"C:/Users/kevin/Documents/GitHub/eHawk-Inc/documentation"
domain  = r'https://raw.githubusercontent.com'
user    = r'/Kevin-Arellano94'
repo    = r'/documentation'
branch  = r'/main'

folders = glob.glob(
    path +
    '*/**/',
    recursive = True
)

files = glob.glob(
    path +
    '*/**/*',
    recursive = True
)

def get_folders():
    github_folders = []

    for items in folders:
        new_items = fix_slashes(items)
        raw_url = get_full_url(new_items)
        slash_count = count_slashes(raw_url)

        github_folders.append(
            (
                slash_count,
                raw_url
            )
        )
    return github_folders

def fix_slashes(items):
    new_items = items.replace('\\', '/')
    return new_items

def get_full_url(new_items):
    raw_url = new_items.replace(f'{ path }', domain + user + repo + branch)
    return raw_url

def count_slashes(raw_url):
    slash_count = raw_url.count('/')
    return slash_count

# def get_files():
#     for items in files:
#         new_items = items.replace('\\', '/')

#         raw_url = new_items.replace(
#             f'{ path }',
#             domain +
#             user +
#             repo +
#             branch
#         )

#         slash_count = raw_url.count('/')
#         print(slash_count, raw_url)

#     return