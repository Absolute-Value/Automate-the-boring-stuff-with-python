#! /usr/bin/env python3
# 9.7.1_SelectCopy.py - フォルダから特定のファイルを新しいフォルダにコピーする
# Usage:
# 9.4_BackupToZip.py <folder> <extention> - <folder>の<extention(拡張子)>を新しいフォルダにコピー

import os, sys

# クリップボードの内容を保存

def search_file(folder, size=100):
    folder = os.path.abspath(folder) # folderを絶対パスに

    # フォルダのツリーを渡り歩いてその中のファイルを圧縮する
    for foldername, subfolders, filenames in os.walk(folder):

        # 現在のフォルダの中の全ファイルをZIPファイルに追加する
        for filename in filenames:
            file_path = (os.path.join(foldername, filename))
            if os.path.getsize(file_path) > int(size):
                print(f'{file_path} : {os.path.getsize(file_path)} MB')

    print("Done.")

if len(sys.argv) < 2:
    print("サイズの大きいファイルを探したいフォルダを入力してください")
elif len(sys.argv) == 2:
    search_file(sys.argv[1])
else:
    search_file(sys.argv[1], sys.argv[2])