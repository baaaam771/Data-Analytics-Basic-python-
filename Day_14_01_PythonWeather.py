# Day_14_01_PythonWeather.py
import re
import requests

url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=184'
received = requests.get(url)
# print(received)                 # <Response [200]>
# print(type(received))           # <class 'requests.models.Response'>

data = received.text
# print(data)
# print(type(data))               # <class 'str'>

# 문제
# city 태그 안쪽의 지역을 찾아주세요
# temp = re.findall(r'<city>제주</city>', data)
# temp = re.findall(r'<city>..</city>', data)
# temp = re.findall(r'<city>..</city>', data)
# temp = re.findall(r'<city>...</city>', data)
temp = re.findall(r'<city>.+</city>', data)
print(temp)
temp = re.findall(r'<city>(.+)</city>', data)
print(temp)

# <city>.+</city>
# <city>제주</city>
# <city>서귀포</city>
# <city>성산</city>
# <city>성판악</city>
# <city>고산</city>
# <city>이어도</city>
# <city>추자도</city>




