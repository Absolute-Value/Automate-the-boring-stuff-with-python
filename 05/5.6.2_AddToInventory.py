#! /usr/bin/env python3
# 5.6.2 ファンタジーゲームの持ち物リスト用にリストから辞書に移す関数

def display_inventory(inventory):
    print("持ち物リスト")
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print("アイテム総数：" + str(item_total))

def add_to_intentory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

inv = {'金貨': 42, 'ロープ': 1}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']
inv = add_to_intentory(inv, dragon_loot)
display_inventory(inv)