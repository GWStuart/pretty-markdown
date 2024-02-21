import os
import pyfiglet
from pyfiglet import FigletFont, Figlet

"""
TODO:
    there will be an issue with wordwrapping if the line contains modifiers
"""

content_pad = "  "
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
            print_formatted(line, colour=31)

def print_formatted(text, length="auto", colour=32):
    if length == "auto":
        length = len(text)

    part2 = False
    if length > content_width:
        part2 = text[content_width:]
        text = text[:content_width]
        length = len(text)

    print(left + f"\x1b[0;{colour};40m" + text + " " * (content_width - length) + "\x1b[0m" + "│")

    if part2:
        print_formatted(content_pad + part2, colour=colour)

def _print_colours():
    for i in range(7):
        print(f"\x1b[1;{31 + i};40m  {31 + i}test ")
    print("\033[0m")

def modifier_check(line, length, modifier, effect, line_colour=32): # Checks for the specific modifier and applys the given ascii effect
    if modifier in line:
        first = line.index(modifier)
        second = first + line[first + 1:].index(modifier) + 1
        mod_length = len(modifier)
        line = line[0:first] + effect + line[first+mod_length:second] + f"\x1b[0;{line_colour};40m" + line[second+mod_length:]
        length -= mod_length * 2

    return line, length


def render_line(line):
    length = len(line)

    if line == "":
        colour = 32
    elif line[0] == "#":
        heading = line.count("#")
        if heading > len(figlets):
            print("Too many headings")
            quit()
        f = figlets[heading - 1].renderText(line[2:]).split("\n")

        print_ascii(f)
        return
    elif line[0] == "-":
        colour = 33
    else:
        colour = 32

    line, length = modifier_check(line, length, "**", "\x1b[1m", line_colour=colour)
    line, length = modifier_check(line, length, "*", "\x1b[3m", line_colour=colour)
    line, length = modifier_check(line, length, "`", "\x1b[2m", line_colour=colour)
    line, length = modifier_check(line, length, "__", "\x1b[4m", line_colour=colour)
    line, length = modifier_check(line, length, "~~", "\x1b[9m", line_colour=colour)
    line, length = modifier_check(line, length, "==", "\x1b[7m", line_colour=colour)

    print_formatted(content_pad + line, colour=colour, length=length + 2)

