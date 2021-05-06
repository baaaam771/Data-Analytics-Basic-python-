# Day_14_03_PythonWeather.py
import re
import requests


# url = 'https://www.naver.com/'
# url = 'https://movie.naver.com/'
url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=184'
received = requests.get(url)
# print(received, type(received))     # <Response [200]> <class 'requests.models.Response'>

data = received.text
# print(data)

# 문제
# city 태그 안에 포함된 지역 이름을 찾으세요
# temp = re.findall(r'<city>제주</city>', data)
# temp = re.findall(r'<city>..</city>', data)
# temp = re.findall(r'<city>...</city>', data)
# temp = re.findall(r'<city>.+</city>', data)
temp = re.findall(r'<city>(.+)</city>', data)
print(temp)

# <city>제주</city>
# <city>서귀포</city>
# <city>성산</city>
# <city>성판악</city>
