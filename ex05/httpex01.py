# python -m pip install requests

import requests

response = requests.get("http://apis.data.go.kr/1360000/TourStnInfoService/getCityTourClmIdx?serviceKey=dSHJNipMJz%2BPWTt9UN2qgExW7ql36lF%2BXp81YL%2FD42muatm7QP9jYJQSfIPMJ79C6NLitgJqd%2FGhRmY6U6YWwg%3D%3D&pageNo=1&numOfRows=10&dataType=JSON&CURRENT_DATE=2018123110&DAY=3&CITY_AREA_ID=5013000000")

print(response)

# dict response["키값"]
# class response.객체연결

print(type(response))
print(type(response.json()))
print(type(response.text))
print(response.status_code)

# print(response.json())
datas = response.json()["response"]["body"]["items"]["item"]

for data in datas:
    print(data["doName"])
