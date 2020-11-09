# test5.py
# 딕셔너리 자료형  사전   단어:뜻   키:값
#  {키1:값1,키2:값2}
# JSON데이터 형태 리스트[딕셔너리,딕셔너리]
# [
# {"id":"kim","pass":"p123"},
# {"id":"lee","pass":"p345"}
# ]
d={"id":"kim","pass":"p123"}
print(d)  #{'id': 'kim', 'pass': 'p123'}
print(type(d))  #<class 'dict'>
print(d["id"])  # kim
print(d['pass'])  #p123
# 값 추가
d['name']="kimgildong"
print(d) #{'id': 'kim', 'pass': 'p123', 'name': 'kimgildong'}
d[1]='a'
print(d)
#{'id': 'kim', 'pass': 'p123', 'name': 'kimgildong', 1: 'a'}
# 삭제
del(d[1])  # 1키에 해당하는 값 삭제
print(d)
#{'id': 'kim', 'pass': 'p123', 'name': 'kimgildong'}

# 딕셔너리 클래스 함수(메서드)
print(d.keys()) #dict_keys(['id', 'pass', 'name'])
print(type(d.keys()))  #<class 'dict_keys'>
a=list(d.keys())  # list형으로 형변환
print(a)  #['id', 'pass', 'name']
print(type(a))  #<class 'list'>

print(d.values()) #dict_values(['kim', 'p123', 'kimgildong'])
print(d.items())
#dict_items([('id', 'kim'), ('pass', 'p123'), ('name', 'kimgildong')])
print(type(d.items()))  #<class 'dict_items'>
a=list(d.items())
print(type(a)) #<class 'list'>
print(a)
#[('id', 'kim'), ('pass', 'p123'), ('name', 'kimgildong')]
print(type(a[0])) #<class 'tuple'>
print(a[0])  #('id', 'kim')

print(d['id'])  #kim
print(d.get('id')) #kim

#전체 삭제
d.clear()
print(d) #{}

# 집합 자료형
# set : 순서없음, 중복허용하지 않음
s1=set([1,2,3,2])
print(s1)  #{1, 2, 3}

s2=set("Hello")
print(s2)  #{'e', 'l', 'H', 'o'}
print(type(s2))  #<class 'set'>

# 차집합, 교집합, 합집합
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
#교집합
print(s1&s2)  #{4, 5, 6}
print(s1.intersection(s2))
#합집합
print(s1|s2)  #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))
#차집합
print(s1-s2)
print(s1.difference(s2))

#추가
s1=set([1,2,3])
s1.add(4)
print(s1)
s1.update([5,6])   # 여러개 추가 할때는 update
print(s1)
print("======")
s1.remove(2)
print(s1)

# 참조 자료형
a=3
b=3
c=3
#변수들의 주소 값
print(id(a))
print(id(b))
print(id(c))
print(a is b)


a,b=('a','b')
a,b=10,20
print(a)
print(b)

#변수값 교환 -> 참조형이기 떄문에 가능 -> 원래 값이 아니라 주소값을 갖고 있으므로 주소값을 교환하는 의미..
a,b=b,a
print(a)
print(b)
print("---------------")

# 변수 메모리 삭제
a=3
b=3
del(a)
# print(a) #name 'a' is not defined  메모리까지 완전 삭제 된것

# 리스트 변수 복사
a = [1,2,3]
b=a # 주소 복사
a[1] = 4
print(id(a))
print(a) #[1, 4, 3]
print(id(b))
print(b) #[1, 4, 3]

#리스트 변수 값 복사
a=[1,2,3]
b=a[:] # 값
a[1] = 4
print(a)
print(id(a))
print(b)
print(id(b))

#리스트 변수 값 복사 copy()함수
from copy import copy
a=[1,2,3]
b=copy(a)
a[1] =4
print(a)
print(id(a))
print(b)
print(id(b))

#모든 파이썬의 변수는 참조형이다!!