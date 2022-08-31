#! /usr/bin/env python3
# 8.10.1 マルチクリップボードを拡張
# Usage:
# 8.10.1_MultiClipBoard.py save <keyword> - クリップボードをキーワードに紐づけて保存
# 8.10.1_MultiClipBoard.py <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
# 8.10.1_MultiClipBoard.py list - 全キーワードをクリップボードにコピー
# 8.10.1_MultiClipBoard.py delete <keyword> - キーワードを削除

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

mode = sys.argv[1].lower()
clip_board = pyperclip.paste()

# クリップボードの内容を保存
if len(sys.argv) == 3:
    keyword = sys.argv[2]
    if mode == 'save':
        mcb_shelf[keyword] = clip_board
        print(f"クリップボード上の {clip_board} を {keyword}　として保存しました")
    elif mode == 'delete':
        mcb_shelf.pop(keyword)
        print(f"{keyword}を削除しました")

elif len(sys.argv) == 2:
    # キーワード一覧と，内容の読み込み
    if mode == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print("全キーワードをクリップボードにコピーしました")
    elif sys.argv[1] in mcb_shelf:
        content = mcb_shelf[sys.argv[1]]
        pyperclip.copy(content)
        print(f"{content} をクリップボードにコピーしました")

mcb_shelf.close()
