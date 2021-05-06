# Day_22_01_NumpyFinal.py
import numpy as np


a = np.arange(6).reshape(2, 3)
b = np.arange(6, 12).reshape(2, 3)

print(a)        # [[ 0  1  2] [ 3  4  5]]
print(b)        # [[ 6  7  8] [ 9 10 11]]
print()

print(np.concatenate([a, b]))
print(np.concatenate([a, b], axis=0))   # (4, 3)
print(np.concatenate([a, b], axis=1))   # (2, 6)
print()

print(np.vstack([a, b]))                # (4, 3) v: vertical
print(np.hstack([a, b]))                # (2, 6) h: horizontal
print('-' * 30)

c = np.arange(12).reshape(3, 4)
print(c)

print(np.transpose(c))                  # 전치 행렬
print(c.transpose())
print(c.T)
print()

# 행렬 곱셉(점곰 연산, point-wise 곱셈)
print(np.dot(c, c.T))                   # (3, 4) @ (4, 3) = (3, 3)
print(np.dot(c.T, c))                   # (4, 3) @ (3, 4) = (4, 4)
print('-' * 30)

# 문제
# 2차원 배열을 반복문을 사용해서 행과 열이 바뀐(전치) 형태로 출력하세요
for j in range(4):
    for i in range(3):
        print(c[i, j], end=' ')
    print()
print()

for j in range(c.shape[1]):
    for i in range(c.shape[0]):
        print(c[i, j], end=' ')
    print()
print()

for j in range(c.shape[-1]):
    print(c[:, j])
print('-' * 30)

# 문제
# 테두리는 1로, 속은 0으로 채워진 5x5 배열을 만드세요 (zeros 함수 사용)
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
d = np.zeros([5, 5], dtype=np.int32)

# 1번
for i in range(5):
    d[0, i] = 1
    d[4, i] = 1
    d[i, 0] = 1
    d[i, 4] = 1

# 2번
# d[0, 0], d[0, 1], d[0, 2], d[0, 3], d[0, 4] : d[0, :]
# d[0, :] = 2
# d[4, :] = 2
d[0] = 2
d[4] = 2
d[:, 0] = 2
d[:, 4] = 2

print(d)





print('\n\n\n\n\n\n\n')