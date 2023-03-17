#!/usr/bin/env python
# coding: utf-8

# # 데이터 탐색 및 시각화

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ### ex) auto mpg 데이터

# In[3]:


auto = pd.read_csv('./Data/auto-mpg.csv', header=None)
auto.head()


# In[4]:


auto.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']
auto


# In[7]:


auto.describe()


# In[8]:


auto.nunique()  # checking columns' unique values


# ### scatter plot

# In[9]:


auto.plot(x = 'weight', y = 'mpg', kind = 'scatter')  # 자동차가 가벼우면 연비가 줄어들 것


# ### Boxplot

# In[10]:


auto[['mpg','cylinders']].plot(kind = 'box') 


# ### ex) 시도별 전출입 인구수 데이터

# In[11]:


df = pd.read_excel('./Data/시도별 전출입 인구수.xlsx', engine = 'openpyxl', header = 0)
df.head(3)


# In[12]:


df.describe()


# In[13]:


df.info()


# In[14]:


d = df.T
d.head()


# ### 결측값 채우기

# In[15]:


# method, forward로 채우기 row(index) 기준
# column을 넘나드는 방식은 따로 있을 것
df = df.fillna(method = 'ffill')    # 'bfill'은 backward로 채우기


# ### 데이터 전처리

# In[16]:


# 서울에서 다른 지역으로 이동한 데이터만 추출

# 전출지별 '서울특별시'만 고르면 됨
immfs = ( df['전출지별'] == '서울특별시')  & ( df['전입지별'] != '서울특별시' ) 
immfs


# In[17]:


df_seoul = df[immfs]
df_seoul.head()


# In[18]:


df_seoul = df_seoul.drop(['전출지별'], axis = 1)   # '전출지별' column 제외
df_seoul


# In[19]:


df_seoul.rename({'전입지별':'전입지'}, axis = 1, inplace = True)  
# '전입지별' 이름 변경
df_seoul


# In[20]:


df_seoul.set_index('전입지', inplace = True)
df_seoul


# In[21]:


# 서울에서 경기도로 이동한 인구 데이터값만 선택
sr_one = df_seoul.loc['경기도']
sr_one


# In[22]:


plt.plot(sr_one.index, sr_one.values)


# In[74]:


plt.plot(sr_one)
plt.title('서울시 → 경기도 인구 이동')  # 제목
plt.xlabel('기간')   # x축
plt.ylabel('이동인구수')   #y축
plt.show()


# ## 한글폰트설치

# ### @ Jupyter
# 

# In[181]:


from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False   # 마이너스 표시
# font_path = "C:/Windows/Fonts/맑은 고딕.ttf"  # Window 안에 있는 폰트를 활용
# font_name = font_manager.FontProperties(fname = font_path).get_name()
# rc('font', family=font_name)

plt.rc('font', family = 'Malgun Gothic')


# ### @ Colab

# #### colab 실행할 때마다 매번 설치해줘야 함

# In[ ]:


get_ipython().system("apt-get install -y fonts-nanum   # '나눔'글꼴 설치")
get_ipython().system('fc-cache -fv')
get_ipython().system('rm -rf ~/.cache/matplotlib')
# 설치 후 반드시 런타임 재시작
# 다시 돌리지 말고, 그 이후 코드 실행


# In[ ]:


# library 불러오기

import matplotlib as mpl
plt.rc('font', family = 'NanumBarunGothic')


# #### 참고. 마이너스 표시

# In[ ]:


import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False


# ## 그래프 그리기

# In[35]:


plt.figure(figsize = (12,6)) # 사이즈(인치)
plt.plot(sr_one)
plt.title('서울시 → 경기도 인구 이동 추이', size = 20)  # 제목
plt.xlabel('기간', size = 10)   # x축명
plt.xticks(size = 10, rotation = 45)   # tick:눈금
# rotation : 표기하는 회전각도, 'vertical도 가능'
plt.ylabel('이동인구수', size = 10)   #y축명
# legend 범례
plt.legend(fontsize = 10, labels = ['인구수(서울 → 경기)'], loc = 0)   
# loc는 범례 위치 : 0 'best', 1 'upper left' , 4 'lower right' ...
plt.show()


# In[58]:


plt.figure(figsize = (12,6)) # 사이즈(인치)

