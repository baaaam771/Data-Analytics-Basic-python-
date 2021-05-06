# Day_19_01_NumpyAdvanced.py
import numpy as np

# scalar + scalar : 3 + 7
# scalar + array  : 3 + [1, 3]          broadcast
# array  + array  : [1, 3] + [2, 5]     vector

a = np.arange(3)      # (1, 3)      # [0, 1, 2]
b = np.arange(6)      # (1, 6)      # [0, 1, 2, 3, 4, 5]
c = np.arange(3).reshape(1, 3)      # [[0, 1, 2]]
d = np.arange(6).reshape(2, 3)      # [[0, 1, 2], [3, 4, 5]]
e = np.arange(3).reshape(3, 1)      # [[0], [1], [2]]

# print(a + b)          # 에러
print(a + c)            # scalar + vector
print((a + c).shape)    # (1, 3)
print(a + d)            # broadcast + vector
print((a + d).shape)    # (2, 3)
print(a + e)            # broadcast + broadcast

# 문제
# 나머지 변수들에 대해서도 연산이 성립하는지 확인하세요 (6개의 연산)
# print(b + c)          # 에러
# print(b + d)          # 에러
print(b + e)            # broadcast + broadcast
print((b + e).shape)    # (3, 6)

print(c + d)            # broadcast + vector
print((c + d).shape)    # (2, 3)

print(d + e)


