#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np


# ### 원핫인코딩 예시

# In[64]:


from sklearn import preprocessing


# In[65]:


# 전처리를 위한 encoder객체 만들기
label_encoder = preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder()


# In[66]:


df = sns.load_dataset('mpg')
df.head()


# In[67]:


df['horsepower'].replace('?', np.nan, inplace=True)
df.isnull().sum()


# In[68]:


df.dropna(subset=['horsepower'], axis=0, inplace=True)
df.isnull().sum()


# In[69]:


df.info()


# In[70]:


# ['horsepower']데이터 타입을  float64
df['horsepower'] = df['horsepower'].astype('float')


# In[71]:


count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(bin_dividers)


# In[73]:


# 3개의 bins에 이름 지정
bin_name = ['low power', 'mid power', 'high power']

# cut 함수로 각 데이터 쪼개기
df['hp_bin'] = pd.cut(x = df['horsepower'],
                        bins = bin_dividers,    # 경계선 값 리스트
                        labels = bin_name,      # 각 구간 이름
                        include_lowest = True   # 첫 경계선값 포함하는 것으로 함
                        )
df[['horsepower','hp_bin']].head(10)


# In[74]:


#label encoder로 문자열 범주를 숫자형 범주로 변환
onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))
print(onehot_labeled)
print(type(onehot_labeled))


# In[75]:


#2차원 행렬형태
onehot_reshped = onehot_labeled.reshape(len(onehot_labeled), 1)
print(onehot_reshped)
print(type(onehot_reshped))


# In[76]:


#희소행렬로 변환
onehot_fitted = onehot_encoder.fit_transform(onehot_reshped)
print(onehot_fitted)
print(type(onehot_fitted))


# # Time Series

# In[7]:


df = pd.read_csv('./Data/stock-data.csv')
df.head()


# In[8]:


df.info()


# In[9]:


df['new_date'] = pd.to_datetime(df['Date'])
df.head()


# In[10]:


df.set_index('new_date', inplace = True)
df.head()


# In[6]:


df.drop("Date", axis = 1, inplace = True)
df.head()


# In[11]:


dates = ['2019-01-01','2020-03-01','2021-06-01']
ts_date = pd.to_datetime(dates)
ts_date


# In[13]:


# Time stamp 를 period로 변환
pr_day = ts_date.to_period(freq='D')   # day
pr_day


# In[14]:


pr_month = ts_date.to_period(freq='M')   # month
pr_month


# In[15]:


pr_year = ts_date.to_period(freq='A')   # annual
pr_year


# In[19]:


#timestamp의 배열 만들기, 월 간격, 월의 시작일 기준
ts_ms = pd.date_range(start = '2019-01-01',    # 날짜범위에서 시작
                     end = None,     # 날짜범위 끝
                     periods = 6,     # 생성할 timestamp의 개수
                     freq = 'MS',      # 시간간격 MS : 월의 시작일
                     tz = 'Asia/Seoul')     # tlrkseo wldur
print(len(ts_ms))
print(ts_ms)


# In[ ]:





# In[44]:


# 월간격, 월의 마지막날 기준
ts_me = pd.date_range(start = '2019-01-01', periods = 6, freq = "M", tz = 'Asia/Seoul')
print(len(ts_me))
print(ts_me)


# In[45]:


# 3 months
ts_3m = pd.date_range(start = '2019-01-01', periods = 6, freq = "3M", tz = 'Asia/Seoul')
print(len(ts_3m))
print(ts_3m)


# ### 10씩 더하기

# In[46]:


titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]


# In[47]:


def add_10(x):
    return x+10


# In[48]:


df_map = df.applymap(add_10)   # 


# In[49]:


df.head()


# In[50]:


df_map.head()    # 10씩 더해짐


# In[51]:


def missing_value(series):
    return series.isnull()    # boolean 시리즈로 변환


# In[52]:


result = df.apply(missing_value, axis = 0)
result.head()


# In[54]:


def min_max(x):
    return x.max() - x.min()


# In[55]:


result2 = df.apply(min_max)
result2


# In[56]:


df['ten'] = 10
df.head()


# In[57]:


def add_two_obj(a,b):
    return a+b


# In[58]:


df['add'] = df.apply(lambda x : add_two_obj(x['age'],x['ten']), axis = 1)
df.head()