plt.plot(sr_one, marker = '*', markersize = 5, color = 'orange')    # marker 점 표시 ^, s, 'o'...

plt.title('서울시 → 경기도 인구 이동 추이', size = 20)  # 제목

plt.xlabel('연도', size = 15)   # x축명
plt.xticks(size = 10, rotation = 45)  
# rotation : 표기하는 회전각도, 'vertical도 가능'
plt.ylabel('이동인구수', size = 15)   #y축명

# legend 범례
plt.legend(fontsize = 10, labels = ['인구수(서울 → 경기)'], loc = 4)   
# loc는 범례 위치 : 0 'best', 1 'upper left' , 4 'lower right' ...

# 각 축 범위설정 가능
plt.ylim(5000, 800000) 

# 눈금표시 (Grid)
plt.grid(True, axis = 'y')

# 주석표시
plt.annotate("인구이동증가(1970-1995)", # 텍스트입력
            xy = (10, 450000),          # 텍스트 위치 기준점
            rotation = 25,              # 텍스트 회전 각도
            va = 'baseline',            # 텍스트 상하정렬
            ha = 'center',              # 텍스트 좌우정렬
            fontsize = 10
            )
plt.annotate("인구이동감소(1995-2017)", # 텍스트입력
            xy = (40, 450000),          # 텍스트 위치 기준점
            rotation = 340,              # 텍스트 회전 각도
            va = 'baseline',            # 텍스트 상하정렬
            ha = 'center',              # 텍스트 좌우정렬
            fontsize = 10
            )

plt.show()


# In[76]:


fig = plt.figure(figsize = (10,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(sr_one, marker = '*', markersize = 7, color = 'orange', markerfacecolor = 'green')
ax2.plot(sr_one, marker = '*', markersize = 7, color = 'purple',linewidth = 4, label = '서울 → 경기')
ax2.legend(loc='best')

ax1.set_ylim(50000, 700000)
ax2.set_ylim(50000, 700000)

ax1.set_xticklabels(sr_one.index, rotation = 75)
ax2.set_xticklabels(sr_one.index, rotation = 75)

ax1.grid(True, axis = 'y')
ax2.grid(True, axis = 'y')

plt.show()


# In[ ]:





# In[51]:


# 서울에서 제주도로 이동한 인구 데이터값만 선택
sr_two = df_seoul.loc['제주특별자치도']


# In[63]:


plt.figure(figsize = (12,6)) # 사이즈(인치)

plt.plot(sr_one, marker = '*', markersize = 5, color = 'orange')    # marker 점 표시 ^, s, 'o'...
plt.plot(sr_two, marker = "*", markersize = 5, color = 'green')

plt.title('서울시 → 경기도 및 제주도 인구 이동 추이', size = 20)  # 제목

plt.xlabel('연도', size = 15)   # x축명
plt.xticks(size = 10, rotation = 45)  
# rotation : 표기하는 회전각도, 'vertical도 가능'
plt.ylabel('이동인구수', size = 15)   #y축명

# legend 범례
plt.legend(fontsize = 10, labels = ['서울→경기','서울→제주'], loc = 0)   
# loc는 범례 위치 : 0 'best', 1 'upper left' , 4 'lower right' ...

# 눈금표시 (Grid)
plt.grid(True, axis = 'y')

plt.show()


# In[72]:


# 서울에서 '충청남도', '경상북도', '강원도'로 이동한 인구데이터값
col_years = list(map(str, range(1970, 2018)))
df3 = df_seoul.loc[['충청남도','경상북도','강원도'], col_years]


# In[79]:


# 스타일 서식 지정

plt.style.use('ggplot')
fig = plt.figure(figsize = (20,5))
ax = fig.add_subplot(1,1,1)
ax.plot(col_years, df3.loc['충청남도',:], marker = 'o', markerfacecolor = 'green',
       markersize = 10, color = 'olive', linewidth = 2,
       label = '서울 → 충청남도')
ax.plot(col_years, df3.loc['경상북도',:], marker = 'o', markerfacecolor = 'blue',
       markersize = 10, color = 'skyblue', linewidth = 2,
       label = '서울 → 경상북도')
ax.plot(col_years, df3.loc['강원도',:], marker = 'o', markerfacecolor = 'red',
       markersize = 10, color = 'magenta', linewidth = 2,
       label = '서울 → 강원도')
ax.legend()
ax.set_title("서울 → 충청남도, 경상북도, 강원도 인구이동", size = 20)
ax.set_xlabel('연도', size = 12)
ax.set_ylabel('인구이동수', size = 12)
ax.set_xticklabels(col_years, rotation = 60)

plt.show()


# In[ ]:


# Quiz
# df4, df3에서 전라남도 추가
# ax1 = subplot(2,2,2) 4등분으로 그려볼 것


# In[80]:


df3


# In[96]:


# DataFrame 데이터 추가 
df44 = df3.append(df_seoul.loc[['전라남도']])
df44


# In[83]:


df4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'], col_years]
df4


# In[94]:


fig = plt.figure(figsize = (30,30))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)


ax1.plot(col_years, df4.loc['충청남도',:], marker = 'o', markerfacecolor = 'green',
       markersize = 10, color = 'olive', linewidth = 2,
       label = '서울 → 충청남도')
ax2.plot(col_years, df4.loc['경상북도',:], marker = 'o', markerfacecolor = 'blue',
       markersize = 10, color = 'skyblue', linewidth = 2,
       label = '서울 → 경상북도')
ax3.plot(col_years, df4.loc['강원도',:], marker = 'o', markerfacecolor = 'red',
       markersize = 10, color = 'magenta', linewidth = 2,
       label = '서울 → 강원도')
ax4.plot(col_years, df4.loc['전라남도',:], marker = 'o', markerfacecolor = 'yellow',
       markersize = 10, color = 'black', linewidth = 2,
       label = '서울 → 전라남도')

ax1.set_title("서울 → 충청남도 인구이동", size = 20)
ax2.set_title("서울 → 경상북도 인구이동", size = 20)
ax3.set_title("서울 → 강원도 인구이동", size = 20)
ax4.set_title("서울 → 전라남도 인구이동", size = 20)

# ax.set_xlabel('연도', size = 12)
# ax.set_ylabel('인구이동수', size = 12)
# ax.set_xticklabels(col_years, rotation = 60)

plt.show()


# In[104]:


# TCH
fig = plt.figure(figsize = (30,10))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)


