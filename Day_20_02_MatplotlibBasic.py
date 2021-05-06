# Day_20_02_MatplotlibBasic.py
import matplotlib.pyplot as plt


# 문제
# 어제 수업했던 로그 그래프 4개를 그려보세요
import numpy as np


# 문제
# 2개의 피겨를 만들고
# 각각의 피겨를 4등분해서 각 피겨에 2개씩의 그래프를 그려주세요
def f_1():
    x = np.arange(0.01, 2.0, 0.01)

    plt.figure()
    plt.grid(True)

    plt.subplot(2, 2, 1)
    plt.plot(x, np.log(x))

    plt.subplot(2, 2, 3)
    plt.plot(x, -np.log(x))

    plt.figure()

    plt.subplot(131)
    plt.plot(-x, np.log(x))

    plt.subplot(3, 3, 6)
    plt.plot(-x, -np.log(x))

    plt.show()


# 문제
# 여성 데이터를 막대 그래프에 추가하세요
def f_2():
    men = [20, 35, 25, 30, 40]
    women = [15, 45, 35, 25, 40]

    indices = np.arange(len(men))

    # plt.bar(indices, men)
    plt.bar(indices, men, width=0.45, color='r', alpha=0.7)
    plt.bar(indices + 0.5, women, width=0.45, color='g', alpha=0.7)

    # 문제
    # 눈금이 가운데 오도록 수정하세요
    plt.xticks(indices + 0.5 / 2, ['A', 'B', 'C', 'D', 'E'])

    plt.show()


# 문제
# 2016_GDP.txt 파일을 읽어서 2차원 리스트를 반환하는 함수를 만드세요
def read_2016_gdp():
    f = open('data/2016_GDP.txt', 'r', encoding='utf-8')

    rows = []
    # 1번
    # for line in f:
    #     # print(line.strip().split(':'))
    #     rows.append(line.strip().split(':'))
    # rows.pop(0)

    # 2번
    # for i, line in enumerate(f):
    #     if i > 0:
    #         rows.append(line.strip().split(':'))

    # 3번
    # f.readline()        # skip header
    # for line in f:
    #     rows.append(line.strip().split(':'))

    f.readline()        # skip header
    for line in f:
        rank, name, dollar = line.strip().split(':')

        items = dollar.split(',')
        if len(items) == 2:
            dollar = items[0] + items[1]

        rows.append([name, int(dollar)])

    f.close()

    return rows


def f_3():
    gdp = read_2016_gdp()
    print(*gdp, sep='\n')


# f_1()
# f_2()
f_3()

