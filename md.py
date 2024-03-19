import utils
import sys

if len(sys.argv) == 1:
    print("Script regires an argument to run")
    quit()

argument = sys.argv[1]
if argument == "-h" or argument == "--help":
    print("Type command followed by a file to be rendered.\nExample:\nmd example.md")
    quit()

try:
    with open(argument, "r") as f:
        utils.render_file(f.readlines())
except FileNotFoundError:
    print("File not found")

