import sys
import re

listType = ""
Inlist = False
CloseList = False

def subs_bolds(line):
    bold_regex = re.compile(r'\*\*(.*?)\*\*')
    return bold_regex.sub(r'<b>\1</b>', line)

def subs_italic(line):
    italic = re.compile(r'\*(.*?)\*')
    return italic.sub(r'<i>\1</i>', line)

def subs_link(line):
    link = re.compile(r'(\[)(.*)(\])\((.*)\)')
    return link.sub(r'<a href=\"\4\">\2</a>', line)

def subs_images(line):
    images = re.compile(r'!(\[)(.*)(\])\((.*)\)')
    return images.sub(r'<img src=\"\4\" alt=\"\2\">', line)

def subs_header(line):
    header = re.search(r'^(\s*(#(?!#)|##(?!#)|###))', line)
    if header:
        if header.group(2) == "#":
            new_line = "<h1>" + line.strip('# ') + "</h1>\n"
            return new_line
        elif header.group(2) == "##":
            new_line = "<h2>" + line.strip('# ') + "</h2>\n"
            return new_line
        elif header.group(2) == "###":
            new_line = "<h3>" + line.strip('# ') + "</h3>\n"
            return new_line
    return line

def subs_list(line):
    global Inlist
    global CloseList
    global listType

    ul_regex = re.compile(r'^\s*[\*\-\+] (.*)$')
    ol_regex = re.compile(r'^\s*\d+\.\s(.*)$')

    matchul = ul_regex.match(line)
    matchol = ol_regex.match(line)

    if matchul:
        if not Inlist:
            listType = "ul"
            Inlist = True
            CloseList = False
            return "<ul>\n<li>" + matchul.group(1) + "</li>\n"
        else:
            return "<li>" + matchul.group(1) + "</li>\n"
    elif matchol:
        if not Inlist:
            listType = "ol"
            Inlist = True
            CloseList = False
            return "<ol>\n<li>" + matchol.group(1) + "</li>\n"
        else:
            return "<li>" + matchol.group(1) + "</li>\n"
    else:
        if Inlist:
            CloseList = True
            Inlist = False
    return line

def process_line(line):
    bolds = subs_bolds(line)
    italics = subs_italic(bolds)
    images = subs_images(italics)
    links = subs_link(images)
    header = subs_header(links)
    return subs_list(header)

def main():
    global CloseList

    file = sys.stdin.read()
    linhas = file.split("\n")
    text = ""
    for linha in linhas:
        new_line = process_line(linha)
        text += new_line
        if (CloseList):
            text += f"</{listType}>\n"
            CloseList = False
    if (Inlist):
        text += f"</{listType}>\n"

    open("output.html", "w").write(text)


if __name__ == "__main__":
    main()