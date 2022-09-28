import os

import markdown

converted = 0
total_files = 0

mds = os.listdir('md')
total_files = len(mds)
print(mds)

for md in mds:
    markdown.markdownFromFile(input='md/' + md, output='src/views/' + md[:-3] + '.html', encoding='utf-8')
    converted += 1
    print('Converted ' + md + ' to html' + ' (' + str(converted) + '/' + str(total_files) + ')')



