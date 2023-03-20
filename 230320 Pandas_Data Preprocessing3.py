#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np


# ### Quiz

# In[8]:


titanic = sns.load_dataset('titanic')


# In[12]:


titanic.info()


# In[9]:


# 1. age 결측치, 평균으로 대체
titanic.age.fillna(titanic.age.mean(), inplace = True)


# In[10]:


# 2. embarked를 최빈값으로 대체
titanic.embarked.value_counts()


# In[11]:


titanic.embarked.fillna('S', inplace = True)


# In[13]:


# 3. embark_town 결측값이 있는 행 삭제

titanic.dropna(subset = ['embark_town'], inplace = True)


# In[14]:


# 4. deck 삭제
titanic.drop(columns = ['deck'], inplace = True)


# In[16]:


titanic.shape   # 삭제 확인


# In[17]:


# 5. titanic['adult/child'] 컬럼 만들고, 20살 이상이면 adult, 이하면 child
# lambda 활용
titanic['adult/child'] = titanic.age.apply(lambda x: 'adult' if x >= 20 else 'child')


# In[18]:


titanic.head(3)


# In[19]:


# 6. age를 기준으로 'age_cut' 컬럼을 생성 후 두 컬럼을 출력
bins = [1,20,30,50,70,100]
labels = ['미성년자', '청년', '중년', '장년', '노년']
titanic ['age_cut'] = pd.cut (titanic.age, bins, labels = labels)
titanic.tail()


# ## 데이터프레임 연결

# ### column기준으로 연결 : concat

# In[20]:


# pd.concat(데이터프레임리스트, axis = 축)
df1 = pd.DataFrame([['a',1], ['b',2]], columns = ['letter', 'number'])
df2 = pd.DataFrame([['c',3], ['d',4]], columns = ['letter', 'number'])
df3 = pd.DataFrame([['e',5,'!'], ['f',6,'@']], columns = ['letter', 'number','etc'])
df1, df2, df3


# In[25]:


# column명을 기준으로 연결
df_rowconcat = pd.concat([df1,df2,df3])   # default: axis = 0, col기준
df_rowconcat


# In[24]:


# row명을 기준으로 연결
df_colconcat = pd.concat([df1,df2,df3], axis = 1)   # axis = 1이면 row기준
df_colconcat


# In[26]:


# 공통된 컬럼만 남기기
df_rowconcat2 = pd.concat([df1, df2, df3], join = 'inner')   # inner join 교집합만 (공통되는 것) 
df_rowconcat2


# In[29]:


# 그런데 인덱스가 엉망, 인덱스 재지정 필요
df_rowconcat3 = pd.concat([df1, df2, df3], join = 'inner', ignore_index = True)
df_rowconcat3


# In[30]:


df_rowconcat2.reindex


# ### 열로 연결하기 

# In[38]:


df4 = pd.DataFrame({'age':[20,21,22]}, index = ['amy', 'james', 'david'])
df5 = pd.DataFrame({'phone':['010-1111-1111','010-1234-5678','010-3333-3333']}, index = ['amy', 'james', 'david'])
df6 = pd.DataFrame({'job':['student', 'programmer', 'CEO','designer']}, index = ['amy', 'james', 'david', 'kim'])


# In[39]:


df4


# In[42]:


df_col_concat = pd.concat([df4, df5, df6])   # default는 column기준으로 
df_col_concat


# In[43]:


df_column_concat = pd.concat([df4, df5, df6], axis = 1)   # row 기준
df_column_concat


# In[44]:


# nan있는 data제외
df_column_concat2 = pd.concat([df4, df5, df6], axis = 1, join = 'inner')   # concat은 default가 outer
df_column_concat2


# In[45]:


df_column_concat3 = pd.concat([df4, df5, df6], axis = 1, join = 'outer') 
df_column_concat3 


# ### Merge 함수 사용
# 
# #### merge는 default가 겹치는 애들만(Nan값 없음), concat은 전부다 묶어서 출력함(Nan값 있을수 있음)

# In[46]:


#pd.merge(left, right, on = 기준컬럼, how = 연결방법)
score = pd.read_csv('./Data/scores.csv')
score.head()


# In[47]:


# 일부 잘라서 사용
sc1 = score.loc[[1,2,3]][['name','eng']]   
sc2 = score.loc[[1,2,4]][['name','math']]


