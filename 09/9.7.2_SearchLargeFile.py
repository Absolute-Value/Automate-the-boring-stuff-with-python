#! /usr/bin/env python3
# 9.7.2_SeachLargeFile.py - フォルダから大きいサイズのファイルを探し出す
# Usage:
# 9.7.2_SeachLargeFile.py <folder> - <folder>を探す
# 9.7.2_SeachLargeFile.py <folder> <size> - <folder>から<size>B以上のファイルを探す
# 9.7.2_SeachLargeFile.py <folder> <size> <unit> - <folder>から<size><unit>以上のファイルを探す

import os, sys

# クリップボードの内容を保存

def search_file(folder, size=100, unit='KB'):
    folder = os.path.abspath(folder) # folderを絶対パスに

    # フォルダのツリーを渡り歩いてその中のファイルを圧縮する
    for foldername, subfolders, filenames in os.walk(folder):

        # 現在のフォルダの中の全ファイルをZIPファイルに追加する
        for filename in filenames:
            file_path = (os.path.join(foldername, filename))
            
            file_size = os.path.getsize(file_path)
            if unit == 'KB':
                file_size = file_size / 1000
            elif unit == 'MB':
                file_size = file_size / 1000 / 1000
            elif unit == 'GB':
                file_size == file_size / 1000 / 1000 / 1000

            if  file_size > int(size):
                print(f'{file_path} : {file_size:.2f} {unit}')

    print("Done.")

if len(sys.argv) < 2:
    print("サイズの大きいファイルを探したいフォルダを入力してください")
elif len(sys.argv) == 2:
    search_file(sys.argv[1])
elif len(sys.argv) == 3:
    search_file(sys.argv[1], sys.argv[2])
else:
    search_file(sys.argv[1], sys.argv[2], sys.argv[3])