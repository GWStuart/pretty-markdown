import os
import pyfiglet
from pyfiglet import FigletFont

columns = os.get_terminal_size().columns
content_width = 100 # should be even
box_start = (columns - (content_width + 2)) // 2
end = "│"
left = " " * box_start + end 
space = left + "\x1b[1;32;40m" + " " * content_width + "\x1b[0m" + end 


def render_file(file):
    # render top of file
    print(" " * box_start + "╭" + "─" * content_width + "╮" + " " * box_start)

    for line in file:
        render_line(line[:-1])

    print(left[:-1] + "╰" + "─" * content_width + "╯")

def print_ascii(f):
    spacing = " " * ((content_width - len(f[1])) // 2)
    for line in f:
        print(left + "\x1b[1;31;40m" + spacing + line + spacing + "\x1b[0m" +  "│")

    # for line in f.split("\n"):
    #     print(left + line + " " * (content_width - len(line)) + end)

def render_line(line):
    if line == "":
        print(space)
    elif line[0] == "/":
        pass
    elif line[0] == "#":
        font = FigletFont("/home/will/github/pretty-markdown/big-money-ne")
        print(font.height)

        f = pyfiglet.figlet_format(line[2:], font="/home/will/github/pretty-markdown/big-money-ne", width=content_width, justify="center").split("\n")
        print_ascii(f)
    elif line[0] == "-":
        print("list")
    elif line.replace(" ", "").strip() == "":
        print(space)
    else:
        print(left + line + " " * (content_width - len(line)) + end)
    