# In[48]:


sc1


# In[49]:


sc2


# In[50]:


# 공통 데이터로만 연결
pd.merge(sc1,sc2, on = 'name')   


# In[51]:


pd.merge(sc1,sc2, on = 'name', how = 'inner')   # merge는 default가 'inner'


# In[52]:


pd.merge(sc1,sc2, on = 'name', how = 'outer')    # outer : 모두 다 표시


# In[53]:


pd.merge(sc1,sc2, on = 'name', how = 'right') 


# In[54]:


pd.merge(sc1,sc2, on = 'name', how = 'left') 


# ## 행과 열의 형태 변형 (데이터 재구조화)

# ### melt 함수
# #### sorting하는 방법중에 하나, 때에 따라서 reshape도 사용할 수 있음

# In[57]:


score.head()


# In[59]:


score.info()


# In[58]:


score.melt()    # index가 쭉 나오고, 데이터 전체가 value값으로 출력, column먼저 


# In[60]:


pd.melt(score)    # score.melt()와 같은 명령어임


# In[61]:


# 고정할 컬럼 지정하여 melt 가능
# id_vars = [열이름리스트] 
# name을 고정해봄
score.melt(id_vars = ['name'])


# In[63]:


# 두개 묶어서 고정시키는 것 가능
score.melt(id_vars = ['name','kor'])


# In[64]:


score.melt(id_vars = ['name','kor','eng'])


# In[65]:


score.melt(id_vars = 'name', value_vars = 'kor')   # value 변수 선택도 가능


# In[67]:


score.melt(id_vars = 'name', value_vars = ['kor','math'])   # value 변수


# In[68]:


score.melt(id_vars = 'name', value_vars = ['kor','math'], var_name = 'subject', value_name = 'score')   


# ### Sorting해서 정렬

# In[70]:


df = score.melt(id_vars = 'name', var_name = 'subject', value_name = 'score')
df


# In[71]:


df.describe()


# In[72]:


def get_grade(x):
    if x >= 90:
        grade = 'A'
    elif x >= 80:
        grade = 'B'
    elif x >= 70:
        grade = 'C'
    elif x >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade


# In[73]:


df['grade'] = df['score'].apply(get_grade)
df.head()


# In[75]:


df = df.sort_values('name')
df


# In[83]:


df = df.sort_values(['score'], ascending = False)
df


# ### Pivot 사용

# In[84]:


# dataframe, pivot(index = 인덱스로 사용할 컬럼, columns = 컬럼으로 사용할 컬럼, values = 값으로 사용할 컬럼)
df.pivot(index = 'name', columns = 'subject',  values = 'score')


# In[85]:


df.pivot(index = 'name', columns = 'subject',  values = 'grade')


# In[89]:


df.pivot(index = 'name', columns = 'subject',  values = ['score','grade']).head(10)


# In[87]:


df.T


# In[88]:


df.transpose()


# ### 집계분석

# In[93]:


df_read = pd.read_csv('./Data/상품판매테이블.txt')
df_read


# In[94]:


