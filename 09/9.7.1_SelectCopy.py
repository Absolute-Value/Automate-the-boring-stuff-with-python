#! /usr/bin/env python3
# 9.7.1_SelectCopy.py - フォルダから特定のファイルを新しいフォルダにコピーする
# Usage:
# 9.4_SelectCopy.py <folder> <extention> - <folder>の<extention(拡張子)>を新しいフォルダにコピー

import shutil, os, sys

# クリップボードの内容を保存
if len(sys.argv) != 3:
    print("コピーにしたいフォルダと拡張子を入力してください")

def select_copy(folder, extention):
    #folder = os.path.abspath(folder) # folderを絶対パスに

    # フォルダのツリーを渡り歩いてその中のファイルを圧縮する
    for foldername, subfolders, filenames in os.walk(folder):
        new_foldername = foldername.replace('..','.')

        # 現在のフォルダの中の全ファイルをZIPファイルに追加する
        for filename in filenames:
            if str(extention) in filename:
                os.makedirs(new_foldername, exist_ok=True)
                print(f'Making folder: {new_foldername}')

                newfile_path = os.path.join(new_foldername,filename)
                shutil.copy(os.path.join(foldername, filename), newfile_path)
                print(f'Copy file: {newfile_path}')

    print("Done.")

select_copy(sys.argv[1], sys.argv[2])