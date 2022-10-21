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

    CHECK = BOLD  + GREEN + " ✓ " + NORMAL
    CROSS = BOLD + FAIL + " ✗ " + NORMAL
    INFO = BOLD + BLUE + " ℹ " + NORMAL
    WARN = BOLD + WARNING + " ⚠ " + NORMAL
    HEAD = BOLD + HEADER + " ➜ " + NORMAL

html_out = ""

def Reset_Build():
    # Remove old build
    files = os.listdir('src/build/views')
    for file in files:
        os.remove('src/build/views/' + file)
    print(tColors.CHECK + tColors.BLUE + "Removed old build" + tColors.NORMAL)

class MD_to_HTML:
    def get_description():
        # "Description" MD to HTML
        description = markdown.markdown(open('md/description.md', 'r').read())
        print(tColors.CHECK + tColors.BLUE + "Description" + tColors.NORMAL )
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
        print(tColors.CHECK + tColors.BLUE + "Courses and Example Coursework" + tColors.NORMAL )
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
        print(tColors.CHECK + tColors.BLUE + "Students" + tColors.NORMAL )
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
        print(tColors.CHECK + tColors.BLUE + "Teachers" + tColors.NORMAL )
        return teachers

class HTML_Build:
    def build_description():
        out = ""

        out += "<section id=\"description\">\n"
        out += "<h1>Description</h1>\n"
        out += "<div>\n"
        out += MD_to_HTML.get_description() + "\n"
        out += "</div>\n"
        out += "</section>\n"

        return out
    def build_courses():
        out = ""

        out += "<section id=\"courses\">\n"
        out += "<h1>Courses</h1>\n"
        out += "<div>\n"
        c_ = MD_to_HTML.get_courses()
        if len(c_) > 0:
            for c in c_:
                out += c + "\n"
        else:
            out += "<p style='text-align:center;'>There are no courses yet.</p>\n"
        out += "</div>\n"
        out += "</section>\n"

        return out
    def build_students():
        out = ""

        out += "<section id=\"students\">\n"
        out += "<h1>Student Testimonies</h1>\n"
        out += "<div>\n"
        s_ = MD_to_HTML.get_students()
        if len(s_) > 0:
            for s in s_:
                out += s + "\n"
        else:
            out += "<p style='text-align:center;'>There are no student testimonies yet.</p>\n"
        out += "</div>\n"
        out += "<p style='text-align:center;'>If you are a student and would like to add your testimony click <a href='https://forms.gle/4nQaBPgMga2XVb9H6'>here</a>.</p>"
        out +="</section>\n"

        return out
    def build_teachers():
        out = ""

        out += "<section id=\"teachers\">\n"
        out += "<h1>Teachers</h1>\n"
        out += "<div>\n"
        t_ = MD_to_HTML.get_teachers()
        if len(t_) > 0:
            for t in t_:
                out += t + "\n"
        else:
            out += "<p style='text-align:center;'>There are no teachers yet.</p>\n"
        out += "</div>\n"
        out += "</section>\n"

        return out
    def build_html():
        out = ""

        # == Description ==
        out += HTML_Build.build_description()

        # == Courses ==
        out += HTML_Build.build_courses()

        # == Students ==
        out += HTML_Build.build_students()

        # == Teachers ==
        out += HTML_Build.build_teachers()

        print(tColors.CHECK + tColors.BLUE + "Raw HTML" + tColors.NORMAL ) #+ html_out)

        return out

def write_html_to_file():
    with open('src/build/index.html', 'r') as f:
        index = f.read()
        
        index = index.replace("<!--main-->", HTML_Build.build_html())

        open('src/index.html', 'w').write(index)

    print(tColors.CHECK + tColors.BLUE + "Wrote HTML to file" + tColors.NORMAL)

if __name__ == '__main__':
    os.system('cls')
    Reset_Build()
    write_html_to_file()

    print(tColors.BOLD + tColors.GREEN + "===Build Complete===" + tColors.NORMAL)
