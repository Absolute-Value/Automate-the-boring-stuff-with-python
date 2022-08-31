#! /usr/bin/env python3
# 8.7_MultiClipBoard.py - クリップボードのテキストを保存・復元
# Usage:
# 8.7_MultiClipBoard.py save <keyword> - クリップボードをキーワードに紐づけて保存
# 8.7_MultiClipBoard.py <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
# 8.7_MultiClipBoard.py list - 全キーワードをクリップボードにコピー

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

mode = sys.argv[1].lower()
clip_board = pyperclip.paste()

# クリップボードの内容を保存
if len(sys.argv) == 3 and mode == 'save':
    keyword = sys.argv[2]
    mcb_shelf[keyword] = clip_board
    print(f"クリップボード上の {clip_board} を {keyword}　として保存しました")

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
