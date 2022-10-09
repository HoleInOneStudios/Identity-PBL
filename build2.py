import os

import markdown
from markdown.extensions.tables import * 


class tColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

courses = []
students = []
teachers = []
description = ""

html_out = ""

def Reset_Build():
    files = os.listdir('src/build/views')
    for file in files:
        os.remove('src/build/views/' + file)

def convert_markdown_to_html():
    global description

    # "Description" MD to HTML
    description += markdown.markdown(open('md/description.md', 'r').read(), extensions=[TableExtension()])
    print(tColors.BOLD + tColors.BLUE + "\n========== Description =========\n" + tColors.NORMAL + description)

    # "Courses" MD to HTML
    for c in os.listdir('md/courses'):
        if c.endswith('.md'):
            tempC = "<div>"
            tempC += markdown.markdown(open('md/courses/' + c, 'r').read())
            tempC += "</div>"
            courses.append(tempC)
    print(tColors.BOLD + tColors.BLUE + "\n========= Courses and Example Coursework ==========\n" + tColors.NORMAL + str(courses))

    # "Students" MD to HTML
    for s in os.listdir('md/students'):
        if s.endswith('.md'):
            tempS = "<div>"
            tempS += markdown.markdown(open('md/students/' + s, 'r').read())
            tempS += "</div>"
            students.append(tempS)
    print(tColors.BOLD + tColors.BLUE + "\n========= Students ==========\n" + tColors.NORMAL + str(students))

    # "Teachers" MD to HTML
    for t in os.listdir('md/teachers'):
        if t.endswith('.md'):
            tempT = "<div>"
            tempT += markdown.markdown(open('md/teachers/' + t, 'r').read())
            tempT += "</div>"
            teachers.append(tempT)
    print(tColors.BOLD + tColors.BLUE + "\n========= Teachers ==========\n" + tColors.NORMAL + str(teachers))

def build_html():
    global html_out
    
    # == Description ==
    html_out += "<section id=\"description\">\n"
    html_out += "<h1>Description</h1>\n<div>\n"
    html_out += description + "\n</div>\n</section>\n"

    # == Courses ==
    html_out += "<section id=\"courses\">\n"
    html_out += "<h1>Courses</h1>\n<div>\n"
    for c in courses:
        html_out += c + "\n"
    html_out += "</div>\n</section>\n"

    # == Students ==
    html_out += "<section id=\"students\">\n"
    html_out += "<h1>Students</h1>\n<div>\n"
    for s in students:
        html_out += s + "\n"
    html_out += "</div>\n</section>\n"
    
    # == Teachers ==
    html_out += "<section id=\"teachers\">\n"
    html_out += "<h1>Teachers</h1>\n<div>\n"
    for t in teachers:
        html_out += t + "\n"
    html_out += "</div>\n</section>\n"

    print(tColors.BOLD + tColors.BLUE + "\n========= Raw HTML ==========\n" + tColors.NORMAL + html_out)

def write_html_to_file():
    with open('src/build/index.html', 'r') as f:
        index = f.read()
        
        index = index.replace("<!--main-->", html_out)

        open('src/index.html', 'w').write(index)

if __name__ == '__main__':
    os.system('cls')
    Reset_Build()
    convert_markdown_to_html()
    build_html()
    write_html_to_file()
