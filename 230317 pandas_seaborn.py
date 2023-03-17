#!/usr/bin/env python
# coding: utf-8

# ## Seaborn, chart

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[15]:


# 한글폰트 설치
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False   # 마이너스 표시
plt.rc('font', family = 'Malgun Gothic')


# In[2]:


titanic = sns.load_dataset('titanic')
titanic.head()


# ### Seaborn의 Style Theme: darkgrid, whitegrid, dart, white, ticks

# ### 회귀선표시

# In[6]:


# 기본 그림 툴
sns.set_style('darkgrid')
fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# 그래프그리기, 선형회귀선 표시
# regression plot 회귀선 그리기
sns.regplot(x='age', y='fare', data = titanic, ax=ax1)
# 그래프그리기, 선형회귀선 미표시
sns.regplot(x='age', y='fare', data = titanic, ax=ax2, fit_reg=False)
plt.show()


# In[8]:


# Heatmap
flights = sns.load_dataset('flights')
flights.head()


# In[9]:


flights_psg = flights.pivot('month','year','passengers')
flights_psg.head()


# In[11]:


flights.info()


# ### Heatmap

# In[17]:


plt.figure(figsize = (7,5))
plt.title('연도, 월별 승객수에 대한 Heatmap')

sns.heatmap(flights_psg, annot = True, fmt = 'd',   #fmt: format, d: 정수, 
            linewidths = 1)


# ### Seaborn의 Scatter plot

# In[20]:


sns.set_style('whitegrid')

titanic.head()


# In[23]:


fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# 이산형 변수의 분포 - 데이터 분산 미고려
sns.stripplot(x = 'class', y = 'age', data = titanic, ax = ax1)
# 이산형 변수의 분포 - 데이터 분산 고려 (중복X), 분산까지 표현됨
sns.swarmplot(x = 'class', y = 'age', data = titanic, ax = ax2)

# The main difference is that in a swarm plot, 
# the data points don't overlap and are adjusted along the categorical axis. 
# On the other hand, the issue of point overlapping in a strip plot can be partially fixed 
# by setting the alpha parameter that regulates point transparency

# 차트 제목
ax1.set_title('StripPlot')
ax2.set_title('SwarmPlot')
plt.show()


# In[27]:


# Bar plot
sns.set_style('whitegrid')

fig = plt.figure(figsize = (15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

# x축, y축에 변수를 할당
sns.barplot(x = 'sex', y = 'survived', data= titanic, ax = ax1)
# hue 옵션, class별로 표시
sns.barplot(x = 'sex', y = 'survived', hue = 'class', data= titanic, ax = ax2)
# hue 옵션, class별 누적으로 표시
sns.barplot(x = 'sex', y = 'survived', hue = 'class', dodge = False, data= titanic, ax = ax3)
ax1.set_title('Titanic Survived - sex')
ax2.set_title('Titanic Survived - sex/class')
ax3.set_title('Titanic Survived - sex/class(cumulated)')
plt.show()


# In[38]:


# Count plot
sns.set_style('whitegrid')

fig = plt.figure(figsize = (15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

# x축, y축에 변수를 할당
sns.countplot(x = 'class', palette = 'Set1', data= titanic, ax = ax1)   #palette는 색깔
# hue 옵션으로 who 추가(woman, man, child)
sns.countplot(x = 'class', palette = 'Pastel1', hue='who', data= titanic, ax = ax2)
sns.countplot(x = 'class', palette = 'BrBG', hue='who', dodge=False, data= titanic, ax = ax3)

ax1.set_title('Titanic Class')
ax2.set_title('Titanic Class - Who')
ax3.set_title('Titanic Class - Who(stacked)')
plt.show()


# In[45]:


# 해보기 
sns.set_style('whitegrid')

fig = plt.figure(figsize = (15,15))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

# ax1에는 Boxplot 기본값
sns.boxplot(x = 'alive', y = 'age', palette = 'BuGn', data=titanic, ax= ax1)

# ax2, Boxplot hue = sex
sns.boxplot(x = 'alive', y = 'age', palette = 'BuGn', hue = 'sex', data=titanic, ax= ax2)

# ax3, Violin Graph 기본값
sns.violinplot(x = 'alive', y = 'age', palette = 'RdBu', data=titanic, ax= ax3)

# ax4, Violin Graph 기본값, hue = sex
sns.violinplot(x = 'alive', y = 'age', palette = 'RdBu', hue = 'sex', data=titanic, ax= ax4)


ax1.set_title('Age alive')
ax2.set_title('Age alive by sex')
ax3.set_title('Violin age alive')
ax4.set_title('Violin age alive by sex')
plt.show()


# In[56]:


# joint plot : scatter plot + histogram

sns.set_style('whitegrid')

# fig = plt.figure(figsize = (15,15))
# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)
# ax4 = fig.add_subplot(2,2,4)

# j1 기본값
j1 = sns.jointplot(x = 'fare', y = 'age', data=titanic)

# j2 회귀선
j2 = sns.jointplot(x = 'fare', y = 'age', kind = 'reg', data=titanic)

# j3 육각그래프    #그리스 수, Hexa Hepta Octa Nona Deca..
j3 = sns.jointplot(x = 'fare', y = 'age', kind = 'hex', data=titanic)

# j4 커널 등고선? 밀집 그래프
j4 = sns.jointplot(x = 'fare', y = 'age', kind = 'kde', data=titanic)

j1.fig.suptitle('Titinac Fare-scatter', size = 10)
j2.fig.suptitle('Titinac Fare-Reg', size = 10)
j3.fig.suptitle('Titinac Fare-Hex', size = 10)
j4.fig.suptitle('Titinac Fare-Kde', size = 10)

plt.show()


# ### Pairplot

# In[51]:


iris = sns.load_dataset('iris')
sns.pairplot(iris, hue = 'species')
plt.title('Pairplot of Iris')
plt.show()


# 
