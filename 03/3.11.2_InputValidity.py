#! /usr/bin/env python3
# 3.11.2 入力の妥当性検証

def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1

while(True):
    try:
        number = int(input("整数を入力してください："))
        break
    except:
        print("エラー：整数値を入力してください")

while(True):
    print(number)
    if number == 1:
        break
    else:
        number = int(collatz(number))