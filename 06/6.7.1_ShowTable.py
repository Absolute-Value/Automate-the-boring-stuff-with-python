#! /usr/bin/env python3
# 6.7.1 表の表示

def print_table(table_data):
    col_widths = [0] * len(table_data)
    for i, datas in enumerate(table_data):
        for data in datas:
            length = len(data)
            if length > col_widths[i]:
                col_widths[i] = length
                
    for i in range(len(table_data[0])):
        for j in range(len(table_data)):
            print(table_data[j][i].rjust(col_widths[j]), end='')
            print(' ',end='')
        print('')

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
print_table(table_data)