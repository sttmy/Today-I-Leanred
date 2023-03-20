#!/usr/bin/env python
# coding: utf-8

# In[38]:


import folium   
import pandas as pd
import json


# ## 지도 만들기

# In[2]:


# Folium   지도시각화 라이브러리
# 위도 경도로 지도에 표시

seoul_map = folium.Map(location=[37.55, 126.98], #위도, 경도값
                       zoom_start=15)


# In[3]:


seoul_map


# In[4]:


seoul_map.save('./seoul.html') # 저장


# In[8]:


seoul_map2 = folium.Map(location=[37.55, 126.98], #위도, 경도값
                       tiles = 'Stamen Terrain',  #종류: Stamen Watercolor, Stamen Toner 총 3개
                       zoom_start=12)
seoul_map2.save('./seoul2.html') # 저장


# In[9]:


seoul_map2


# In[10]:


seoul_map3 = folium.Map(location=[37.55, 126.98], #위도, 경도값
                       tiles = 'Stamen Toner',
                       zoom_start=12)
seoul_map3.save('./data1/seoul2.html') # 저장
seoul_map3


# In[30]:


data.index


# In[31]:


data = pd.read_excel('./Data/서울지역 대학교 위치.xlsx', engine = 'openpyxl')
data.columns = ['학교이름','위도','경도']
data.head()


# ### 대학교 데이터 불러오기

# ### 대학교 위치를 지도상에 표시 (위도, 경도 활용)

# In[34]:


# 서울지도 만들기
seoul_map = folium.Map(location = [37.55, 126.98], zoom_start = 12,
                      tiles = 'Stamen Terrain')


# In[35]:


# 대학교 위치정보를 Marker로 표시

for name, lat, lng in zip(data.학교이름, data.위도, data.경도):   # column명으로 가져옴
    folium.Marker([lat, lng], popup = name).add_to(seoul_map)  # popup, 클릭하면 뜨는창
    # add_to, seoul_map에 뜨도록 함


# In[36]:


seoul_map


# In[37]:


# Marker 달리해보기
for name, lat, lng in zip(data.학교이름, data.위도, data.경도):   # column명으로 가져옴
    folium.CircleMarker([lat, lng], radius = 10,    # 동그라미, 반지름 지정
                        color = 'brown', fill = True, fill_color = 'coral',   
                        fill_opacity = 0.7,    #투명도                        
                        popup = name).add_to(seoul_map2) 
seoul_map2    


# ## 지도 _ 단계구분도 그리기
# 
# https://m.blog.naver.com/flyproject/222035218795

# In[33]:


# 경기도 인구변화데이터, 데이터프레임으로 전환

df = pd.read_excel('./Data/경기도인구데이터.xlsx', engine = 'openpyxl', index_col = '구분')
df.columns = df.columns.map(str)


# In[41]:


# 경기도 시군구 경게 정보를 가진 geo-Json파일 가져오기

geo_path = './Data/경기도행정구역경계.json'
try: 
    geo_data = json.load(open(geo_path, encoding = 'utf-8'))
except:
    geo_data = json.load(open(geo_path, encoding = 'utf-8-sig'))
    
geo_data


# In[45]:


# 경기도 지도 만들기

g_map = folium.Map(location = [37.5502, 126.982], tiles = 'Stamen Terrain', zoom_start = 9)
g_map


# In[48]:


# 출력할 연도 선택 (2007~2017)

year = '2017'

# 단계구분도 (Choropleth)    단계구분도 표시하기
folium.Choropleth(geo_data = geo_data, 
                  data = df[year], 
                  columns = [df.index, df[year]],
                  fill_color = 'YlOrRd',    # YellowOrangeRed
                  fill_opacity = 0.7,        # 투명도  지도가 보여야 하니까 조절
                  line_opacity = 0.3,
                  threshold_scale = [10000,100000,300000,500000,7000000],
                  key_on = 'feature.properties.name').add_to(g_map)   #json파일 열어보고 확인
g_map


# In[49]:


# 지도를 html로 저장
g_map.save('./data1/gyonggi_population' + year +'.html')


# In[ ]:




