import glob
for f in glob.glob('C:/Users/kevin/Documents/GitHub/eHawk-Inc/documentation/**/*.md', recursive=True):
    f = f.replace('C:/Users/kevin/Documents/GitHub/eHawk-Inc/', '')
    # print(f)

    f_slash = f.count('\\')

    if (f_slash == 1):
        hexo_2_arg = 'https://www.notion.so/ehawk/Engineering-8982234254df4a99bca13654a714ba89'
        # print(hexo_2_arg, f_slash, f)
    
    if (f_slash == 2):
        hexo_2_arg = 'https://www.notion.so/ehawk/documentation-fe02c36771de49bba38fd437c8d42491'
        # print(hexo_2_arg, f_slash, f)

        if r'documentation\adr' in f:
            print(hexo_2_arg, f_slash, f)
    
    # print(f_slash, f)

'd0adf9d574d1ac180fb677ccfe701bb50f78926e5552b6be532b70cded234fba05d35898e2d13ec14c4db2bb2d007755d19ef1e7f84fad2251e67d350852c1424b5dc4ec328f0b3ec2e6207f2c43'
'https://www.notion.so/ehawk/Engineering-8982234254df4a99bca13654a714ba89'
'https://raw.githubusercontent.com/Kevin-Arellano94/documentation/main/readme.md'