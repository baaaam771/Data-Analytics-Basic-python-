# Day_11_01_PythonQuiz.py

# 문제
# 100보다 작은 양수의 합계를 구하세요
# 1 2 3 ... 99
s = 0
for i in range(1, 100):
    # s = s + i
    s += i

print(s)

# 문제
# 아래처럼 출력하세요 (3가지)
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# 반복문: 0, 1, 2
# print('* * * * *\n* * * * *\n* * * * *\n* * * * *\n* * * * *\n')
# print('* * * * *\n' * 5)

# for _ in range(5):        # _: place holder
#     print('* * * * *')

# for _ in range(5):
#     print('* ' * 5)

# for i in range(5 * 5):
#     print('* ', end='')     # keyword argument
#
#     if i % 5 == 4:
#         print()

# for _ in range(5):
#     # print('* * * * *')
#
#     for _ in range(5):
#         print('* ', end='')
#     print()


def draw_stars():
    for _ in range(5):
        print('* ', end='')
    print()


for _ in range(5):
    draw_stars()


