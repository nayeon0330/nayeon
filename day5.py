# -*- coding: utf-8 -*-
"""
1.  

    모든 범죄가 아닌  중요 범죄만 분석 : 
        '강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율'
    
    아래 파일을 이용하여 CCTV 갯수와 범죄 발생건수 및 인구수 에 대한 상관관계 분석    
        01. CCTV_result.csv / 
        02. crime_in_Seoul.csv / 02. crime_in_Seoul_include_gu_name.csv / 
        02. skorea_municipalities_geo_simple.json

    결과의 예 
    CCTV 갯수와 범죄 발생건수 / 범죄 발생건수 및 인구수 / CCTV 갯수와 인구수 상관관계 시각화
    CCTV 갯수와 범죄 발생건수 및 인구수 에 대한 상관관계 시각화
    범죄율에 대한 지도 시각화
    경찰서별 검거현황과 구별 범죄발생 현황을 시각화

2. 시계열 데이터 분석에 대하여 진행합니다..
"""

### 모듈 import
import numpy as np
import pandas as pd
import googlemaps


### 데이터 정리
## 데이터 로드 :  02. crime_in_Seoul.csv
'''
 02. crime_in_Seoul.csv 파일 분석
 1. 데이터 내의 천단위 콤마(,)
 2. 한글 Encoding : euc-kr
'''
crime_anal_police = pd.read_csv("./data/ 02. crime_in_Seoul.csv",
                                thousands=",",
                                encoding="euc-kr")


### 02. crime_in_Seoul_include_gu_name.csv
crime_anal_raw = pd.read_csv("./data/02. crime_in_Seoul_include_gu_name.csv",
                             encoding="utf-8",
                             index_col = 0 )


## 1. pivot_table()을 이용하여 '관서별' => '구별'
## 2. pivot_table()의 aggfunc=np.sum을 설정하여 동일구내의 경찰서 데이터를 합하기
crime_anal = pd.pivot_table(crime_anal_raw, index='구별', aggfunc=np.sum)


# 5대 중요 범죄에 대한 검거율을 계산하여 crime_anal에 추가
crime_anal['강간 검거율'] = crime_anal['강간 검거'] / crime_anal['강간 발생'] * 100
crime_anal['강도 검거율'] = crime_anal['강도 검거'] / crime_anal['강도 발생'] * 100
crime_anal['살인 검거율'] = crime_anal['살인 검거'] / crime_anal['살인 발생'] * 100
crime_anal['절도 검거율'] = crime_anal['절도 검거'] / crime_anal['절도 발생'] * 100
crime_anal['폭력 검거율'] = crime_anal['폭력 검거'] / crime_anal['폭력 발생'] * 100



#### 데이터 스케일링 작업 : 검거율이 100울 넘는 데이터는 100으로 변경..
col_list = ['강간 검거율', '강도 검거율','살인 검거율', '절도 검거율', '폭력 검거율']

for colum in col_list:
    crime_anal.loc[crime_anal[colum] > 100, colum] = 100
    
crime_anal.head()
crime_anal.tail()


## 컬럼명 변경 : " 강간 발생 "  => " 발생 " 부분을 삭제 => " 강간 " : DataFrame.rename('변경전' : '변경후')
crime_anal.rename(columns={'강간 발생':'강간',
                          '강도 발생':'강도',
                          '살인 발생':'살인',
                          '절도 발생':'절도',
                          '폭력 발생':'폭력'}, inplace=True)


### 비교할 데이터의 크기가 아주 심할 경우(범위가 넓을 경우), 최솟값과 최댓값에 대한 비율 전처리.
### MinMaxScalar 방법을 적용
# 데이터 스케일링을 위한 모듈 import : sklearn의 preprocessing
from sklearn import preprocessing


# preprocessing의 클래스 중 MinMaxScalar를 이용하여 전처리(데이터 스케일링)

# 1. 전처리할 데이터 설정을 위한 컬럼 추출
col = ['강간', '강도', '살인', '절도', '폭력']

# 2. 각 컬럼의 데이터를 추출
x = crime_anal[col].values

# 3. MinMaxScalar 객체 생성
min_max_scalar = preprocessing.MinMaxScaler()

# 4. MinMaxScalar 객체에 스케일링한 데이터를 전달
x_scaled = min_max_scalar.fit_transform(x.astype(float))

# 5. 결과 데이터를 데이터프레임에 저장
crime_anal_norm = pd.DataFrame(x_scaled, columns=col, index=crime_anal.index)


## crime_anal_norm에 검거율 추가
col2 = ['강간 검거율', '강도 검거율', '살인 검거율', '절도 검거율', '폭력 검거율']


crime_anal_norm[col2] = crime_anal[col2]

"""
현재까지의 작업 내용
1. 경찰서 위치 : 구글맵에게 요청하여 데이터 정리
2. 범죄 데이터 : 분석 및 시각화를 위한 데이터 정리
"""

### CCTV 데이터 로드 : 01. CCTV_result.csv
result_CCTV = pd.read_csv("./data/01. CCTV_result.csv",
                          encoding="utf-8",
                          index_col='구별')

# crime_anal_norm에게 '인구수', 'CCTV' 컬럼 추가
crime_anal_norm[['인구수', 'CCTV']] = result_CCTV[['인구수', '소계']]


## 5대 중요범죄의 합을 구하여 crime_anal_norm에게 '범죄' 컬럼을 추가
# col=['강간', '강도', '살인', '절도', '폭력']
crime_anal_norm['범죄'] = np.sum(crime_anal_norm[col], axis=1)




### ------------------ ###
### Seaborn을 이용한 시각화
### ------------------ ###

# Seaborn 및 시각화 모듈 import
import matplotlib.pyplot as plt
import seaborn as sns

