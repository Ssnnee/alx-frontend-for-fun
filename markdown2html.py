#!/usr/bin/python3
"""Convertes markdown files to html files."""


import sys
from pathlib import Path


def markdown2html():
    """Main function of the script."""
    arr_to_write = []

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    for i in range(1, 3):
        if not Path(sys.argv[i]).is_file():
            print("Missing {}".format(sys.argv[i]), file=sys.stderr)
            sys.exit(1)

    with open(sys.argv[1], 'r') as mdfile:
        content = mdfile.readlines()

    for line in content:
        parsed_line = line.split()
        if (parsed_line[0].startswith("#")):
            level = parsed_line[0].count("#")
            line_content = line[level:-1].strip()
            with open(sys.argv[2], mode="w", encoding="utf-8") as file:
                arr_to_write.append("<h{}>{}<h{}>\n".format(
                    level, line_content, level))

                file.write("".join(arr_to_write))


__name__ == "__main__" and markdown2html()
