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


__name__ == "__main__" and markdown2html()
