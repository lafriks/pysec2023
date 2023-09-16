"""Example to list directory recursively"""

import os
import sys

path = os.curdir
if len(sys.argv) > 1:
    path = os.path.normpath(sys.argv[1])

src_level = len(path.split(os.sep))

for root, _, files in os.walk(path):
    dirs = root.split(os.sep)
    level = len(dirs) - src_level

    # Print current directory
    print(f"{'  ' * level}➜ {dirs[len(dirs)-1]}")

    # Print all files
    file_count = len(files)
    for i, name in enumerate(files):
        sep = "├─ "
        if i == file_count - 1:
            sep = "└─ "
        print(f"{'  ' * (level+1)}{sep}{name}")
