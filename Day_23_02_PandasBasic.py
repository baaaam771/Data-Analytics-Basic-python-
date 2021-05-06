# Day_23_02_PandasBasic.py
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

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

