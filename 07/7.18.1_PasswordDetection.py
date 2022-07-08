# 7.18.1 強いパスワードの検出

import re

given_password = str(input("パスワードを入力してください："))
is_strong = True

if len(given_password) < 8:
    print("弱い：8文字以上を推奨")
    is_strong = False

upper_regex = re.compile(r'[A-Z]')
mo_u = upper_regex.search(given_password)
lower_regex = re.compile(r'[a-z]')
mo_l = lower_regex.search(given_password)
if mo_u is None or mo_l is None:
    print("弱い：大文字と小文字を推奨")
    is_strong = False

num_regex = re.compile(r'\d')
mo = num_regex.search(given_password)
if mo is None:
    print("弱い：一つ以上の数字を推奨")
    is_strong = False

if is_strong:
    print("強いパスワードです。")