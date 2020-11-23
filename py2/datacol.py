#requests, BeautifulSoup4, lxml 설치

import requests  # 웹페이지에 있는 HTML 코드 가져오기
r = requests.get("https://www.google.com/").text
# print(r)


from bs4 import BeautifulSoup
soup=BeautifulSoup(r,'lxml')
# .find('태그') -> 1개   find_all('태그전체') -> 전체   -> xml에서 많이 쓰임

# select('태그 클래스이름 아이디이름') -> 전체 찾는 방법
# select_one('태그 클래스이름 아이디이름') -> 1개 찾는법


# print(soup.find('a'))
# print(soup.find_all('a'))    # 전체 => 리턴타입: 리스트형
# ali=soup.find_all('a')
#
# for i in ali:
#     print(i)

# print(soup.select('body img')) #리턴 타입: 리스트
# ise = soup.select('body img')
#
# for i in ise:
#     print(i)

# https://movie.naver.com/movie/sdb/rank/rmovie.nhn
# 네이버 영화 순위   영화명 a
# r=requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn").text
# soup=BeautifulSoup(r,'lxml')
# ali=soup.select('tr td.title div.tit3 a')   #html 구조 파악해서 접근
# # print(ali)
# for i in ali:
#     # print(i)
#     # print(i.attrs['href'])
#     # print(i.attrs['title'])
#     print(i.string)

#xml 데이터 날씨 xml 제공

#http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108

# url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
import urllib.request as req
# req.urlretrieve(url,"forecast.xml")
#
# #파일 => xml 읽기
# xml=open("forecast.xml","r",encoding="utf-8").read()
# # print(xml)
# soup=BeautifulSoup(xml, "html.parser")  #BeautifulSoup에서 xml 파일 읽어오기
# li = soup.find_all("location")
# for i in li:
#     print(i.find('city').string)      #구조를보고 find를쓸지 find_all 을 쓸지 결정!
#     print(i.find('wf').string)

#JSON   https://api.github.com/repositories
# url = "https://api.github.com/repositories"
# req.urlretrieve(url,"repo.json")
# import json
# itemjson=json.load(open("repo.json","r",encoding="utf-8"))
# # print(itemjson)
# # 리스트 딕셔너리  키 name   owner login
# for i in itemjson:
#     print(i['name']+"-"+i['owner']['login'])






