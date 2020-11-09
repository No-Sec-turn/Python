#반복문 while for

#초기값
#while 조건:
#   반복실행문
#   초기값 1증가

#1~10 출력
i=1
while i<=10:
    print(i, end =" " )
    i += 1
print()
#list while
li = [85, 95, 90, 80, 75]
# print(li[0])
# print(li[1])
# print(li[2])
# print(li[3])
# print(li[4])
i=0
while i<len(li):
    print(li[i])
    i += 1

#=====================
print("====================")
li2 = [85,90,80,75,95]
sum=0

for i in  li2:  #list 안의 값이 i에 하나씩 담기고, 1씩 증가함
    print(i)
    sum += i
    print(sum)

a = "문자열"
print("항목 개수: ", len(li2))  # "," 가 연결자 "+"는 연산자
print(len(li2))
print("점수 합계: ", sum)
# print(sum)
print("점수 평균: ")
print(sum/len(li2))

s="hello"
for a in s:
    print(a)

li3 = [85,25,80,45,95]
# 60점 이상이면 합격 아니면 불합격
# 90점은 합격
# 25점 불합격
for a in li3:
    if(a>=60):
        b = "합격"
    else:
        b = "불합격"
    print(a, "는", b )

# range (시작번호, 끝번호, 증가값)
for i in range(1,11,1):
    print(i)

# 2 4 6 8 10 출력
for i in range(2,11,2):
    print(i, end=" ")

#2단
for i in range(1,10,1):
    print("%d*%d=%d" % (2,i,2*i))


#구구단
for i in range(2,10,1):
    print(i,"단")
    for j in range(1,9,1):
        # print(i,"*",j,"=",i*j)
        # , 로 구분해서 쓰면 자동으로 공백이 적용됨!
        print("%d*%d=%d" % (i,j,i*j))

print("====")

# 한줄 반복문, 조건문, 함수(람다함수)
li4 = [1,2,3,4]
li5 = []
for i in range(0,len(li4),1):
    li5.append(li4[i] * 3)
print(li5)

# 한줄 반복문, 조건문,  함수(람다함수)
#  새로운 리스트 저장 =리스트안 내용에 * 3
# 리스트 추가
# a=[1,2,3]
# a.append(4)
li4=[1,2,3,4]
li5=[]
for i in li4:
    li5.append(i*3)
print(li5)

# 한줄 for  [실행 for 변수 in 리스트 if 조건 ]
# for동작 if 참이면 실행문 => 결과 리스트
li6=[i*3 for i in li4]
print(li6)
# li4에서 짝수이면 i*3 => 결과 리스트에 저장
li7=[i*3 for i in li4 if i%2==0]
print(li7)
# [실행 for 변수1 in 리스트1 for 변수2 in 리스트2]
# 구구단의 결과 값을 리스트 저장
li8=[dan*i for dan in range(2,10) for i in range(1,10)]
print(li8)
# [실행 for 변수1 in 리스트1 if 조건1 for 변수2 in 리스트2 if 조건2]




