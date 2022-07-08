#! /usr/bin/env python3
# 8.10.1_MultiClipBoard.py - クリップボードのテキストを保存・復元
# Usage:
# 8.10.1_MultiClipBoard.py save <keyword> - クリップボードをキーワードに紐づけて保存
# 8.10.1_MultiClipBoard.py <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
# 8.10.1_MultiClipBoard.py list - 全キーワードをクリップボードにコピー
# 8.10.1_MultiClipBoard.py delete <keyword> - キーワードを削除

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.pop(sys.argv[2])

elif len(sys.argv) == 2:
    # キーワード一覧と，内容の読み込み
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
