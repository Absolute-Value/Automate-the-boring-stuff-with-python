#! /usr/bin/env python3
# 9.7.3_Prepare.py - 9.7.3のファイル準備用

import os

def prepare_serial_number(folder='Files', head='spam'):
    os.makedirs(folder, exist_ok=True)

    for i in range(1, 23+1):
        if i == 4 or i == 10 or i==11:
            continue
        with open(os.path.join(folder, head + str(i).zfill(3) + '.txt'), 'a') as f:
            f.write(str(i))

prepare_serial_number()