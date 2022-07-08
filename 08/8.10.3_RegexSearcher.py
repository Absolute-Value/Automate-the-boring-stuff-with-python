#! /usr/bin/env python3
# 8.10.3 正規表現探索

import re, sys, os

if len(sys.argv) != 2:
    print("探索したいフォルダのパスを入力してください")
    sys.exit()

regex = re.compile(str(input("正規表現を入力してください：")))
for file in os.listdir(sys.argv[1]):
    if ".txt" in file:
        txt_file = open(os.path.join(sys.argv[1], file))
        txt_content = txt_file.read()
        txt_file.close()

        targets = regex.findall(txt_content)
        if len(targets) != 0:
            print(file)
            
            export_content = txt_content
            for target in set(targets):
                export_content = re.sub(target, f'"{target}"', export_content)
            print(export_content)