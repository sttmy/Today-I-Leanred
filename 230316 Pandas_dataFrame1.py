#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# 열이름을 key, 리스트를 value로 갖는 dictionary (2차원 array)

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data)
print(type(df))
print(df)


# In[3]:


# 리스트에 행 인덱스 열이름 지정해 데이터프레임 만들기
df = pd.DataFrame([[15, 'M','Sinchon'],[17, 'F','Yonsei']], 
                  index = ['James','Mary'],columns = ['age','sex','school'] )
df


# In[6]:


print(df.index)  # index name
print(df.columns)  # col name


# In[7]:


df.columns = ['나이','M/F','소속']   # column명 바꿔줌
df


# In[8]:


df.index = ['Student1', 'Student2']   #index명 바꿔줌
df


# In[9]:


# 메소드 사용해 행, 열이름 변경
df = pd.DataFrame([[15, 'M','Sinchon'],[17, 'F','Yonsei']], 
                  index = ['James','Mary'],columns = ['age','sex','school'] )
df.rename(columns = {'age':'how old','sex':'M/F','school':'L'}, inplace = True )   #inplace true는 값 자체를 바꾸는 것
df


# In[10]:


df.rename(index = {'James':'student1','Mary':'student2'}, inplace = True ) 
df


# In[11]:


data = {'kor':[80,90,70,30],'eng':[90,70,60,40],'math':[90,60,80,70]}
data


# In[12]:


data_df = pd.DataFrame(data, index = ['춘향','몽룡','향단','방자'])
data_df


# In[13]:


# 몽룡의 국어점수
data_df.iloc[0,1]


# In[16]:


# 모든 국어점수
data_df.loc[:,'kor']


# In[24]:


data_df.iloc[:,0]


# In[17]:


data_df['kor']


# In[19]:


import numpy as np
np.sort(data_df['kor'])


# In[28]:


np.argsort(data_df['kor'])


# In[29]:


data_df['kor']['몽룡']   #열, 인덱스


# In[30]:


import numpy as np
np.random.seed(2023)
d = pd.DataFrame(np.random.randint(60,100,12).reshape(4,3),
                 index = ['James','Maria','Brian','Alice'], 
                 columns = ['kor','eng','math'])
d


# #### Select row

# In[34]:


get_ipython().run_cell_magic('writefile', 'sample.csv', 'c1, c2, c3\n1, 1.15, one\n2, 2.23, two\n3, 3.32, three\n')


# In[35]:


# 파일 읽기
df = pd.read_csv('sample.csv')


# In[36]:


df


# In[37]:


df2 = df[:]   #copy명령 없이 복사


# In[38]:


df2.drop(1,inplace=True)
df2


# In[40]:


df3 = pd.DataFrame(np.random.randint(60,100,12).reshape(4,3),
                 index = ['James','Maria','Brian','Alice'], 
                 columns = ['kor','eng','math'])
df3


# In[41]:


df3.drop('Brian',inplace=True)
df3


# In[44]:


df3.drop(columns = 'kor')


# In[45]:


df3.drop(['Maria','Alice'],inplace=True)
df3


# In[46]:


df4 = pd.DataFrame(np.random.randint(60,100,16).reshape(4,-1),
                 index = ['James','Maria','Brian','Alice'], 
                 columns = ['kor','eng','math','music'])
df4


# In[47]:


df5 = df4.copy()
df5


# In[51]:


df5.drop('math',axis = 1, inplace = True)
df5


# In[52]:


df6 = df4.copy()
df6


# In[53]:


df6.drop(['eng','music'], axis = 1, inplace = True)
df6


# In[54]:


# select row

mar1 = df4.loc['Maria']   #location
mar1


# In[55]:


mar2 = df4.iloc[1]   #index location
mar2


# In[56]:


label1 = df4.loc[['Brian','Alice']]   #list형태로 반드시 넣어줘야 함
label1


# In[57]:


label22 = df4.iloc[[2,3]]
label22


# In[58]:


label2 = df4.iloc[2:,]
label2


# In[59]:


label3 = df4.loc[['Maria','Brian']]
label33 = df4.loc['Maria':'Brian']
print(label3)
print(label33)


# In[60]:


label4 = df4.iloc[[1,2]]
label44 = df4.iloc[1:3]
print(label4)
print(label44)


# #### Select Columns

# In[67]:


df4


# In[66]:


math1 = df4['math']
print(type(math1))
print(math1)


