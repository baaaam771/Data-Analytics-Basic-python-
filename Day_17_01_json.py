# Day_17_01_json.py
import json

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






