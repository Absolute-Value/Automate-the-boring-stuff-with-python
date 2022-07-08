# 3.11.1 コラッツ数列

def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1

number = int(input("整数を入力してください："))
while(True):
    print(number)
    if number == 1:
        break
    else:
        number = int(collatz(number))