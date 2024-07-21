#!/usr/bin/python3
"""Convertes markdown files to html files."""


import sys
from pathlib import Path


def markdown2html():
    """Main function of the script."""

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    for i in range(1, 3):
        if not Path(sys.argv[i]).is_file():
            print("Missing {}".format(sys.argv[i]), file=sys.stderr)
            sys.exit(1)

    with open(sys.argv[1], 'r') as mdfile:
        lines = mdfile.readlines()

    with open(sys.argv[2], 'w', encoding='utf-8') as htmlfile:
        for line in lines:
            if line.startswith("#"):
                level = 0
                while line[level] == '#':
                    level += 1
                line_content = line[level:].strip()
                htmlfile.write(f"<h{level}>{line_content}</h{level}>\n")

    sys.exit(0)


__name__ == "__main__" and markdown2html()
