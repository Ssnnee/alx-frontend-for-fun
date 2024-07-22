#!/usr/bin/python3
"""Convertes markdown files to html files."""


import sys
from pathlib import Path


def markdown2html():
    """Main function of the script."""

    try:
        if len(sys.argv) < 3:
            print("Usage: ./markdown2html.py README.md README.html",
                  file=sys.stderr)
            sys.exit(1)

        if not Path(sys.argv[1]).is_file():
            print("Missing {}".format(sys.argv[1]), file=sys.stderr)
            sys.exit(1)

        with open(sys.argv[1], 'r') as mdfile:
            lines = mdfile.readlines()

        with open(sys.argv[2], 'w', encoding='utf-8') as htmlfile:
            is_ul = False
            ul_opened = False

            for line in lines:
                if line.startswith("#"):
                    if (ul_opened):
                        htmlfile.write("</ul>\n")
                        ul_opened = False
                        is_ul = False
                    level = 0
                    while line[level] == '#':
                        level += 1
                    line_content = line[level:].strip()
                    htmlfile.write(f"<h{level}>{line_content}</h{level}>\n")

                elif not is_ul:
                    htmlfile.write("<ul>\n")
                    is_ul = True
                    ul_opened = True

                if line.startswith("- "):
                    line_content = line[2:].strip()
                    htmlfile.write(f"<li>{line_content}</li>\n")

            if is_ul:
                htmlfile.write("</ul>\n")
                ul_opened = False

    except Exception:
        sys.exit(1)


__name__ == "__main__" and markdown2html()
