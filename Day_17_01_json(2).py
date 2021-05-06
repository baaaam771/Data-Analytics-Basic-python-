# Day_17_01_json.py
import json
import requests


# 데이터 교환 형식: json, xml(html), yaml
# save: 메모리(단기 기억장치)에 있는 내용을 파일(영구 기억장치)에 쓰기
# load: 파일(영구 기억장치)에 있는 내용을 메모리(단기 기억장치)에 쓰기

t1 = '{"ip": "8.8.8.8"}'
print(type(t1))             # <class 'str'>

j1 = json.loads(t1)
print(j1)
print(type(j1))
print(j1['ip'])

print('-' * 30)

# 문제
# 아래 데이터를 json을 사용해서 문자열 형태로 변환하세요
t2 = {"ip": "8.8.8.8"}
print(type(t2))             # <class 'dict'>

j2 = json.dumps(t2)
print(j2)
print(type(j2))

print('-' * 30)

# 문제
# 아래 데이터로부터 key와 value를 뽑아서 출력하세요
date_and_time = '''{
   "time": "03:53:25 AM",
   "milliseconds_since_epoch": 1362196405309,
   "date": "03-02-2013"
}'''

j3 = json.loads(date_and_time)
print(j3)

for k in j3:
    print(k, j3[k])

print('-' * 30)

url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
received = requests.get(url)
print(received)
print(received.text)
print(received.content)
print(type(received.text))      # <class 'str'>
print(type(received.content))   # <class 'bytes'>

print('\xec :', 16 * 14 + 12)
# \xec

text = received.content.decode('utf-8')
print(text)
print(type(text))               # <class 'str'>

# 문제
# 기상청에서 가져온 지역 코드를 깔끔하게 출력하세요 (json)
# 11 서울특별시
# 26 부산광역시

data = json.loads(text)
print(data)
print(type(data))

for item in data:
    # print(type(item), item)
    # for k in item:
    #     print(item[k], end=' ')
    # print()

    print(item['code'], item['value'])


