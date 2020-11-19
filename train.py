import pandas as pd
from numpy.distutils.system_info import agg2_info

print("------------------------------------------------------------------------------------")
# 타이타닉 실제 데이터 => 데이터 파악
#train.csv 파일 읽어 오기
train = pd.read_csv("train.csv")   # 변수명 = pandas.read_csv("파일이름.csv")


pd.set_option('display.max_rows',5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 1000)
print(train)
#컬럼분석
# PassengerID: 승선 번호, Survived: 생존 여부

#상위 데이터 10개
# print(train.head(10))
#하위 데이터 10개
# print(train.tail(10))

#열의 합계
print("=====================열의 합계=======================")
# print(train.sum)
#열 평균
print("=====================열의 평균=======================")
# print(train.mean)

#통계치
# print(train.describe())
#count = 컬럼별 데이터 갯수
#mean = 평균
#std = 표준 편차
#min = 최소값
#25% = 하위 25%값
#50% = 중위 값
#75% = 상위 75% 값
#max = 최대값




# print(train[1:10])
# print(train['Survived'])   # 생존한 사람 출력
# print(train[['Survived','Age']])  # Age 20보다 작은 경우
# print(train['Survived'][1:3])
#
#
# print(train[train['Survived']==1]) #생존한 사람 출력
# print(train[train['Age']<20]['Age'])  #Age 20보다 작은 경우
# print(train.sort_values(by=["Pclass"]))#오름차순 조회
# print(train.sort_values(by=["Pclass"],ascending=False))   # Pclass  내림차순 조회

#Pclass 그룹 각 값별 갯수  #count(self,level)
# print(train.groupby(by='Pclass').count())


#각 Pclass 그룹별 생존자 수
# print(train.groupby(by='Pclass')['Survived'].agg(sum))


# print(train.groupby(by="Pclass")['Age'].min())
#Pclass 그룹 Age min  maxmin())
# print(train.groupby(by="Pclass")['Age'].max())
#sex 그룹 Survived sum Age mean
# print(train.groupby(by='sex')['Age'].mean())
# print(train.groupby(by='sex')['Age'].sum())

# agg_format={'Survived':'sum','Age':'mean'}
# train_g4=train.groupby(by='Sex').agg(agg_format)
# print(train_g4)

#이상한 데이터(이상치) => 결손데이터(결측치) => 처리(0,평균)  이상한 데이터: 데이터 범위로 설정된 값보다 벗어난 경우
# 결손 데이터 NA isna() 비어있는 데이터 찾기

df1=pd.DataFrame({'1반':[95,92,98,100],
            '2반': [85,90]  })

print(df1)







# def pie_chart(feature):
#     feature_ratio = train[feature].value_counts(sort=False)
#     feature_size = feature_ratio.size
#     feature_index = feature_ratio.index
#     survived = train[train['Survived'] == 1][feature].value_counts()
#     dead = train[train['Survived'] == 0][feature].value_counts()
#
#     import matplotlib.pyplot as plt
#     plt.plot(aspect='auto')
#     plt.pie(feature_ratio, labels=feature_index, autopct='%1.1f%%')
#     plt.title(feature + '\'s ratio in total')
#     plt.show()
#
#     for i, index in enumerate(feature_index):
#         plt.subplot(1, feature_size + 1, i + 1, aspect='equal')
#         plt.pie([survived[index], dead[index]], labels=['Survivied', 'Dead'], autopct='%1.1f%%')
#         plt.title(str(index) + '\'s ratio')
#
#     plt.show()
#
#     pie_chart('Sex')