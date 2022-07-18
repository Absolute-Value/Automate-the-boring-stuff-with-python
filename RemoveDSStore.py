#! /usr/bin/env python3
# RemoveDSStore.py - .DS_Storeファイルを一括削除するためのプログラムです

import os

def search_file(folder='./'):
    folder = os.path.abspath(folder) # folderを絶対パスに

    # フォルダのツリーを渡り歩く
    for foldername, subfolders, filenames in os.walk(folder):

        for filename in filenames:
            if '.DS_Store' in filename:
                file_path = (os.path.join(foldername, filename))
                os.remove(file_path)
                print(f'removed {file_path}')

    print("Done.")

search_file()