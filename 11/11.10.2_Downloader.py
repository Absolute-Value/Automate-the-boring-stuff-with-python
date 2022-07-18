#! /usr/bin/env python3
# 11.10.2_Downloader.py - 画像サイトのダウンローダー

import os
from PIL import Image
from io import BytesIO
import requests, sys, bs4, re

print('Googling...') # Googleページをダウンロード中にテキストを表示
res = requests.get('https://www.flickr.com/search/?text=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# 上位の検索結果のリンクを取得する
soup = bs4.BeautifulSoup(res.text, 'html5lib')
link_elems = soup.select(".view .awake")

regex = re.findall(r'//.*\.jpg', str(link_elems))

if len(regex) > 0:
    os.makedirs('downloads', exist_ok=True)
    for i, reg in enumerate(regex):
        print(reg)
        res = requests.get('https:' + reg)
        if res.status_code == 200:
            with BytesIO(res.content) as buf:
                im = Image.open(buf)             # PIL.Imageで読込む
                im.save(f"downloads/{sys.argv[1]}_{i}.{im.format.lower()}") # 保存ファイル名に拡張子を設定
