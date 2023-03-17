#!/usr/bin/env python
# coding: utf-8

# # Series 숫자계산

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns


# ### 사칙연산

# In[2]:


student1 = pd.Series({'kor':100, 'eng':80, 'math':90})
print(student1)


# In[3]:


# 과목별로 점수를 200으로 나누기


percentage = student1 / 200
percentage


# In[4]:


type(percentage)


# In[6]:


student2 = pd.Series({'math':80, 'kor':90, 'eng':80})


# In[7]:


# 두 학생의 과목별 점수 사칙연산


add1 = student1 + student2
add1


# In[8]:


sub = student1 - student2
mul = student1 * student2
div = student1 / student2
print(sub)
print(mul)
print(div)


# In[13]:


# 사칙연산 결과를 데이터프레임으로 합치기, 각각은 series임


result = pd.DataFrame([add1, sub, mul,div], index = ['add','sub','mul','div'])
result


# ### 결측치가 있는 경우 사칙연산

# In[14]:


student1 = pd.Series({'kor':np.nan, 'eng':80, 'math':90})
student2 = pd.Series({'math':80, 'kor':90, 'eng':80})

add1 = student1 + student2
sub = student1 - student2
mul = student1 * student2
div = student1 / student2

result2 = pd.DataFrame([add1, sub, mul,div], index = ['add','sub','mul','div'])
result2   # 결측치 있는 경우, 연산이 안 됨


# In[18]:


# 연산메소드 사용해도 같은 결과임

add3 = student1.add(student2)
sub3 = student1.sub(student2)
mul3 = student1.mul(student2)
div3 = student1.div(student2)
print(add3)
print(sub3)
print(mul3)
print(div3)


# In[19]:


# 연산메소드 + fill_value = 0으로 처리할 경우, 값이 도출됨


add3 = student1.add(student2, fill_value=0)
sub3 = student1.sub(student2, fill_value=0)
mul3 = student1.mul(student2, fill_value=0)
div3 = student1.div(student2, fill_value=0)

result3 = pd.DataFrame([add3, sub3, mul3,div3], index = ['add','sub','mul','div'])
result3


# # DataFrame의 연산

# ### ex) Titanic dataset

# In[25]:


titanic = sns.load_dataset('titanic')
titanic.head()    #첫 5행 출력


# In[24]:


len(titanic)


# In[27]:


# age, fare 열 출력해보기



df = titanic[['age','fare']]    
df2 = titanic.loc[:,['age','fare']]

df.tail()  # 마지막 5행 출력


# In[29]:


new_df = df + 10
new_df.tail()


# In[30]:


# 데이터프레임끼리 연산
new_df - df


# ### Data 불러오기

# In[38]:


df = pd.read_csv('./Data/sample.csv')
df


# In[39]:


file_path = './Data/sample.csv'
df1 = pd.read_csv(file_path)
df1


# In[33]:


df2 = pd.read_csv(file_path, header = None)   # header 없는, 시작이 column인 경우 
df2


# In[35]:


df3 = pd.read_csv(file_path, header = 0)   # header값 default = 0
df3


# In[36]:


df4 = pd.read_csv(file_path, index_col = 'c1')
df4


# # Read 파일읽기

# ### Excel

# In[35]:


df1 = pd.read_excel('./Data/남북한발전전력량.xlsx',engine='openpyxl')   # excel open위한 모듈 설치 필요
df1.tail()


# ### Json

# In[36]:


df2 = pd.read_json('./Data/read_json_sample.json')     #json, dictionary 형태
df2.tail()


# ### Html

# In[37]:


df3 = pd.read_html('./Data/sample.html')
df3


# In[9]:


# 테이블을 따로 불러옴


for i in range(len(df3)):
    print('df3[%i]'%i)
    print(df3[i])
    print('\n')


# In[10]:


# 하나의 테이블을 dataframe 형태로 바꿔줌

df4 = df3[1]
df4.set_index(['name'],inplace=True)
df4


# # Save data 데이터저장

# In[11]:


# 데이터를 csv로 저장

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data)
df


# In[12]:


df.set_index('c0', inplace = True)
df


# In[13]:


df.to_csv("./df_csv.csv")


# In[14]:


df.to_json("./df_json.json")


# In[15]:


df.to_excel("./df_excel.xlsx")


# ## Excel sheet1, sheet2, ...에 저장하기 *많이쓰진 않음

# In[16]:


df1 = pd.DataFrame({'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],'c3':[10,11,12], 'c4':[13,14,15]})
df1.set_index('c0', inplace = True)
df1


# In[17]:


df2 = pd.DataFrame([[15, 'M','Sinchon'],[17, 'F','Yonsei']], 
                  index = ['James','Mary'],columns = ['age','sex','school'] )
df2


# ## Exploratory analysis 데이터탐색
# ### ex) auto_mpg data

# In[18]:


writer = pd.ExcelWriter('./df_excelwriter.xlsx')
df1.to_excel(writer, sheet_name = 'sheet1')
df2.to_excel(writer, sheet_name = 'sheet2')
writer.save()


# In[40]:


auto = pd.read_csv('./Data/auto-mpg.csv', header=None)
auto.head()


# In[41]:


auto.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']
len(auto)


# In[58]:


auto.head()


# In[29]:


auto.shape


# In[33]:


t = pd.read_excel('./data1/df_excel.xlsx')
t


# ### 데이터 정보 요약
# 

# In[31]:


print(auto.info())  # column9개, non-null count 데이터 있는 갯수


# ### 데이터프레임 기술통계정보 확인

# In[57]:


auto.describe()  # categorical data는 안 나옴


# In[43]:


auto.count() #각 열 갯수 확인


# In[44]:


type(auto.count())


# In[45]:


auto['origin'].value_counts()


# In[46]:


auto['origin'].unique()


# In[51]:


# 평균
auto.mean()


# In[52]:


# 'mpg' 평균
auto['mpg'].mean()


# In[53]:


auto.mpg.mean()


# In[55]:


# median
auto.mpg.median(), auto['mpg'].median()


# In[56]:


# min, max, std
auto.mpg.min(), auto.mpg.max(), auto.mpg.std()


# ### 변수간 관계 탐색

# In[59]:


auto.corr()


# In[60]:


auto[['mpg','weight']].corr()


# In[62]:


df1 = pd.read_excel('./Data/남북한발전전력량.xlsx',engine='openpyxl')   # excel open위한 모듈 설치 필요
df1.tail()


# In[63]:


df1.info()


# In[64]:


df1.describe()


# In[66]:


df1_ns = df1.iloc[[0,5],3:]   #1990 부터 남한, 북한 행 2개 가져오기
df1_ns


# In[67]:


df1_ns.index = ['South','North']
df1_ns


# In[68]:


df1_ns.columns = df1_ns.columns.map(int)   # col name을 정수형으로 변경


# In[69]:


df1_ns


# In[70]:


# 선 그래프 그리기
df1_ns.plot()


# In[71]:


# 행, 열 전치해서 다시 그리기
tdf_ns = df1_ns.T
tdf_ns.plot()


# In[72]:


tdf_ns.plot(kind = 'hist')


# In[ ]:




