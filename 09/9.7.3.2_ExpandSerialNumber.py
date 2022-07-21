#! /usr/bin/env python3
# 9.7.3.2_ExpandSerialNumber.py - 連番の隙間を開ける

import sys, os

def expand_serial_number(expand_num=3, folder='Files', head='spam'):
    filenames = sorted(os.listdir(folder), reverse=True)
    if len(filenames) < expand_num:
        sys.exit()
    for filename in filenames:
        before_filepath = os.path.join(folder, filename)
        num = os.path.splitext(filename.lstrip(head))[0]
        after_filename = head + str(int(num)+1).zfill(len(num)) + os.path.splitext(filename)[1]
        after_filepath = os.path.join(folder, after_filename)
        print(before_filepath, after_filepath)
        os.rename(before_filepath, after_filepath)
        if int(num) == expand_num:
            break

if len(sys.argv) < 2:
    expand_serial_number
else:
    expand_serial_number(int(sys.argv[1]))