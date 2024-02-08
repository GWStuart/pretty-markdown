import os
import pyfiglet
from pyfiglet import FigletFont, Figlet

columns = os.get_terminal_size().columns

if columns > 120: 
    content_width = 100 # should be even
elif columns > 90:
    content_width = columns - 20
elif columns > 75:
    content_width = columns - 10
elif columns > 40:
    content_width = columns - 4 
else:
    content_width = columns - 2

box_start = (columns - (content_width + 2)) // 2
left = " " * box_start + "│" 

font = "standard" # ~/github/pretty-markdown/big-money-ne"
figlets = [Figlet(font=font, width=content_width, justify="center"),
           Figlet(font=font, width=content_width)]
# figlet_center = Figlet(font=font, width=content_width, justify="center")
# figlet_left = Figlet(font=font, width=content_width)
font_height = figlets[0].Font.height

def render_file(file):
    # render top of file
    print(" " * box_start + "╭" + "─" * content_width + "╮" + " " * box_start)

    for line in file:
        render_line(line[:-1])

    print(left[:-1] + "╰" + "─" * content_width + "╯")

def print_ascii(f):
    rows = int((len(f) - 1) / font_height)
    for i in range(rows):
        for line in f[i*font_height:(i+1)*font_height]:
            print_formatted(line, colour=31, ascii_type=1)

def print_formatted(text, colour=32, ascii_type=0):
    length = len(text)
    print(left + f"\x1b[{ascii_type};{colour};40m" + text + " " * (content_width - length) + "\x1b[0m" + "│")

def _print_colours():
    for i in range(7):
        print(f"\x1b[1;{31 + i};40m  {31 + i}test ")
    print("\033[0m")

def render_line(line):
    if "**" in line:
        first = line.index("**")
        second = first + line[first + 1:].index("**") + 1
        line = line[0:first] + "\x1b[1m" + line[first+2:second] + "\x1b[0;32;40m" + line[second+2:]

        #line = line.replace("**", "\x1b[1m") # \x1b[1")
        ascii_type = 0
    elif "*" in line:
        first = line.index("*")
        second = first + line[first + 1:].index("*") + 1
        line = line[0:first] + "\x1b[3m" + line[first+1:second] + "\x1b[0;32;40m" + line[second+1:]
        # line = line.replace("*", "\x1b[3m") # \x1b[1")
        ascii_type = 0
    elif "`" in line:
        first = line.index("`")
        second = first + line[first + 1:].index("`") + 1
        line = line[0:first] + "\x1b[2m" + line[first+1:second] + "\x1b[0;32;40m" + line[second+1:]

        ascii_type = 0
    else:
        ascii_type = 0

    if line == "":
        print_formatted("")
    elif line[0] == "/":
        pass
    elif line[0] == "#":
        heading = line.count("#")
        if heading > len(figlets):
            print("Too many headings")
            quit()
        f = figlets[heading - 1].renderText(line[2:]).split("\n")

        print_ascii(f)
    elif line[0] == "-":
        print_formatted("  " + line, colour=33, ascii_type=ascii_type)
    elif line.replace(" ", "").strip() == "":
        print_formatted("")
    else:
        print_formatted("  " + line, ascii_type=ascii_type)

