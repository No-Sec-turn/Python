#test3.py
# 제어문 조건문 if  반복문 for while
a=True
print(a)
print(type(a))  #<class 'bool'>
a=False
# ==  !=  >  >=  < <=

# 점수가 60점 이상이면 "pass"출력 아니면 "재시험"
# if 조건:
#     조건 참 실행문
# else:
#     조건 거짓 실행문
a=85
if a>=60:
    print("pass")
else:
    print("재시험")

# 조건   숫자 0 아니면 True  0이면 False
#         문자열 "" 아니면 True ""이면 False
#         리스트 []아니면 True []이면 False
#         튜플 () 아니면 True ()이면 False
#          딕셔너리 {} 아니면 True {}이면 False

#카드가 있으면 "택시타라" 카드가 없으면 "걸어가라"
card=0
if card:
    print("택시타라")
else:
    print("걸어가라")

#논리연산자  and  or
#  나이가 10 ~ 19  "10대"  아니면 "10대 아님"
#  나이가 10보다 크거나 같고 19보다 작거나 같은 경우
age=20
if age>=10 and age<=19:
    print("10대")
else:
    print("10대 아님")

if 10<=age<=19:
    print("10대")
else:
    print("10대 아님")

a="901223-1234567"
# 주민번호 성별코드 "1"이거나 "3"이면 "남" 아니면 "여"
if a[7]=="1" or a[7]=="3":
    print("남")
else:
    print("여")

#다중 if    
# if 조건1:
#     조건1 참 실행문
# elif 조건2:
#     조건2 참 실행문
# else:
#     나머지 실행문

# a 변수 값이 양수, 영, 음수
a=-5
if a>0:
    print("양수")
elif a==0:
    print("영")
else:
    print("음수")