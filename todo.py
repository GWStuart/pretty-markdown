import os

"""
A python script that prints my todo list
"""

columns = os.get_terminal_size().columns
content_width = 100 # should be even
box_start = (columns - (content_width + 2)) // 2
left = " " * box_start + "│" 
space = left + "\x1b[1;32;40m" + " " * content_width + "\x1b[0m" +  "│"

print(" " * box_start + "╭" + "─" * content_width + "╮" + " " * box_start)
print(space)

todo = """
  /$$$$$$$$ /$$$$$$  /$$$$$$$   /$$$$$$ 
 |__  $$__//$$__  $$| $$__  $$ /$$__  $$
    | $$  | $$  \ $$| $$  \ $$| $$  \ $$
    | $$  | $$  | $$| $$  | $$| $$  | $$
    | $$  | $$  | $$| $$  | $$| $$  | $$
    | $$  | $$  | $$| $$  | $$| $$  | $$
    | $$  |  $$$$$$/| $$$$$$$/|  $$$$$$/
    |__/   \______/ |_______/  \______/ 
""".split("\n")[1:-1]

spacing = " " * ((content_width - len(todo[1])) // 2)
for line in todo:
    print(left + "\x1b[1;31;40m" + spacing + line + spacing + "\x1b[0m" +  "│")
print(space)


lst = """
- example 1
- here is a longer example
- i also need to do this btw
""".split("\n")[1:-1]

left_spacing = spacing[:-4]  # ((content_width - len(max(lst))) // 2)
for item in lst:
    print(left + "\x1b[1;32;40m" + left_spacing + item + " " * (content_width - len(left_spacing) - len(item)) + "\x1b[0m" +  "│")
print(space)

# print("\x1b[0m")

# Close the box
print(left[:-1] + "╰" + "─" * content_width + "╯")

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

# print_format_table()
