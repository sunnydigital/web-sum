#!/usr/bin/env python3

"""This script outputs as HTML the diffs between
files in the Hugo theme specified in variable ``THEME`` and the modified ones in the project.

See https://main--cheerful-mousse-b9d87b.netlify.app/posts/papermod_diff for deployed output.

Run this script from the root of the project. Output will be in scripts/{THEME}_diff (configurable).
This script is wrapped by ``scripts/build``, which moves the output to ``content/`` to be deployed.

Dependencies: ansi2html. ``pip3 install ansi2html``."""

__author__ = "Jesse Wei <jesse@cs.unc.edu>"

from pathlib import Path
from helpers.cd import cd
# Netlify's Python environment doesn't allow list[Path], etc.
from typing import List
import os

THEME: str = "PaperMod"
"""You can modify the theme name."""
THEME_DIR: Path = Path("themes") / THEME
OUTPUT_DIR: Path = Path("scripts") / f"{THEME}_diff"
if not OUTPUT_DIR.exists():
    OUTPUT_DIR.mkdir(parents=True)
MODIFIED_DIRECTORIES: List[Path] = [Path("assets"), Path("layouts")]
for i, directory in enumerate(MODIFIED_DIRECTORIES):
    if not directory.exists():
        del MODIFIED_DIRECTORIES[i]

# This is kinda wack bruh
# See helpers/generate_directory_index_caddystyle.py line 55
HTML_AT_END_OF_INDEX_FILE: List[str] = [
    "<br><br>\n",
    f'<p>This page shows `diff`s between overriding files in <a href="https://github.com/jesse-wei/jessewei.dev-PaperMod/tree/main/assets">assets/</a> and <a href="https://github.com/jesse-wei/jessewei.dev-PaperMod/tree/main/layouts">layouts/</a> and the OG files in themes/{THEME}/assets and themes/{THEME}/layouts.</p>\n',
    "<p>Note that if a file in the theme submodule is updated, then the diff will also be updated when this page is regenerated.</p>\n",
    "<p>This page is generated by scripts/diff.py, which is wrapped by scripts/build.</p>\n"
    '<p>Both scripts are <a href="https://github.com/jesse-wei/jessewei.dev-PaperMod/tree/main/scripts">here</a>.</p>\n',
    '<p>Setup is further described <a href="https://jessewei.dev/blog/2023/papermod/#ci">here</a>.</p>\n',
]
"""HTML text to be appended (right before </main>) to the generated root index.html file."""

for directory in MODIFIED_DIRECTORIES:
    for modified_file in directory.rglob("*"):
        if modified_file.is_file():
            # Output of diff will go here
            output_html: Path = (OUTPUT_DIR / modified_file).with_suffix(".html")
            # Create parent directories if they don't exist
            output_html.parent.mkdir(parents=True, exist_ok=True)

            og_file: Path = THEME_DIR / modified_file

            # If OG file doesn't exist, create an empty temp file to diff with
            # The diff will be everything, indicating that the file is brand-new
            temp_file_created: bool = False
            if not og_file.exists():
                temp_file_created = True
                og_file.touch()

            # Generate HTML file (with color) from diff (with color)
            os.system(f"diff --color=always {og_file} {modified_file} | ansi2html > {output_html}")

            if temp_file_created:
                og_file.unlink()

# Not an official Python feature
# See helpers/cd.py
# At this point, OUTPUT_DIR is populated with HTML files in directories. Just need to generate index.html files
with cd(OUTPUT_DIR):
    # Generate index.html files in directories recursively
    command: str = "python ../helpers/generate_directory_index_caddystyle.py -r"
    if os.system(command) != 0:
        if os.system(command.replace("python", "python3")) != 0:
            raise Exception(f"{command} doesn't work. python and python3 both don't work. Is Python installed?")

    # Append some explanatory text to homepage
    with open("index.html", "r") as homepage:
        contents = homepage.readlines()
    content_end_index: int = contents.index("</main>\n")
    for html_text in reversed(HTML_AT_END_OF_INDEX_FILE):
        contents.insert(content_end_index, html_text)
    with open("index.html", "w") as homepage:
        contents = "".join(contents)
        homepage.write(contents)