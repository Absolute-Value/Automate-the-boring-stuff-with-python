#! /usr/bin/env python3
# 12.4_readCensusExcel.py - 群ごとに人口と人口調査標準地域の数を集計する

from itertools import count
from unittest import result
from numpy import result_type
import openpyxl, pprint

print('ワークブックを開いています...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
county_data = {}

# TODO: county_dataに群の人口と地域数を格納する
print('行を読み込んでいます...')
for row in range(2, sheet.max_row + 1):
    # スプレッドシートの1行に、ひとつの人口調査標準地域のデータがある
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # この州のキーが確実に存在するようにする
    county_data.setdefault(state, {})
    # この州のこの群のキーが確実に存在するようにする
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # 各行が人口調査標準調査地域を表すので、数を1つ増やす
    county_data[state][county]['tracts'] += 1
    # この人口調査地域の人口だけ群の人口を増やす
    county_data[state][county]['pop'] += int(pop)

# 新しいテキストファイルを開き、county_dataの内容を書き込む
print('結果を書き込み中...')
result_file = open('census2010.py', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()
print('完了')

import census2010
print(f"2010年のアンカレッジの人口は{census2010.all_data['AK']['Anchorage']['pop']}")