#! /usr/bin/env python3

import random

guess = ''
while guess not in ('表', '裏'):
    print('コインの裏表を当ててください。表か裏かを入力してください：')
    guess = input()

toss = random.randint(0,1) # 0は裏、1は表
if toss == guess:
    print('当たり！')
else:
    print('はずれ！もう一回あてて！')
    guess = input()
    # 2回目を振り直すなら、ここに
    # toss = random.randint(0,1)
    # を入れる
    if toss == guess:
        print('当たり！')
    else:
        print('はずれ。このゲームは苦手ですね。')