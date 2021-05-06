# Day_18_02_ReLibrary.py
import requests
import re


# 문제
# 수지도서관 제1열람실의 빈 좌석 갯수를 알려주세요
url = 'http://211.251.214.168:8080/seatmate_sj/seatmate.php?classInfo=1'

received = requests.get(url)
text = received.content.decode('euc-kr')
# print(text)

# empty = re.findall(r'<li class='txt4'>14 </li>', text)        # 작은 따옴표 때문에 에러
empty = re.findall(r"<li class='txt4'>([0-9]+) </li>", text)
print('빈 좌석 갯수 :', int(empty[0]))
