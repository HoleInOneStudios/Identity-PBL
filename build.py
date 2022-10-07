import os

import markdown


class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def Convert_To_Markdown():
    converted = 0
    total_files = 0
    
    mds = os.listdir('md')
    total_files = len(mds)
    
    for md in mds:
        markdown.markdownFromFile(input='md/' + md, output='src/build/views/' + md[:-3] + '.html', encoding='utf-8')
        converted += 1
        # == Progress Indication ==
        print('Converted md/' + md + ' to src/build/views/' + md[:-3] + '.html (' + str(converted) + '/' + str(total_files) + ')')
    
    # == Finished Indication ==
    print('Finished converting ' + str(converted) + ' files')

def Get_HTML_Index():
    html_main = ""
    html_nav = ""

    for file in os.listdir('src/build/views'):
        if file.endswith('.html'):
            section = "<section id=\""+os.path.splitext( ( os.path.basename(file) ) )[0]+"\">\n"
            with open('src/build/views/' + file, 'r') as f:
                content = f.read()
                section += content + "\n</section>\n"

            # == Add to main ==
            html_main += section
            # == Add to nav ==
            html_nav += '<a href="#' + os.path.splitext( ( os.path.basename(file) ) )[0] + '">' + file[:-5].capitalize() + '</a>\n'

    # == Finished Main Indication ==
    print('Finished build HTML main content')
    open('src/build/main.html', 'w').write(html_main)

    # == Finished Nav Indication ==
    print('Finished build HTML nav content')
    open('src/build/nav.html', 'w').write(html_nav)

    # == Add to index ==
    with open('src/index.html', 'r') as f:
        index = f.read()

        startM = '<main>'
        endM = '</main>'
        repM = index[index.find(startM)+len(startM):index.rfind(endM)]

        startN = '<nav>'
        endN = '</nav>'
        repN = index[index.find(startN)+len(startN):index.rfind(endN)]

        index = index.replace(repN, html_nav)
        index = index.replace(repM, html_main)

        # write back into index
        open('src/index.html', 'w').write(index)

    # == Finished Indication ==
    print('Finished build index.html')

if __name__ == '__main__':
    Convert_To_Markdown()
    Get_HTML_Index()



