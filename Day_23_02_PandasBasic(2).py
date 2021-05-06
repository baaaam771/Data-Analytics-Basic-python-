# Day_23_02_PandasBasic.py
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors


def dataframe_plot():
    df = pd.DataFrame({
        'city': ['jeju', 'jeju', 'jeju', 'gunsan', 'gunsan', 'gunsan'],
        'year': [2018, 2019, 2020, 2018, 2019, 2020],
        'population': [300, 400, 350, 500, 550, 600],
    })

    # 문제
    # 제주는 왼쪽 플롯에, 군산은 오른쪽 플롯에 막대 그래프로 그려주세요
    # 막대 색상은 다르게, 플롯 위쪽에 도시 이름도 출력합니다

    plt.subplot(1, 2, 1)
    plt.title('jeju')
    plt.bar(range(3), df.population[:3], color=colors.TABLEAU_COLORS)
    plt.xticks(range(3), df.year[:3])
    plt.ylim(0, 700)

    plt.subplot(1, 2, 2)
    plt.title('gunsan')
    plt.bar(range(3), df.population[3:], color=colors.TABLEAU_COLORS)
    plt.xticks(range(3), df.year[3:])
    plt.ylim(0, 700)

    plt.show()


def dataframe_basic():
    df = pd.read_csv('data/scores.csv')
    print(df)
    print()

    # 정수 인덱스인 경우 loc와 iloc가 동일하다
    print(df.loc[2])
    print(df.iloc[2])
    print()

    print(df['kor'])
    print(df.kor)
    print('-' * 30)

    # 문제
    # 모든 학생의 점수 합계를 구하세요
    print(df.values[:, 2:].sum())
    print(sum(df.kor) + sum(df.eng) + sum(df.mat) + sum(df.bio))
    print(df.kor.values.sum() + df.eng.values.sum() + df.mat.values.sum() + df.bio.values.sum())
    print(df.kor.sum() + df.eng.sum() + df.mat.sum() + df.bio.sum())
    print(sum(df.kor + df.eng + df.mat + df.bio))
    print((df.kor + df.eng + df.mat + df.bio).sum())
    print()

    # print(df.columns)           # Index(['class', 'name', 'kor', 'eng', 'mat', 'bio'], dtype='object')
    # print(df.columns.values)    # ['class' 'name' 'kor' 'eng' 'mat' 'bio']

    subjects = ['kor', 'eng', 'mat', 'bio']
    # print(df[subjects])                   # 인덱스 배열
    # print(df[subjects].sum())
    # kor    933
    # eng    892
    # mat    936
    # bio    987
    # dtype: int64

    # print(df[subjects].sum(axis=0))     # 수직
    # print(df[subjects].sum(axis=1))     # 수평

    print(df[subjects].sum().sum())
    print(df[subjects].sum(axis=0).sum())
    print(df[subjects].sum(axis=1).sum())
    print('-' * 30)

    # 클래스와 이름을 덧셈
    # print(df.sum())

    # 문제
    # 과목별 평균과 학생별 평균을 구하세요
    df_temp = df[subjects]
    print(df_temp.sum(axis=0) / 12)
    print(df_temp.sum(axis=1) / 4)
    print()

    print(df_temp.shape)             # (12, 4)
    print(df_temp.values.shape)      # (12, 4)

    print(df_temp.sum(axis=0) / df_temp.shape[0])
    print(df_temp.sum(axis=1) / df_temp.shape[1])
    print()

    print(df[subjects].mean(axis=0))
    print(df[subjects].mean(axis=1))
    print('-' * 30)

    df['sum'] = df[subjects].sum(axis=1)
    df['avg'] = df[subjects].mean(axis=1)
    print(df)


# dataframe_plot()
dataframe_basic()