ax1.plot(col_years, df44.loc['충청남도',:], marker = 'o', markerfacecolor = 'green',
       markersize = 10, color = 'olive', linewidth = 2,
       label = '서울 → 충청남도')
ax2.plot(col_years, df44.loc['경상북도',:], marker = 'o', markerfacecolor = 'blue',
       markersize = 10, color = 'skyblue', linewidth = 2,
       label = '서울 → 경상북도')
ax3.plot(col_years, df44.loc['강원도',:], marker = 'o', markerfacecolor = 'red',
       markersize = 10, color = 'magenta', linewidth = 2,
       label = '서울 → 강원도')
ax4.plot(col_years, df44.loc['전라남도',:], marker = 'o', markerfacecolor = 'yellow',
       markersize = 10, color = 'orange', linewidth = 2,
       label = '서울 → 전라남도')

ax1.legend(loc='best')
ax2.legend(loc='best')
ax3.legend(loc='best')
ax4.legend(loc='best')
ax1.set_title("서울 → 충청남도 인구이동", size = 15)
ax2.set_title("서울 → 경상북도 인구이동", size = 15)
ax3.set_title("서울 → 강원도 인구이동", size = 15)
ax4.set_title("서울 → 전라남도 인구이동", size = 15)

ax1.set_xticklabels(col_years, rotation = 90)
ax2.set_xticklabels(col_years, rotation = 90)
ax3.set_xticklabels(col_years, rotation = 90)
ax4.set_xticklabels(col_years, rotation = 90)

# ax.set_xlabel('연도', size = 12)
# ax.set_ylabel('인구이동수', size = 12)
# ax.set_xticklabels(col_years, rotation = 60)

plt.show()


# ###  색에 핵사코드 활용
# 

# In[105]:


colors = {}
for name, hex in mpl.colors.cnames.items():
    colors[name] = hex


# In[106]:


print(colors)


# In[107]:


df4.head()


# ### 면적 그래프 그리기

# In[108]:


df4 = df4.T


# In[109]:


df4.head()


# In[110]:


df4.index = df4.index.map(int)   # 전입지를 숫자로 변경


# In[115]:


