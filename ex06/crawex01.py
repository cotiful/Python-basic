# 크롤링

# python -m pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

html = requests.get(
    "https://search.naver.com/search.naver?where=nexearch&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&ie=utf8&sm=tab_she&qdt=0")

soup = BeautifulSoup(html.text, 'html.parser')

weather_el = soup.select_one(".weather_graphic .temperature_text strong")

print(weather_el.get_text())
