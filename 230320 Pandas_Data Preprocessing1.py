#!/usr/bin/env python
# coding: utf-8

# # 데이터 전처리 연습

# In[65]:


import pandas as pd
import seaborn as sns
import numpy as np


# ### Titanic 데이터

# In[26]:


df = sns.load_dataset('titanic')


# In[5]:


df.head()      # deck: 선실번호 첫 알파벳
# https://bskyvision.com/entry/python-seaborn-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%EA%B0%80-%EC%A0%9C%EA%B3%B5%ED%95%98%EB%8A%94-%ED%83%80%EC%9D%B4%ED%83%80%EB%8B%89-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B-%EC%84%A4%EB%AA%85


# ## 결측치 처리

# In[17]:


# nan값 조회
df.isnull().sum()  # 데이터 너무 많으니까 sum으로 조회


# In[6]:


df['deck'].unique()


# In[7]:


# deck열의 Nan 갯수 계산기
nan_deck = df['deck'].value_counts(dropna = False)
print(nan_deck)


# In[9]:


df.notnull().sum()   # null이 아닌 데이터 갯수 합


# In[10]:


df.notnull().sum(axis = 1)


# In[19]:


# for 반복문으로 각 열 NaN 갯수 게산

missing_df = df.isnull()
missing_df['pclass'].value_counts()


# In[14]:


for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()
    try:
        print(col, ':', missing_count[True])   # nan값이 있으면 갯수 출력
    except:
        print(col, ':', missing_count[0])    # nan값이 있으면 0 출력


# In[18]:


df.isnull().sum()


# In[28]:


# Nan값이 500개 이상인 열을 모두 삭제 : deck열을 삭제

df_tresh = df.dropna(axis = 1, thresh = 500, inplace = True)    # dropna 하나만 없어도 삭제함. thresh값을 주어야함
print(len(df.columns))   # 15개 col 중에서 deck 하나 사라졌는지 확인


# In[29]:


# age 열, 데이터가 없는 모든 행을 삭제
df_age = df.dropna(subset = ['age'], how = 'any', axis = 0)
df_age


# In[31]:


df.isnull().sum()


# In[32]:


# age 데이터가 많이 없음. 버리긴 아까우니 age열의 nan값을 다른 나이 데이터의 평균으로 변경해봄
# 평균값으로 넣어주면, 평균 자체에는 영향이 없음
mean_age = df['age'].mean(axis = 0)    # mean함수는, Nan값 제외하고 계산해줌
df['age'].fillna(mean_age, inplace = True)


# In[34]:


df.isnull().sum()


# In[35]:


df.info()


# In[37]:


# embark_town(승선지) 결측치 채우기
# 최빈값으로 : 가장 많이 출연한 값
most_freq = df['embark_town'].value_counts()
most_freq


# In[38]:


most_freq_one = df['embark_town'].value_counts(dropna = True).idxmax()
print(most_freq_one)


# In[41]:


df['embark_town'].fillna(most_freq_one, inplace = True)
df.isnull().sum()


# In[ ]:


# 데이터를 일부 구역으로 구분해서 최빈값 넣어주기   
# 가능하지만, 왜 이렇게 했는지 명확한 근거가 필요함
# 코드는 아래와 같음
most_freq_one_sep = df['embark_town'][825:].value_counts(dropna = True).idxmax()
df['embark_town'].fillna(most_freq_one_sep, inplace = True)    


# In[42]:


# embarked 열의 Nan값을 바로 앞의 값으로 변경하기
df['embarked'].fillna(method = 'ffill', inplace = True)
df.isnull().sum()


# ## 중복값 처리

# In[46]:


# 중복 데이터를 갖는 데이터 찾기

df2 = pd.DataFrame({'c1':['a','a','b','a','b'],
                   'c2':[1,1,1,2,2],
                   'c3':[1,1,2,2,2]})
df2


# In[47]:


df2_dup = df2.duplicated()
df2_dup


# In[49]:


# 데이터프레임의 특정 열에서 데이터 중복값 찾기
col_dup = df2['c2'].duplicated()
col_dup


# In[50]:


# 중복된 데이터 삭제 (중복 행 제거)
df3 = df2.drop_duplicates()
df3


# In[51]:


# c2, c3열을 기준으로 중복 행 제거
df4 = df2.drop_duplicates(subset = ['c2','c3'])
df4


# ## 값 변환하기 conversion

# In[53]:


# mpg data: Mile Per Gallon

auto = pd.read_csv('./Data/auto-mpg.csv', header = None)
auto.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']
auto.head()


# In[54]:


auto.info()


# In[57]:


auto.isnull().sum()


# #### 파생변수 컬럼 만들기

# In[59]:


# Mile per Gallon을 Kilometer per Liter로 변경
# 1 mpg = 0.425 kpl   ( 3.78541 mpg = 1.60934 kpl )
auto['kpl'] = auto['mpg'] * 0.425
auto.head()


# #### 반올림

# In[61]:


# kpl열을 소수점 아래 둘째자리 반올림
auto['kpl'] = auto['kpl'].round(2)
auto.head(3)


# #### 열 데이터타입 변경

# In[62]:


auto.info()


# In[68]:


auto.isnull().sum()


# In[63]:


# 각 열의 자료형 확인
auto.dtypes


# In[64]:


# horsepower 열의 고유값
auto['horsepower'].unique()


# #### 누락데이터 ('?') 삭제

# In[67]:


# 삭제하려면 Nan값이 필요함
auto['horsepower'].replace('?',np.nan, inplace = True)
auto.isnull().sum()


# In[69]:


auto.dropna(subset = ['horsepower'], axis = 0, inplace = True)     # subset안써줘도 되지만, horsepower 기준으로 빼라고 확인
auto.isnull().sum()


# In[70]:


auto.info()


# In[74]:


# horsepower 데이터타입 float로 변경
auto['horsepower'] = auto['horsepower'].astype('float')
auto.info()


# In[75]:


# origin열의 고유값 확인
auto['origin'].unique()


# In[76]:


auto['origin'].replace({1:'USA', 2:'EU', 3:'JAP'}, inplace= True)
auto['origin'].unique()


# In[79]:


print(auto['origin'].dtypes)


# In[80]:


# origin의 문자열 자료형을 범주형 자료형으로 변환
auto['origin'] = auto['origin'].astype('category')
auto['origin'].dtypes


# In[81]:


auto.info()


# In[84]:


# model year, 정수형에서 범주형으로 변환
auto['model year'].head(3)


# In[85]:


auto['model year'].sample(3)


# In[86]:


auto['model year'].unique()


# In[87]:


auto['model year'] = auto['model year'].astype('category')
auto['model year'].sample(3)


# #### 데이터를 Category형으로 나누기

# In[89]:


# horsepower를 3개 등급으로 나누기
# np.histogram 함수로 3개의 bin으로 나누는 경계값 리스트 구하기
count, bin_dividers = np.histogram(auto['horsepower'], bins= 3)
bin_dividers


# In[91]:


auto['horsepower'].describe()


# In[96]:


# 3개의 bins에 이름 지정
bin_name = ['low power', 'mid power', 'high power']

# cut 함수로 각 데이터 쪼개기
auto['hp_bin'] = pd.cut(x = auto['horsepower'],
                        bins = bin_dividers,    # 경계선 값 리스트
                        labels = bin_name,      # 각 구간 이름
                        include_lowest = True   # 첫 경계선값 포함하는 것으로 함
                        )
auto[['horsepower','hp_bin']].head(10)

