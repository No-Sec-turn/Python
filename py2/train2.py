import pandas as pd

# 데이터프레임 , 데이터프레임 합치기
df1=pd.DataFrame({'1반':[95,92,98,100],
                  '2반':[91,93,97,99]})
print(df1)

df2=pd.DataFrame({'1반':[87,89],
                  '2반':[85,90]})
print(df2)

# 행추가
print(df1.append(df2))
print(df1.append(df2,ignore_index=True))

# 열추가
df3=pd.DataFrame({'3반':[90,96,88,80]})
print(df3)
print(df1.join(df3))

#통합 merge()

df4=pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                 '제품A':[95,92,98,100],
                 '제품B':[91,93,97,99]})

df5=pd.DataFrame({'판매월':['5월','6월','3월','4월'],
                 '제품C':[90,96,88,80],
                 '제품D':[98,95,92,99]})
print("================df4========================")
print(df4)
print("================df5========================")
print(df5)

#df4 기준을 잡고 추가되는 df5 중 겹치는 column만 입력 받고 없는 것은 NaN 처리 후 merge
# print(df4.merge(df5,how='left'))

#df5 기준을 잡고 추가되는 df4 중 겹치는 column만 입력 받고 없는 것은 NaN 처리 후 merge
# print(df4.merge(df5,how='right'))

#모든 컬럼을 다 포함시켜 merge
# print(df4.merge(df5,how='outer'))

#겹치는 컬럼만 merge 해서 출력
# print(df4.merge(df5,how='inner'))

#isna() 메서드 => NaN 값은 True로 처리, 값이 있으면 False로 출력

# fillna(value) : NaN 값을 value 값으로 대체

df6=df4.merge(df5,how='left')
print(df6)

# # 이상한데이터(이상치)=>결손데이터(결측치) => 처리(0,평균)
# #  결손데이터 NA, NaN  isna() 비어있는 데이터 찾기
print(df6.isna())  #True
print(df6.isna().sum())
print(df6.mean())
# #  결손데이터 다른것으로 대치 fillna()
print(df6['제품C'].fillna(0))
print(df6['제품C'].fillna(df6['제품C'].mean()))

# apply()  lamba
print(df6)
# 제품A100   =   제품A *100
df6['제품A100']=df6['제품A'].apply(lambda x:x*100)
print(df6)     # lambda x :참값  if 조건 else 거짓값
# 제품Agrade = 제품A  100이상이면 'A' else 'B'
df6['제품Agrade']=df6['제품A'].apply(lambda x:'A'if x>=100 else 'B')
print(df6)
