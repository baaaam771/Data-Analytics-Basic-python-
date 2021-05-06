# Day_16_01_sqlite.py
import sqlite3


# 문제
# weather.txt 파일을 읽어서 반환하는 함수를 만드세요
def read_weather():
    f = open('data/weather.txt', 'r', encoding='utf-8')

    rows = []
    for line in f:
        row = line.strip().split(',')
        # print(row)
        rows.append(row)

    f.close()
    return rows


rows = read_weather()
# print(rows)
# for r in rows:
#     print(r[5])
print(*rows, sep='\n')










