import os
import sys
import shutil

from copystatic import copy_files_recursive
from generate_page import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"
basepath = sys.argv[0]


def main():
    print("Deleting docs directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_pages_recursive("content", "template.html", "docs", basepath)


main()