df4.plot(kind = 'area', stacked = False, alpha=0.4, figsize = (20,10) )   
# stacked 그래프가 겹치도록 하려면 False (누적되지 않고)
# alpha 투명도
plt.title('서울 → 타 도 인구이동', size = 30)
plt.ylabel('인구이동수', size = 25)
plt.xlabel('연도', size = 25)
plt.legend(loc='best', fontsize = 20)
plt.show()


# In[116]:


# stacked = True이면 수치 누적됨
df4.plot(kind = 'area', alpha=0.4, figsize = (20,10) )   
plt.title('서울 → 타 도 인구이동(누적)', size = 30)
plt.ylabel('인구이동수', size = 25)
plt.xlabel('연도', size = 25)
plt.legend(loc='best', fontsize = 20)
plt.show()


# ### Bar chart

# In[118]:


df4.plot(kind = 'bar', figsize = (20,10), width = 0.7, 
         color = ['purple','green','skyblue','orange'])   
plt.title('서울 → 타 도 인구이동(Bar Graph)', size = 30)
plt.ylabel('인구이동수', size = 25)
plt.xlabel('연도', size = 25)
plt.legend(loc='best', fontsize = 20)
plt.show()


# In[121]:


# Horizontal bar
df4.plot(kind = 'barh', figsize = (10,10), width = 0.7, 
         color = ['purple','green','skyblue','orange'])
plt.title('서울 → 타 도 인구이동(Horizontal Bar Graph)', size = 30)
plt.ylabel('인구이동수', size = 25)
plt.xlabel('연도', size = 25)
plt.legend(loc='best', fontsize = 20)
plt.show()


# In[127]:


df44 = df4.copy()
df44.head()


# In[131]:


df44.drop(columns = [['충청남도','전라남도']], inplace=True)
df44.head()


# In[138]:


df5 = df4.T
df5['합계'] =df5.sum(axis=1)
df_total = df5[['합계']].sort_values(by= '합계', ascending= True)
df_total.head()


# In[140]:


plt.style.use('ggplot')

# Horizontal bar
df_total.plot(kind = 'barh', figsize = (5,2), width = 0.5, 
         color = 'cornflowerblue')
plt.title('서울 → 타 도 인구이동(Horizontal Bar Graph)', size = 20)
plt.ylabel('전입지', size = 10)
plt.xlabel('이동인구수', size = 10)
plt.show()


# ## Ex) 남북한 전력량으로 secondary_y를 그리기

# In[142]:


elec = pd.read_excel('./Data/남북한발전전력량.xlsx', engine = 'openpyxl', convert_float = True)
elec.head()


# In[143]:


elec.tail()


# In[149]:


elec.info()


# In[150]:


elec.describe()


# In[144]:


# 북한데이터만 가져오기
elec_n = elec.loc[5:]
elec_n


# In[145]:


elec_n.drop('전력량 (억㎾h)', axis = 1, inplace = True)
elec_n


# In[148]:


elec_n.set_index('발전 전력별', inplace = True)
elec_n


# In[153]:


elec_n_y = elec_n.T
elec_n_y.tail(3)


# In[154]:


# 증감율 (변동률) 계산

elec_n_y = elec_n_y.rename(columns = {'합계':'총발전량'})
elec_n_y['총발전량 - 1년'] = elec_n_y['총발전량'].shift(1)    # shift 
elec_n_y.head()


# In[167]:


elec_n_y['증감율(%)'] = ( ( elec_n_y['총발전량'] / elec_n_y['총발전량 - 1년'] ) -1 ) * 100
elec_n_y.tail()


# In[168]:


elec_n_y.drop(columns = ['증감율'], inplace =True)
elec_n_y.tail()


# ### 2축 그래프 그리기

# In[172]:


ax1_e = elec_n_y[['수력','화력']].plot(kind = 'bar', figsize = (10,5), width = 0.7, stacked = True)  # 누적표시
ax2_e = ax1_e.twinx()   # 복사하기. 
ax2_e.plot(elec_n_y.index, elec_n_y['증감율(%)'], ls = '--',  # line style
           marker = 'o', markersize = 10, color = 'olive', label = '전년대비 증감율(%)'
          )
ax1_e.set_ylim(0,400)
ax2_e.set_ylim(-50,50)

ax1_e.set_xlabel('연도', size = 15)
ax1_e.set_ylabel('발전량(억 Kwh)', size = 15)
ax2_e.set_xlabel('전년대비 증감율', size = 15)

