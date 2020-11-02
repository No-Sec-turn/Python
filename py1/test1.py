#test1.py
#주석 처리 cntl + / 한줄 주석
'''여러줄 주석'''
from builtins import print

""" 여러줄 주석"""
# 처음 파일 선택 alt + shift + F10
# 실행 shift f10


var = 7
print(type(var))    # <class 'float'>

var2 = "문자열"
print(type(var2))   # <class 'int'>

var = 3.4
print(type(var))    # <class 'float'>

# 자바와 달리 파이썬은 모든 자료형이 참조형임

#연산자
# + - * / **(제곱) //(몫) %(나머지

a=5/2
print(a)  # 2.5
a=5//2
print(a) # 2(몫만 출력)
a=2**3
print(a)  # 8

#연산자 우선순위
"""
1. 괄호
2. ** 제곱
3. - 음수
4. * / // %
5. + -  
"""



a= 1+2*3**2-5
print(a)


print('-------------------')

a=10
a=a+1
a += 1
print(a)

#여러변수 할당
a,b = 10,20
c = "10"
print("c=" + c)
print(b)

a=4/2
print(a) #2.0

#형변환
a=int(3.4)
print(a) #3 // int로 강제 형변환 했으므로..
a=float(3)
print(a) # 3.0 // float으로 강제 형변환