df = pd.DataFrame({"item": ["shirts", "shirts", "shirts", "shirts", "shirts",
                          "pants", "pants", "pants", "pants"],
                    "color": ["white", "white", "white", "black", "black",
                          "white", "white", "black", "black"],
                   "size": ["small", "large", "large", "small",
                          "small", "large", "small", "small",
                         "large"],
                   "sale": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "inventory": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
df.head()


# In[95]:


# item, size별 재고 합계를 pivot_table메소드로 분석
# 재고, pants와 shirt, large와 small

df.pivot_table(index= 'item', columns = 'size', values = 'inventory', aggfunc = 'sum')


# In[96]:


# 색깔을 넣고 싶음, index가 추가됨
df.pivot_table(index= ['item','color'], columns = 'size', values = 'inventory', aggfunc = 'sum')


# In[98]:


# 색깔을 넣고 싶음, index가 추가됨
df.pivot_table(index= ['item','color'], columns = 'size', values = 'inventory', aggfunc = 'sum', 
               fill_value = 0)  #nan은 0으로 채울 것


# In[99]:


# 판매된 갯수 추가
df.pivot_table(index= ['item','color'], columns = 'size', values = ['inventory','sale'], aggfunc = 'sum', 
               fill_value = 0)


# ### titanic data

# In[110]:


titanic = sns.load_dataset('titanic')
titanic


# In[101]:


titanic = titanic[['survived','pclass','sex','age','embarked']]


# In[111]:


titanic = titanic[['survived','pclass','sex','age','embarked']]
titanic.info()


# In[112]:


titanic.dropna(inplace = True)    # inplace = True를 반드시 해줘야함
titanic.head()


# ### Quiz

# In[113]:


# 성별, 객실등급별 승선자수 : count 사용
# 총합: margins

titanic.pivot_table(index = 'sex', columns = 'pclass', values = 'survived',
                   aggfunc = 'count', margins = True)


# In[114]:


# 생존자/사망자 함께 표시
titanic.pivot_table(index = ['sex','survived'], columns = 'pclass', values = 'embarked',
                   aggfunc = 'count', margins = True)


# In[115]:


# 성별, 객실등급별 생존자수 사용
# survive = [1,0,1,1,0]  3명

titanic.pivot_table(index = 'sex', columns = 'pclass', values = 'survived',
                   aggfunc = 'sum', margins = True)


# In[116]:


# 생존률
# mean을 써주면 됨

titanic.pivot_table(index = 'sex', columns = 'pclass', values = 'survived',
                   aggfunc = 'mean', margins = True)


# In[117]:


# aggfunc = 'mean'은 default임

titanic.pivot_table(index = 'sex', columns = 'pclass', values = 'survived', margins = True)


# ### tips data

# In[118]:


tips = sns.load_dataset('tips')
tips.head()


# In[119]:


tips.info()
# total bill 총 계산요금
# tip 팁 요금
# size 식사 인원


# In[120]:


tips['tip_pct'] = ((tips.tip/tips.total_bill) * 100).round(2)
tips.head()


# ### Quiz

# In[125]:


tips.pivot_table('tip_pct','sex')


# In[128]:


tips.pivot_table(index = 'sex', values = 'tip_pct', 
                 aggfunc = 'mean', margins = True)


# In[130]:


tips.pivot_table(index = ['sex','smoker'], values = 'tip_pct',
                 aggfunc = 'mean', margins = True)


# In[133]:


## tch
tips.pivot_table('tip_pct',['sex','smoker'])


# In[134]:


## tch
tips.pivot_table('tip_pct','sex','smoker')


# In[132]:


## tch
tips.pivot_table('tip_pct','sex','smoker', 
                 aggfunc = 'count', margins = True)


# In[ ]:


## tch
tips.pivot_table('sex','smoker', aggfunc = 'count', margins = True)


# In[129]:


tips.pivot_table(index = ['sex','smoker'], values = 'tip_pct',
                 aggfunc = ['mean','min','max'], margins = True)


# In[135]:


## tch
tips.pivot_table('tip_pct','smoker', aggfunc = ['mean','min','max'], margins = True)


# ### Groupby

# In[136]:


# df.groupby(그룹기준컬럼).통게적용컬럼.통계함수
# .count(): 누락값 제외한 데이터수
# .size(): 누락값 포함한 데이터수


# In[137]:


titanic


# In[141]:


# 객실등급에 따른 승선자수
df_tt1 = titanic.groupby('pclass').survived.count()
df_tt1


# In[142]:


# 데이터프레임으로 변경   .to_frame()
df_t1 = titanic.groupby('pclass').survived.count().to_frame()
df_t1


# In[145]:


# 객실등급에 따른 생존자수 집계
df_t2 = titanic.groupby('pclass').survived.sum().to_frame()
df_t2


# In[146]:


# 객실등급에 따른 생존비율 결과 집계
df_t3 = titanic.groupby('pclass').survived.mean().to_frame()
df_t3


# In[153]:


df_t4 = pd.concat([df_t1, df_t2, df_t3], axis = 1)
df_t4


# In[155]:


df_t4.columns = ['승선자수','생존자수','생존비율']
df_t4


# In[157]:


# 성별 생존통계
sx1 = titanic.groupby('sex').survived.count().to_frame()
sx2 = titanic.groupby('sex').survived.sum().to_frame()
sx3 = titanic.groupby('sex').survived.mean().to_frame()
sx4 = pd.concat([sx1, sx2, sx3], axis = 1)
sx4.columns = ['승선자수','생존자수','생존비율']
sx4

