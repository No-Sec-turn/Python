# test7.py
# def 함수이름():
#   실행문
#   return


def sum(a,b):
    return a+b

print(sum(10,20))
print(sum(10,20)/2)

# def sum2(list):
#     return size(list)

def sum2(e1):
    s=0
    for a in e1:
        s=s+a
    return s


eng=[90,80,70,60,50]


print("-----------")
print(sum2(eng))
print(sum2(eng)/5)

# 최대값 구하는 함수 max2() 리스트를 받아서 가장 큰값을 받아서 리턴
def max2(e1):
    m=0 #최대값 저장하는 변수
    for a in (e1):
        if m<a:
            m = a
    return m
print(max2((eng)))


# *변수 : 리스트 변수
def sum_many(*li):
    ss=0
    for a in li:
        ss=ss+a
    return ss


print("======-----")
print(sum_many(1,2,3))
print(sum_many(1,2,3,4,5,6))
print(sum_many(1,2,3,4,5,6,7,8,9,10))

def my(name,old,man=True):
    print(name,old,man)

my("홍길동",21,True)
my("이순신",33)
my("유관순",17,False)

# 람다 함수 lambda() 한줄 함수 정의
# 함수이름 = lambda 받는변수1, 변수2 : 변수1 + 변수2
# def sum(a,b):
#   return a+b  를 한줄로 바꾼 것
sum = lambda a,b:a+b
print(sum(10,20))

# a,b 두수를 받앗 a**b square 함수
squre = lambda  a,b:a**b
print(squre(4,2))

#리스트 안에 람다함수

mylist = [lambda a,b:a+b, lambda a,b:a**b]
print(mylist[0](10,20))
print(mylist[1](2,3))

#map() 리스트 람다함수 접목
#하나를 받아서 *2를 하고 싶다

two2 = lambda a:a*2
print("람다")
print(two2(2))

# [1,2,3,4] =>람다함수 => [2,4,6,8]
li = [1,2,3,4]
#li2 =list(map(two2,li))   # 리스트로 형변환 -> map함수(생성한함수, 넣을 값)
li2 = list(map(lambda a:a*2, li))
print(li2)

# 리스트 = list(filter(람다함수,리스트))
li3 = list(filter(lambda a:a>0,[1,3,2,0,-5,6]))
print(li3)
#map() filter() 내장함수
print("절대값", abs(-5))
print("몫나머지", divmod(9,4))
print("정렬", sorted([3,1,2]))