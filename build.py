import os

import markdown


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

html_out = ""

def Reset_Build():
    # Remove old build
    files = os.listdir('src/build/views')
    for file in files:
        os.remove('src/build/views/' + file)
    print(tColors.BOLD + tColors.GREEN + " ✓ "+ tColors.BLUE + "Removed old build" + tColors.NORMAL)

def get_description():
    # "Description" MD to HTML
    description = markdown.markdown(open('md/description.md', 'r').read())
    print(tColors.BOLD  + tColors.GREEN + " ✓ " + tColors.BLUE + "Description" + tColors.NORMAL )

    return description

def get_courses():
    # "Courses" MD to HTML
    courses = []
    for c in os.listdir('md/courses'):
        if c.endswith('.md'):
            tempC = "<div>"
            tempC += markdown.markdown(open('md/courses/' + c, 'r').read())
            tempC += "</div>"
            courses.append(tempC)
    print(tColors.BOLD  + tColors.GREEN + " ✓ " + tColors.BLUE + "Courses and Example Coursework" + tColors.NORMAL ) #+ str(courses))

    return courses

def get_students():
    # "Students" MD to HTML
    students = []
    for s in os.listdir('md/students'):
        if s.endswith('.md'):
            tempS = "<div>"
            tempS += markdown.markdown(open('md/students/' + s, 'r').read())
            tempS += "</div>"
            students.append(tempS)
    print(tColors.BOLD  + tColors.GREEN + " ✓ " + tColors.BLUE + "Students" + tColors.NORMAL )

    return students

def get_teachers():
    # "Teachers" MD to HTML
    teachers = []
    for t in os.listdir('md/teachers'):
        if t.endswith('.md'):
            tempT = "<div>"
            tempT += markdown.markdown(open('md/teachers/' + t, 'r').read())
            tempT += "</div>"
            teachers.append(tempT)
    print(tColors.BOLD  + tColors.GREEN + " ✓ " + tColors.BLUE + "Teachers" + tColors.NORMAL )

    return teachers


def build_html():
    global html_out
    
    # == Description ==
    html_out += "<section id=\"description\">\n"
    html_out += "<h1>Description</h1>\n<div>\n"
    html_out += get_description() + "\n</div>\n</section>\n"

    # == Courses ==
    html_out += "<section id=\"courses\">\n"
    html_out += "<h1>Courses</h1>\n<div>\n"
    c_ = get_courses()
    if len(c_) > 0:
        for c in c_:
            html_out += c + "\n"
    else:
        html_out += "<p style='text-align:center;'>There are no courses yet.</p>\n"
    html_out += "</div>\n</section>\n"

    # == Students ==
    html_out += "<section id=\"students\">\n"
    html_out += "<h1>Student Testimonies</h1>\n<div>\n"
    s_ = get_students()
    if len(s_) > 0:
        for s in s_:
            html_out += s + "\n"
    else:
        html_out += "<p style='text-align:center;'>There are no student testimonies yet.</p>\n"
    html_out += "</div>\n"
    html_out += "<p style='text-align:center;'>If you are a student and would like to add your testimony click <a href='https://forms.gle/4nQaBPgMga2XVb9H6'>here</a>.</p>"
    html_out +="</section>\n"
    
    # == Teachers ==
    html_out += "<section id=\"teachers\">\n"
    html_out += "<h1>Teachers</h1>\n<div>\n"
    t_ = get_teachers()
    if len(t_) > 0:
        for t in t_:
            html_out += t + "\n"
    else:
        html_out += "<p style='text-align:center;'>There are no teachers yet.</p>\n"
    html_out += "</div>\n</section>\n"

    print(tColors.BOLD  + tColors.GREEN + " ✓ " + tColors.BLUE + "Raw HTML" + tColors.NORMAL ) #+ html_out)

def write_html_to_file():
    with open('src/build/index.html', 'r') as f:
        index = f.read()
        
        index = index.replace("<!--main-->", html_out)

        open('src/index.html', 'w').write(index)

    print(tColors.BOLD  + tColors.GREEN + " ✓ " + tColors.BLUE + "Wrote HTML to file" + tColors.NORMAL)

if __name__ == '__main__':
    os.system('cls')
    Reset_Build()
    build_html()
    write_html_to_file()

    print(tColors.BOLD + tColors.GREEN + "===Build Complete===" + tColors.NORMAL)
