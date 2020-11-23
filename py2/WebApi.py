# test25.py
# 웹API 데이터 추출
# 날씨 정보, 상품 데이터, 주가, 환율 => 웹API제공
# 웹API : 사이트가 가지고 있는 기능을 외부에서도 쉽게
#         사용할수 있게 공개
# 사이트 웹 API 요청 : xml, JSON

# OpenWeatherMap날씨 정보 제공
# https://openweathermap.org/

import requests
import json

# API키
# apikey="474d59dd890c4108f62f192e0c6fce01"
# api="http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
# url=api.format(city="Beijing,CN",key=apikey)
# print(url)
# r=requests.get(url)
# # print(r.text)
# data=json.loads(r.text)
# print(data['name'])  # dictionary 안에 "name" 의 값 출력
# print(data['weather'][0]['description'])  # weather 키 안의 0번째의 description 값

# http://data.go.kr  -> 공공데이터 포털
#https://kosis.kr/index/index.do -> 국가통계포털
# http://data.oecd.org/waste/municipal-waste.htm -> OECD데이터

# http://data.seoul.go.kr -> 서울 열린데이터 광장
# http://data.ex.co.kr -> 한국 도로교통공사
# # http://taas.koroad.or.kr -> 교통사고 분석 시스템
# # http://data.kma.go.kr/cmmn/main.do -> 기상청
# http://www.kofic.or.kr/kofic/business/main/main.do -> 영화진흥위원회
