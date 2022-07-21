#! /usr/bin/env python3
# 11.10.4_LinkSearch.py - 

import requests, bs4, sys, os

def link_search(url, save_dir='Downloads'):
    os.makedirs(save_dir ,exist_ok=True)

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html5lib')
    links = soup.select("a")

    for link in links:
        href = link.get('href')
        if not href:
            continue

        try:
            res = requests.get(href)
        except:
            print(f'{href} はリンク切れです．')
            continue

        if not href.endswith('.html'):
            href += '.html'
        with open(os.path.join(save_dir, os.path.basename(href)), 'a') as f:
            f.write(res.text)
        print(f'{href}を{save_dir}に保存しました')
        
if len(sys.argv) < 1:
    print('URLを入力してください')

link_search(' '.join(sys.argv[1:]))