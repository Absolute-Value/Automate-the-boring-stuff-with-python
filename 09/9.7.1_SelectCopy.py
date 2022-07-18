#! /usr/bin/env python3
# 9.7.1_SelectCopy.py - フォルダから特定のファイルを新しいフォルダにコピーする
# Usage:
# 9.4_BackupToZip.py <folder> <extention> - <folder>の<extention(拡張子)>を新しいフォルダにコピー

import zipfile, os, sys

# クリップボードの内容を保存
if len(sys.argv) != 3:
    print("コピーにしたいフォルダと拡張子を入力してください")

def backup_to_zip(folder):
    #folder = os.path.abspath(folder) # folderを絶対パスに

    # 既存のファイル名からファイル名の連番を決める
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # ZIPファイルを作成する
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # フォルダのツリーを渡り歩いてその中のファイルを圧縮する
    for foldername, subfolders, filenames in os.walk(folder):
        foldername2 = foldername.replace('..','.')

        print(f'Adding files in {foldername2}')
        # 現在のフォルダをZIPファイルに追加する
        #backup_zip.write(foldername)
        # 現在のフォルダの中の全ファイルをZIPファイルに追加する
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            print(new_base)
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename), os.path.join(foldername2,filename))

    backup_zip.close()
    print("Done.")

backup_to_zip(sys.argv[1])