import platform

# 차트에 대한 한글 방지 깨짐
path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

### 1. 강도, 살인, 폭력 : pairplot()
sns.pairplot(crime_anal_norm,
             vars=['강도', '살인', '폭력'],
             kind='reg',
             size=3)

plt.show()


### 2. ['인구수', 'CCTV'] ['살인', '강도'] : 발생 건수
sns.pairplot(crime_anal_norm,
             x_vars = ['인구수', 'CCTV'],
             y_vars = ['살인', '강도'],
             kind ='reg',
             size = 3)

plt.show()


### 3. ['인구수', 'CCTV'] ['살인 검거율', '강도 검거율']
sns.pairplot(crime_anal_norm,
             x_vars = ['인구수', 'CCTV'],
             y_vars = ['살인 검거율', '강도 검거율'],
             kind ='reg',
             size = 3)

plt.show()


###### 검거율에 대한 시각화 : heatmap()
# 검거율의 최댓값을 100으로 설정하여 heatmap()을 통한 시각화
# col2 = ['강간 검거율', '강도 검거율', '살인 검거율', '절도 검거율', '폭력 검거율']

# 검거율의 합 => crime_anal_norm
crime_anal_norm['검거'] = np.sum(crime_anal_norm[col2], axis=1)

tmp_max = crime_anal_norm['검거'].max()
# 432.593167122272

crime_anal_norm['검거'] = crime_anal_norm['검거'] / tmp_max * 100

# '검거' 컬럼을 기준으로 정렬
crime_anal_norm_sort = crime_anal_norm.sort_values(by='검거', ascending=False)  

plt.figure(figsize=(10, 10))
sns.heatmap(crime_anal_norm_sort[col2],
            annot=True,
            fmt='f',
            linewidths=0.5,
            cmap='RdPu')
plt.title('범죄 검거 비율')
plt.show()


# 범죄 발생 건수
## col = ['강간', '강도', '살인', '절도', '폭력']
crime_anal_norm['범죄'] = crime_anal_norm['범죄'] / 5
crime_anal_norm_sort = crime_anal_norm.sort_values(by='범죄', ascending=False)

plt.figure(figsize=(10, 10))
sns.heatmap(crime_anal_norm_sort[col],
            annot=True,
            fmt='f',
            linewidths=0.5,
            cmap='RdPu')
plt.title('범죄 발생 건수')
plt.show()


##### 범죄율에 대한 지도 시각화 : folium
# 지도 시각화를 위한 모듈 import
import json
import folium

# 행정구역 데이터 로드 : 02. skorea_municipalities_geo_simple.json
geo_path = "./data/02. skorea_municipalities_geo_simple.json"
geo_str = json.load(open(geo_path, encoding="utf-8"))


# 살인, 범죄 시각화
map = folium.Map(location=[37.5502, 126.982],
                 zoom_start=11,
                 title = "살인, 범죄 시각화",
                 tiles="Stamen Toner")

map.choropleth(geo_data=geo_str,
               data=crime_anal_norm['살인'],
               columns=[crime_anal_norm.index, crime_anal_norm['살인']],
               fill_color="RdPu",
               key_on="feature.id")
map.save('./result/살인.html')

import webbrowser
webbrowser.open_new('살인.html')




# 인구 대비 범죄 시각화
# 범죄 데이터를 인구로 나눈 후, 시각화
tmp_criminal = crime_anal_norm['범죄'] / crime_anal_norm['범죄'] * 1000000 # 백
# => 위도 경도가 1/1000000이기 때문에... 값을 조

map = folium.Map(location=[37.5502, 126.982],
                 zoom_start=11,
                 title = "Stamen Toner")


map.choropleth(geo_data=geo_str,
               data=tmp_criminal,
               columns=[crime_anal_norm.index, tmp_criminal],
               fill_color="RdPu",
               key_on="feature.id")

map.save('인구대비 범죄율.html')

import webbrowser
webbrowser.open_new('인구대비 범죄율.html')

# 검거 시각화
map = folium.Map(location=[37.5502, 126.982],
                 zoom_start=11,
                 title = "살인, 범죄 시각화",
                 tiles="Stamen Toner")


map.choropleth(geo_data=geo_str,
               data=crime_anal_norm['검거'],
               columns=[crime_anal_norm.index, crime_anal_norm['검거']],
               fill_color="RdPu",
               key_on="feature.id")

map.save('검거.html')

import webbrowser
webbrowser.open_new('검거.html')

# 인구대비 절도 시각화
tmp_criminal = crime_anal_norm['절도'] / crime_anal_norm['인구수'] * 1000000 # 백
# => 위도 경도가 1/1000000이기 때문에.. 값을 조절

map = folium.Map(location=[37.5502, 126.982],
                 zoom_start=11,
                 title = "Stamen Toner")


map.choropleth(geo_data=geo_str,
               data=tmp_criminal,
               columns=[crime_anal_norm.index, tmp_criminal],
               fill_color="RdPu",
               key_on="feature.id")

map.save('인구대비 절도.html')

import webbrowser
webbrowser.open_new('인구대비 절도.html')



##### 실제 지도예
# 경찰서별 검거현황과 범죄발생 현황 시각화
crime_anal_raw['lat'] = station_lat
crime_anal_raw['lng'] = station_lng

col =['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']
tmp = crime_anal_raw[col] / crime_anal_raw[col].max()

crime_anal_raw['검거'] = np.sum(tmp, axis=1)

# Map을 html 파일로 저장
map.save('각 경찰서 위치.html')

# 저장된 html 파일을 파이썬 코드로 바로 실행



## 경찰서별 검거율(분포 형태) 표시
# Map 객체
