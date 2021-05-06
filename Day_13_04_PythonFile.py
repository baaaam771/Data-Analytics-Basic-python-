# Day_13_04_PythonFile.py

# f = open('./data/poem.txt')
# f = open('data\\poem.txt')        # 윈도우 전용
f = open('data/poem.txt', 'r', encoding='utf-8')     # euc-kr

lines = f.readlines()
print(lines)

f.close()