# In[68]:


eng1 = df4.eng   # 하나만 가져올 수 있음
eng1


# In[72]:


math_music = df4[['math','music']]
print(type(math_music))
print(math_music)


# In[73]:


math2 = df4['math']    # series 로 가져옴
print(type(math2))
print(math2)


# In[74]:


math22 = df4[['math']]    # dataframe으로 가져옴
print(type(math22))
print(math22)


# #### Select elements

# In[75]:


df4


# In[77]:


# Maria의 음악점수 가져오기
df4.iloc[1,3] 


# In[79]:


df4.loc['Maria']['music']


# In[81]:


df4.loc['Maria','music']


# In[91]:


# Maria의 영어, 수학점수 가져오기
df4.iloc[1,1:3]


# In[83]:


df4.loc['Maria',['eng','math']]


# In[92]:


df4.iloc[1,[1,2]]


# In[93]:


# James, eng, math, music, iloc 사용 / loc 사용
df4.iloc[0,1:]


# In[96]:


df4.iloc[0,[1,2,3]]


# In[97]:


df4.loc['James',['eng','math','music']]


# In[104]:


df4.loc['James','eng':'music']


# In[98]:


# Maria~Alice, eng~music 가져오기, iloc/loc 사용
df4


# In[100]:


df4.loc[['Maria','Brian','Alice'],['eng','math','music']]


# In[105]:


df4.loc['Maria':'Alice','eng':'music']


# In[102]:


df4.iloc[1:,1:]


# In[103]:


df4.iloc[[1,3],1:]


# #### Add rows & columns

# In[106]:


df4


# In[108]:


df4['pe']= 90
df4.loc[4] = 0
df4


# In[110]:


df4.loc['George'] = [90, 70, 60, 75, 60]
df4


# In[115]:


df4.drop(4, axis = 0, inplace=True)


# In[116]:


df4


# In[121]:


# 중간에 row 삽입하는 방법
# 1.reindex
# 2.concat iloc
# 3.insert


# ### Set Index

# In[131]:


# set_index
exam_data = {'name':['Gildong','Cheol','Younghee'],
            'math':[90,80,70],'eng':[98,89,95],
            'music':[85,95,100],'phy':[100,90,90]}
exam_data


# In[132]:


df = pd.DataFrame(exam_data)
df


# In[133]:


# 열 자체를 index명으로 지정
df.set_index('name', inplace=True)
df


# In[134]:


#Gildong, phy
df.iloc[0,3]


# In[135]:


df.loc['Gildong','phy']


# In[136]:


#Gildong, phy 90점으로 수정
df.iloc[0,3] = 90
df


# In[139]:


# Cheol, music, phy을 50점으로 변경
df.iloc[[1,1],[2,3]] = [50,50]
df


# In[144]:


df.loc['Cheol',['music','phy']] = 50
df


# In[142]:


# Cheol, music, phy을 100, 50점으로 변경
df.iloc[1,2] = 100
df


# In[145]:


df.loc['Cheol',['music','phy']] = 100, 50
df


# In[152]:


# set_index 
exam_data = {'name':['Gildong','Cheol','Younghee'],
            'math':[90,80,70],'eng':[98,89,95],
            'music':[85,95,100],'phy':[100,90,90]}
df = pd.DataFrame(exam_data)
df


# In[154]:


ndf = df.set_index(['name'])
ndf


# In[155]:


ndf = df.set_index(['music'])
ndf


# In[156]:


ndf = df.set_index(['math','music'])
ndf


# ### Transpose

# In[146]:


df.transpose()


# In[147]:


df.T


# ### Reindex

# In[157]:


dict_data


# In[158]:


df = pd.DataFrame(dict_data, index = ['r0','r1','r2'])
print(df)


# In[162]:


# index 지정해서 새로 행추가
new_index = ['r0','r1','r2','r3','r4']
ndf = df.reindex(new_index)
ndf


# In[164]:


# reindex로 0으로 채우기
ndf2 = df.reindex(new_index, fill_value = 0)
ndf2


# In[165]:


# reset_index 
ndf2 = ndf2.reset_index()
ndf2


# ### sort

# In[168]:


# 내림차순으로 행인덱스 정렬
ndf2 = ndf2.sort_index(ascending = False)
print(ndf2)


# In[171]:


# 열 c1기준, 내림차순
ndf3 = ndf2.sort_values(by= 'c1', ascending = False)
ndf3


# ### Series 숫자계산
