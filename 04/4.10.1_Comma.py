#! /usr/bin/env python3
# 4.10.1 コンマ付け

def AddComma(given_list):
    string = ''
    for _ in range(len(given_list) - 1):
        string += given_list.pop(0) + ', '
    string += 'and ' + given_list[0]
    return string

spam = ['apples', 'bananas', 'tohu', 'cats']
print(AddComma(spam))