#! /usr/bin/env python3

import random

def StrToNum(input):
    if input ==  '表':
        return 1
    else:
        return 0

guess = ''
while guess not in ('表', '裏'):
    print('コインの裏表を当ててください。表か裏かを入力してください：')
    guess = input()

guess = StrToNum(guess)
toss = random.randint(0,1) # 0は裏、1は表
if toss == guess:
    print('当たり！')
else:
    print('はずれ！もう一回あてて！')
    while guess not in ('表', '裏'):
        print('表か裏かを入力してください：')
        guess = input()
    guess = StrToNum(guess)
    if toss == guess:
        print('当たり！')
    else:
        print('はずれ。このゲームは苦手ですね。')