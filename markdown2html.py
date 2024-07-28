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
            l_opened = False
            is_ol = False

            for line in lines:
                if line.startswith("#"):
                    if (l_opened):
                        htmlfile.write("</ul>\n")
                        l_opened = False
                        is_ul = False
                        is_ol = False

                    level = 0
                    while line[level] == '#':
                        level += 1
                    line_content = line[level:].strip()
                    htmlfile.write(f"<h{level}>{line_content}</h{level}>\n")

                elif not is_ul:
                    htmlfile.write("<ul>\n")
                    is_ul = True
                    l_opened = True

                elif not is_ol:
                    htmlfile.write("<ol>\n")
                    is_ol = True
                    l_opened = True

                if line.startswith("- "):
                    line_content = line[2:].strip()
                    htmlfile.write(f"<li>{line_content}</li>\n")

                if line.startswith("* "):
                    line_content = line[2:].strip()
                    htmlfile.write(f"<li>{line_content}</li>\n")

            if is_ul:
                htmlfile.write("</ul>\n")
                l_opened = False

            if is_ol:
                htmlfile.write("</ol>\n")
                l_opened = False

    except Exception:
        sys.exit(1)


__name__ == "__main__" and markdown2html()
