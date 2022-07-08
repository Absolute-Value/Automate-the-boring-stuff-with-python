#! /usr/bin/env python3
# 正規表現を用いたstrip()メソッド

import re

def strip(string, target=' '):
    regex = re.compile(f'^{str(target)}+|{str(target)}+$')
    string = regex.sub('', string)
    return string

given_string = str(input("文字列を入力してください："))
target_string = str(input("変えたい文字列を入力してください（何も入力しないとスペース）："))
if target_string == '':
    target_string = ' '

print(strip(given_string, target_string))