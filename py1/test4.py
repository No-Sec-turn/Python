# test4.py
# 리스트 list  [] 표현
a=[1,3,5,7,9]
b=['a','b','c']
c=[1,2,'a','b']
d=[]
print(a)
print(type(a))  #<class 'list'>
print(a[0]) #1
print(a[-1])  #9
print(a[0:2])  #[1, 3]

# 수정 변경
print(a)
a[2]=4
print(a)

a[1:2]=['a','b','c']
print(a)

pocket=['paper', 'phone','money']
if('money' in pocket):
    print("택시타고 가라")
else:
    print("걸어가라")