plt.title('북한 전력 발전량(1990~2016)', size = 25)
ax1_e.legend(loc= 'upper left')
plt.show()


# ### 히스토그램
# #### 단변수 데이터의 빈도수를 나타냄

# In[173]:


auto.head()


# In[174]:


auto['mpg']


# In[175]:


auto.describe()


# In[183]:


plt.style.use('classic')

# 연비(mpg) 열에 대한 히스토그램 그리기

auto['mpg'].plot(kind = 'hist', bins = 10,    # bins: 10개 구간으로 나누겠다
                 color = 'coral', figsize= (10,5))
plt.title('Histogram of mpg data')
plt.xlabel('mpg')
plt.show()


# In[186]:


plt.style.use('ggplot')
# Scatter plot 

auto.plot(x = 'weight', y ='mpg', kind = 'scatter', c = 'coral', s = 15,
         figsize = (10,5))
plt.title('Scatter plot of mpg vs weight')
plt.show()


# In[187]:


plt.style.available


# ### 버블차트

# In[196]:


c = auto.cylinders / auto.cylinders.max()
c


# In[229]:


plt.style.use('bmh')

# Bubble chart, cylinder 개수 상대적 비율 계산하여 시리즈 생성

cylinder_size = auto.cylinders / auto.cylinders.max() * 500

auto.plot(x = 'weight', y ='mpg', kind = 'scatter', c = 'coral', 
          s = cylinder_size, figsize = (10,5), alpha = 0.5)
plt.title('Scatter plot of mpg-weight-cylinders')
plt.show()


# In[204]:


# 3개의 변수로 산점도 그리기

plt.style.use('dark_background')

auto.plot(x = 'weight', y ='mpg', kind = 'scatter', c = cylinder_size, 
          s = 50, figsize = (10,5), alpha = 0.5, 
          cmap = 'viridis'   # color map
         )
plt.title('Scatter plot : mpg-weight-cylinders')
plt.show()


# In[201]:


# 3개의 변수로 산점도 그리기

plt.style.use('default')

auto.plot(x = 'weight', y ='mpg', kind = 'scatter', c = cylinder_size, 
          s = 50, figsize = (10,5), alpha = 0.5, marker = '+',
          cmap = 'jet'   # color map
         )
plt.title('Scatter plot : mpg-weight-cylinders')
plt.show()


# ## Pie chart

# In[205]:


auto.head()


# In[5]:


auto.nunique()


# In[209]:


auto['count'] = 1
auto_origin = auto.groupby('origin').sum()    #origin의 그룹별로 더해줌
print(auto_origin)


# In[220]:


plt.style.use('default')
auto_origin.index = ['USA','EU','JAP'] 
auto_origin['count'].plot(kind = 'pie', figsize = (7,5), 
                          autopct = '%1.1f%%',  #autopct: 전체 percentage 자동으로 표기, 소숫점 첫째자리까지만, 실수형태로
                          startangle = 220,       # startangle 파이조각 나누는 시작점(각도표시)
                          colors = ['chocolate','bisque','cadetblue']
                         )
plt.title('Model origin', size = 20)
plt.axis('equal')   # 파이차트의 비율을 같게(원에 가깝게 그림)
plt.legend(labels = auto_origin.index, loc = 'upper left')
plt.show()


# ### Box plot

# In[231]:


plt.style.use('default')

# 그래프 객체를 생성 (fig에 2개의 subplot을 생성)
fig = plt.figure(figsize = (15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# ax객체에 botplot메서드로 그래프 출력
ax1.boxplot(x = [auto[auto['origin']==1]['mpg'],
                auto[auto['origin']==2]['mpg'],
                auto[auto['origin']==3]['mpg']],
            labels = auto_origin.index)
ax2.boxplot(x = [auto[auto['origin']==1]['mpg'],
                auto[auto['origin']==2]['mpg'],
                auto[auto['origin']==3]['mpg']],
            labels = auto_origin.index,
            vert = False # box plot 옆으로 그리기
           )

ax1.set_title('MPG by country (vertical box)')
ax2.set_title('MPG by country (horizontal box)')

# plt.axis('equal')   # 파이차트의 비율을 같게(원에 가깝게 그림)
# plt.legend(labels = auto_origin.index, loc = 'upper left')
plt.show()


# In[ ]:




