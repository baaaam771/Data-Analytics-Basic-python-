# Day_22_02_PandasBasic.py
import pandas as pd

# DataFrame: 테이블(표), 엑셀 시트
# Series: DataFrame 객체에서 컬럼을 담당하는 객체

a = pd.Series([5, 1, 2, 9])
print(a)
print()
# 0    5
# 1    1
# 2    2
# 3    9
# dtype: int64

print(a.index)              # RangeIndex(start=0, stop=4, step=1)
print(a.values)             # [5 1 2 9]
print(type(a.values))       # <class 'numpy.ndarray'>
print('-' * 30)

b = pd.Series([5, 1, 2, 9], index=['a', 'b', 'c', 'd'])
print(b)
print()
# a    5
# b    1
# c    2
# d    9
# dtype: int64

print(b.index)
print(b.values)
print()

# 문제
# 입력 데이터 중에서 처음에 있는 5만 가져오고 싶습니다 (3가지)
print(b['a'])
print(b[0])
print(b.values[0])
# print(b[-4])
# print(b.a)








