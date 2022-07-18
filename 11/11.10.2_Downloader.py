#! /usr/bin/env python3
# 11.10.2_Downloader.py - 画像サイトのダウンローダー

import os
from PIL import Image
from io import BytesIO
import requests, sys, bs4, re

url = 'https://www.flickr.com/search/?text=' + ' '.join(sys.argv[1:])
print(f'ページをダウンロード中 {url}...') # Googleページをダウンロード中にテキストを表示
res = requests.get(url)
res.raise_for_status()

# 上位の検索結果のリンクを取得する
soup = bs4.BeautifulSoup(res.text, 'html5lib')
link_elems = soup.select(".view .awake")
regex = re.findall(r'//.*\.jpg', str(link_elems))
if len(regex) == 0:
    print('画像が見つかりませんでした。')
else:
    os.makedirs('downloads', exist_ok=True)
    for i, reg in enumerate(regex):
        img_url = 'https:' + reg
        print(f'画像をダウンロード中 {img_url}...')
        res = requests.get(img_url)
        res.raise_for_status()

        with open(os.path.join('downloads', f'{i+1}_{os.path.basename(img_url)}'), 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)

print('完了')