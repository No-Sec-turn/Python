# test23.py
# 데이터 시각화
# matplotlib 패키지 설치
# 선그래프 , 산점도, 막대그래프, 히스토그램, 파이그래프
import matplotlib.pyplot as plt
# 선그래프 : 순서가 있는 숫자(변하는 숫자) 데이터 시각화
data1=[10,14,19,20,25]
# plt.plot(data1)
# plt.show()
import numpy as np
x=np.arange(-4.5,4.5,0.5)    #(시작/끝/출력 범위)
y=2*x**2
y2=5*x+30
y3=4*x**2+10
# plt.plot(x,y)
# plt.plot(x,y2)
# plt.plot(x,y3)
# plt.show()

# plt.figure(1)
# plt.plot(x,y)
# plt.figure(2)
# plt.plot(x,y2)
# plt.figure(2)
# plt.clf()
# plt.plot(x,y3)
# plt.show()

# plt.subplot(2,2,1)
# plt.plot(x,y)
# plt.subplot(2,2,2)
# plt.plot(x,y2)
# plt.subplot(2,2,3)
# plt.plot(x,y3)
# plt.show()

# plt.plot(x,y)
# plt.plot(x,y2)
# plt.xlim(-4,-2)
# plt.ylim(10,20)
# plt.show()

#한글 처리
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 그래프 꾸미기
# b파란색 g녹색 r빨강 c청록 m자홍 y노랑 k검은 w흰색
# -실선 --파선  :점선   -. 파선 점선 혼합
# o 원모양 ^위쪽 V아래쪽  <왼쪽  >오른쪽
# s사각형  p오각형  h H육각형 * 별모양 +모양 x X모양 D d다이아몬드
# x=np.arange(0,5,1)
# y1=x
# y2=x+1
# y3=x+2
# y4=x+3
# plt.plot(x,y1,'>-r',x,y2,'s--b',x,y3,'d:y',x,y4,'X-.g')
# plt.xlabel('X축')
# plt.ylabel('y축')
# plt.title('제에목')
# plt.grid()   #격자 추가
# plt.legend(['data1','data2','data3','data4'],loc='upper right') #범례 loc(위치) lower : 아래 upper 위
# plt.text(2,2,'data1')
# plt.show()

# 산점도 : 두 요소 데이터 관계
height=[165,177,160,180,185]
weight=[62,67,55,74,90]
# plt.scatter(height,weight,s=500,c='r')
# plt.show()

# 히스토그램 : 정해진 간격 안에 데이터 개수 막대로 표시
math=[76,82,84,83,90,86,85,92,72,71,100,87,81,76,94,78,
      81,60,79,74,87,82,68,79]
# plt.hist(math,bins=8)
# plt.show()

# # 파이그래프 : 원그래프 원안에 각항목별로 비율만큼 영역 표시
# fruit=['사과','바나나','딸기','오렌지','포도']
# result=[7,6,3,2,2]
# plt.pie(result,labels=fruit)   #파이그래프 생성
# plt.savefig('pi.jpg')
# plt.show()

# 막대그래프 : 값 막대 높이, 여러항목 수량 비교
id=['m1','m2','m3','m4']
#x축 준비
num=len(id)
print(num) # 4
index=np.arange(num)  # 0 1 2 3

before_ex=[27,35,40,33] # 운동전 윗몸
after_ex=[30,38,42,37] # 운동후 윗몸 개수
plt.bar(index,before_ex,width=0.4,label='before',color='yellow') # x축 기준
plt.bar(index+0.4,after_ex,width=0.4,label='after',color='green') # x축 오른쪽
plt.xticks(index+0.2,id)
plt.legend()
plt.show()