#! /usr/bin/env python3
# 9.7.3.1_FillSerialNumber.py - 連番の飛びを埋める

import sys, os

def fill_searial_number(folder='Files', head='spam'):
    if not os.path.exists(folder):
        print('フォルダーが存在しません')

    while(True):
        count = 0
        num = 1
        filenames = sorted(os.listdir(folder))
        for filename in filenames:
            if os.path.isdir(filename):
                continue
            
            if not str(num) in filename:
                num_length = len(os.path.splitext(filename.lstrip(head))[0])
                before_filepath = os.path.join(folder, filename)
                after_filename = head + str(num).zfill(num_length) + os.path.splitext(filename)[1]
                after_filepath = os.path.join(folder, after_filename)
                print(before_filepath, after_filepath)
                os.rename(before_filepath, after_filepath)
                count += 1
            else:
                filename = filename.lstrip(head)
            num += 1
        if count == 0:
            break

if len(sys.argv) < 2:
    fill_searial_number()
elif len(sys.argv) == 2:
    fill_searial_number(sys.argv[1])
else:
    fill_searial_number(sys.argv[1], sys.argv[2])