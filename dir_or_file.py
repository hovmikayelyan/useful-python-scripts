#!/usr/bin/env python3
# @author hovmikayelyan
#
# This script allows us to check all files and directories specified,
# and print if it is a file or a directory.
# You can change the functions logic below.
#
# Thank you!

import os
os.listdir("folder_name")

dir = "folder_name"
for name in os.listdir(dir):
    fullname = os.path.join(name, dir)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
