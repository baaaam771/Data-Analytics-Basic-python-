# Day_23_01_NumpyFinal.py
import numpy as np

a = np.arange(12) * 2
print(a)
print()

print(a[0], a[3], a[7])     # 0 6 14
b = [0, 3, 7]
print(a[b])                 # 인덱스 배열, [ 0  6 14]
print(a[[0, 3, 7]])
print()

c = [[2, 9], [3, 5]]
# print(a[c])               # 에러
d = np.int32(c)
print(a[d])                 # [[ 4 18] [ 6 10]]
print(a[d.reshape(-1)])
print(a[d.reshape(-1)].reshape(2, 2))
print('-' * 30)

e = a.reshape(3, 4)
print(e)
print()

print(e[0], e[2], e[1])
print(e[[0, 2, 1]])
print()

f = [[0, 1], [2, 3]]
# print(e[f])               # [ 4 14], deprecated
print(e[[0, 1], [2, 3]])    # [ 4 14], fancy indexing
print(e[(0, 1), (2, 3)])    # [ 4 14]
print()

# 팬시 인덱싱: 정수, 리스트(배열), 슬라이싱
print(e[0, (2, 3)])         # [4 6]
print(e[1:, (2, 3)])
print(e[1:, 2:])






