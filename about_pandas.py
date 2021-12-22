# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 9:00 2021

데이터 자료구조 : Pandas 정리

Numpy가 2차원 행렬 형태의 데이터를 지원하지만,
Numpy는 데이터의 속성을 표시하는 행위나 열의 레이블을 가지고 있지 않다는 것이 한계.

Pandas는 이러한 문제를 해결할 수 있다..

Pandas의 특징
1. 빠르고 효율적이며 표현을 갖춘 자료 구조
   실세계 데이터 분석을 위해 만들어진 패키지
   
2. 다양한 형태의 데이터에 적합 (Numpy는 하나의 데이터형만 보유 가능)
   이종(서로 다른)자료형의 열을 가진 테이블 데이터
   시계열 데이터
   레이블을 가진 다양한 행렬 형태의 데이터
   다양한 관측 통계 데이터

3. Pandas의 핵심 구조
   Series : 1차원 구조를 가진 하나의 열
   DataFrame : 복수의 열(Series)를 가진 2차원 형태의 데이터

4. Pandas 만의 수행
   결측(NaN) 데이터 처리
   데이터 추가 및 삭제(새로운 열 추가 및 특정 열의 삭제 등..)
   데이터 정렬 및 다양한 데이터 조작
"""

# Pandas로 할 수 있는일
"""
1. 파이썬의 기본 자료구조인 리스트, 딕셔너리, Numpy 배열을 데이터프레임으로 변환 가능.
2. CSV / XLS 파일 등을 열어 작업 가능
3. URL을 통해 웹 사이트의 csv, json, 과 같은 원격데이터 또는 데이터베이스를 열 수 있다.

4. 데이터 보기 및 검사 가능
   mean() : 모든 열의 평균 계산 가능
   corr() : 데이터프레임의 열 사이의 상관관계를 계산
   count(): 각 데이터프레임의 열에 대한 갯수 가능(단, null이 아닌 값들)
   
5. 필터 및 정렬 그리고 그룹화
   sort_values() : 데이터 정렬
   조건을 이용한 필터링
   groupby() : 기준에 따라 몇개의 그룹으로 데이터 분할 가능.
   
6. 데이터 경제
   데이터의 누락값 확인 가능
   특정한 값을 다른 값으로 대체 가능   

* 참고 : Pandas는 panel data 라는 용어에서 출발
  계량경제학에서 사용되는 용어로서
  관찰자에 의해서 여러 회에 걸쳐 관측된 데이터 집합를 지칭.
"""




### CSV 파일에 대하여
"""
CSV 파일은 테이블 형태의 데이터를 저장하고, 사용하는데 구조화된 텍스트 파일
CSV 파일은 "," 구분 / "탭" 으로 구분하여 제공되기 때문에,
           사용 전에 미리 원시(raw) 데이터 확인이 필요.
           또한, 인코딩 부분도 확인이 필요.

CSV 파일의 구성 : 필드를 나타내는 열과 
                 레코드를 나타내는 행으로 구성
                 
만약, 데이터 중간에 구분자가 포함되어야 한다면 ""를 이용하여 필드를 묶어야 한다.
ex. 'GilDong Hong' 이라는 데이터가 있고 데이터 중간에, 포함되어야 한다고 가정.
     구분자로 사용되는 쉼표와 구분하기 위해
     반드시 데이터를 ""로 묶어야 한다..                  

CSV 파일의 첫번째 레코드(행)에는 열 제목이 포함되어 있을 수 있다.
따라서 열 제목이 어떤 구조로 되어있는지를 사전에 파악하고, 읽어들여야 작업이 용이.

CSV 파일의 크기를 알 수 없고, 잠재적으로 크기가 큰 경우,
한번에 모든 레코드를 읽지 않고 여러번 나누어 읽는 것이 좋다. (특히, 원격 데이터의 경우)
현재 행을 읽고, 현재 행을 처리한 후, 삭제한 후에 다음 행을 읽는 방식.

또, 다른 방법은

특정 크기만큼의 데이터를 읽고 처리한 후,
동일한 크기의 데이터를 읽는 방식을 사용할 수도 있다.
"""



### 파이썬이 제공하는 CSV 모듈 : csv
# ./data/csv/weather.csv : 울릉도 데이터
import csv

# 1. open()를 이용하여 대상파일 열기
f = open('./data/csv/weather.csv')

# 2. csv 모듈의 reader() 함수를 이용하여 대상 파일 읽기 
data = csv.reader(f)

# header (일시,평균기온(°C), 최대 풍속(m/s), 평균 풍속(m/s))을 건너뛰기
header = next(data)

# 3. 읽은 데이터 처리 (변수에 저장했을 경우에는 차후 처리도 가능)
for row in data:
    print(row)

# 4. 파일 닫기
f.close()


## CSV 파일에서 원하는 데이터 추출 : 인덱스를 이용
f = open('./data/csv/weather.csv')
data = csv.reader(f)
header = next(data)

# 만약, 평균 풍속(m/s) 관한 데이터만 추출할 경우 해당열의 index를 이용하여 지정
for row in data:
    # 열에 해당하는 인덱스를 지정
    print(row[3], end=',')
f.close()

# 평균 풍속에 대한 최대 값을 구할 경우
f = open('./data/csv/weather.csv')
data = csv.reader(f)
header = next(data)

max_wind = 0.0

for row in data:
    if row[3] =='':                 # 평균 풍속의 데이터가 없을 경우
        wind = 0                    # 0으로 처리
    else:
        wind = float(row[3])        # 평균 풍속 데이터가 있을 경우, 실수로 반환

    if max_wind < wind:             # 기존 최대 평균 풍속값과 새로운 평균 풍속값 비교
        max_wind = wind             # 현재까지의 최대 평균 풍속값보다 크면 새로운 값을 저장
        
print('최대 풍속은 : ', max_wind, 'm/s')        
'''
최대 풍속은 :  14.9 m/s
'''



### 울릉도는 몇 월에 바람이 가장 강한지 확인
"""
작업 내용
1. 울릉도 데이터 파일 읽기
2. header 부분은 제외하고 데이터 처리
3. 매달 풍속을 저장한 리스트 선언
4. 각 달마다 측정된 일 수를 저장한 리스트 선언

반복해서 해야 할 일들 첫번째
    5. 첫번째 열에서 달 정보 추출
    6. 풍속 데이터 존재 여부 확인
    7. 풍속 데이터 추출
    8. 해당 달의 풍속 데이터 추가
    9. 해당 달의 일수를 증가
    
반복해서 해야 할 일들 두번째
    10. 일수로 나누어 월 평균 구하기  
"""  

"""
열     : 일시,평균기온(°C), 최대 풍속(m/s), 평균 풍속(m/s)
레코드 : 2010-08-01 ~~ 2020-07-31
"""

import csv

# 1. 울릉도 데이터 파일 읽기
f = open("./data/csv/weather.csv")
data = csv.reader(f)

# 2. header 부분은 제외하고 데이터 처리
header = next(data)

# 3. 매달 풍속을 저장한 리스트 선언
monthly_wind = [0 for x in range(12)]

# 4. 각 달마다 측정된 일 수를 저장한 리스트 선언
days_counted = [0 for x in range(12)]

# 반복해서 해야 할 일들 첫번째
for row in data:
    month = int(row[0][5:7])          # "2010-08-01" => "08" => 8
    
    if row[3] != '':
        wind = float(row[3])
        monthly_wind[month-1] += wind
        days_counted[month-1] += 1

# 반복해서 해야 할 일들 두번째
for i in range(12):
    # monthly_wind[i] = monthly_wind[i] / days_counted[i]
      monthly_wind[i] != days_counted[i]
      
# 시각화 작업 : matplotlib
import matplotlib.pyplot as plt      

plt.plot(monthly_wind, 'blue')

f.close()

### Pandas로 CSV 파일 읽기 : Pandas 모듈의 read_csv() 함수를 사용하여 DataFrame으로 저장
import pandas as pd
df = pd.read_csv("./data/csv/weather.csv", encoding='CP949')

"""
Pandas의 데이터 구조

Pandas는 데이터를 저장하기 위해 2가지의 기본 데이터 구조를 제공.
이 데이터 구조는 모두 Numpy 배열을 이용하여 구현된다.
    따라서 속도가 빠르고, 
    모든 데이터 구조는 값 변경이 가능.
    시리즈를 제외하고는 크기 변경도 가능.

각 행과 열은 이름이 부여되며
    행의 이름을 index,
    열의 이름을 columns라 호칭.
    
Series : 1차원 구조    
         레이블이 붙어있는 1차원 vector 형태.
DataFrame : 2차원 구조
            행과 열로 되어있는 2차원 테이블.
            각 열은 Series로 구성되어 있다.
"""

# 특정 열을 인덱스로 설정하여 읽기 : read_csv("경로 및 파일", index_col="인덱스로 지정할 열 이름")
"""
Pandas의 read_csv() 함수는 인덱스 지정없이 파일을 읽을 경우
파일의 첫번째 행을 각 시리즈의 열이름으로 자동 설정하고,
갈 레코드에 대한 인덱스를 0으로 시작하는 정수를 이용하여 자동 생성한다.
"""
df = pd.read_csv("./data/csv/weather.csv", encoding='CP949')
'''
index 자동 부여
'''

df = pd.read_csv("./data/csv/weather.csv", encoding='CP949', index_col=0)
'''
index를 "일시" 데이터로 설정
'''



### countries.csv를 읽기
"""
,country,area,capital,population
KR,Korea,98480,Seoul,51780579
US,USA,9629091,Washington,331002825
JP,Japan,377835,Tokyo,125960000
CN,China,9596960,Beijing,1439323688
RU,Russia,17100000,Moscow,146748600
"""

df_no_index = pd.read_csv("./data/csv/countries.csv")

# countries.csv의 첫번째 열을 index로 설정
df_my_index = pd.read_csv("./data/csv/countries.csv", index_col=0)



### 열을 기준으로 데이터 선택 : 열 이름을 이용(DataFrame['열이름'])
# 즉, 특정 열에 대한 데이터를 선택할 경우, 데이터프레임에 대괄호를 이용하여 열을 선택
print(df_my_index['population'])
'''
KR      51780579
US     331002825
JP     125960000
CN    1439323688
RU     146748600
Name: population, dtype: int64
'''



### 두개의 열을 선택하여 데이터를 선택 : 각 열의 이름을 리스트로 설정
# DataFrame[['열 이름', '열 이름']]
print(df_my_index[['population', 'area']])
'''
    population      area
KR    51780579     98480
US   331002825   9629091
JP   125960000    377835
CN  1439323688   9596960
RU   146748600  17100000
'''




#### 특정 인코딩으로 되어있는 csv 파일을 Pandas.read()로 읽기
weather_no_encoding = pd.read_csv("./data/csv/weather.csv")
'''
인코딩이 맞지 않을 경우 오류 발생
UnicodeDecodeError:'utf-8' codec can't decode byte 0xc0 in position 0: invalid start byte
'''

weather_encoding = pd.read_csv("./data/csv/weather.csv", encoding='CP949')




#### 데이터프레임 : 행 선택(head() / tail())
"""
head() : 읽은 데이터 중 처음 5개 행만 선택   (기본값이 아닌 행의 수 지정 가능)
tail() : 읽은 데이터 중 마지막 5개 행만 선택
"""

countries_df = pd.read_csv("./data/csv/countries.csv", index_col=0)
'''
 country      area     capital  population
KR   Korea     98480       Seoul    51780579
US     USA   9629091  Washington   331002825
JP   Japan    377835       Tokyo   125960000
CN   China   9596960     Beijing  1439323688
RU  Russia  17100000      Moscow   146748600
'''

countries_df.head(2)
'''
 country     area     capital  population
KR   Korea    98480       Seoul    51780579
US     USA  9629091  Washington   331002825
'''

countries_df.tail(3)
'''
   country      area  capital  population
JP   Japan    377835    Tokyo   125960000
CN   China   9596960  Beijing  1439323688
RU  Russia  17100000   Moscow   146748600
'''


## Pandas도 슬라이싱을 이용하여 행 선택 가능 : DataFrame[ : ]
countries_df[ :3]
'''
 country     area     capital  population
KR   Korea    98480       Seoul    51780579
US     USA  9629091  Washington   331002825
JP   Japan   377835       Tokyo   125960000
'''


## 특정 행의 레이블만 선택할 경우 : loc를 이용하여 선택
countries_df.loc['US']
'''
country              USA    <= 'US' 행의 첫번째 열과 데이터
area             9629091    
capital       Washington
population     331002825
Name: US, dtype: object     <= 선택한 행의 레이블 및 전체 데이터형
'''


## 데이터프레임에서 특정 요소 하나만 선택할 경우 : loc['행', '열']
countries_df.loc['US', 'capital']
'''
'Washington'
'''


## 특정 열에 대한 행을 선택할 경우 : DataFrame['열'][행]
#  ex. 'population' 열의 상위 3개 행인 KR / US / JP 에 해당하는 데이터 선택
countries_df['population'][:3]
'''
KR     51780579
US    331002825
JP    125960000
Name: population, dtype: int64
'''



### 기존 데이터프레임에 새로운 열을 추가할 경우 : DataFrame['신규 컬럼(열)'] = 신규 데이터
#   ex. countries_df 데이터프레임에 인구밀도를 나타내는 컬럼을 추가할 경우
#       인구밀도 = 인구 / 면적
countries_df['density'] = countries_df['population'] / countries_df['area']
'''
   country      area     capital  population     density
KR   Korea     98480       Seoul    51780579  525.797918
US     USA   9629091  Washington   331002825   34.375293
JP   Japan    377835       Tokyo   125960000  333.373033
CN   China   9596960     Beijing  1439323688  149.977044
RU  Russia  17100000      Moscow   146748600    8.581789

위와 같이 새로운 열을 추가하면 항상 맨 뒤에 컬럼이 추가된다!!!!
'''

"""
countries_df['population'] / countries_df['area'] 와 같이

데이터프레임의 어떤 열이 다른 열들의 값에 의해 결정될때

주의사항 : 행별로 반복하여 연산을 처리하는 것이 아니라,
           필요한 열을 통째로 접근하여 한번에 계산이 이루어진다!!!!!
"""



### Pandas 제공 함수를 이용한 간단한 데이터 분석
"""
describe() : 데이터프레임에 대한 간단한 요약 
mean()     : 데이터프레임의 평균
std()      : 데이터프레임의 표준편차
"""

weather_df = pd.read_csv("./data/csv/weather.csv", encoding="CP949")
weather_df.head()
'''
         일시  평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
0  2010-08-01      28.7         8.3         3.4
1  2010-08-02      25.2         8.7         3.8
2  2010-08-03      22.1         6.3         2.9
3  2010-08-04      25.3         6.6         4.2
4  2010-08-05      27.2         9.1         5.6
'''
# 만약 일시를 index로 지정할 경우
weather_df = pd.read_csv("./data/csv/weather.csv", index_col=0, encoding="CP949")
weather_df.head()
'''
   평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
일시                                          
2010-08-01      28.7         8.3         3.4
2010-08-02      25.2         8.7         3.8
2010-08-03      22.1         6.3         2.9
2010-08-04      25.3         6.6         4.2
2010-08-05      27.2         9.1         5.6
'''

weather_df.describe()
'''
아래처럼 간단한 요약 통계를 알 수 있다.
 
          평균기온(°C)   최대 풍속(m/s)   평균 풍속(m/s)
count  3653.000000  3649.000000  3647.000000      <= null이 아닌 레코드 갯수
mean     12.942102     7.911099     3.936441      <= 각 열에 대한 평균
std       8.538507     3.029862     1.888473      <= 각 열에 대한 표준편차
min      -9.000000     2.000000     0.200000      <= 각 열에 대한 최솟값
25%       5.400000     5.700000     2.500000      <= 각 열에 대한 1사분위
50%      13.800000     7.600000     3.600000      <= 각 열에 대한 2사분위
75%      20.100000     9.700000     5.000000      <= 각 열에 대한 3사분위
max      31.300000    26.000000    14.900000      <= 각 열에 대한 최댓값
'''

# 별도의 함수를 이용하여 특정 통계값만 계산 가능
weather_df.mean()
'''
평균기온(°C)      12.942102
최대 풍속(m/s)     7.911099
평균 풍속(m/s)     3.936441
dtype: float64
'''

weather_df.std()
'''
평균기온(°C)      8.538507
최대 풍속(m/s)    3.029862
평균 풍속(m/s)    1.888473
dtype: float64
'''

weather_df.min()
'''
평균기온(°C)     -9.0
최대 풍속(m/s)    2.0
평균 풍속(m/s)    0.2
dtype: float64
'''

weather_df.max()
'''
평균기온(°C)      31.3
최대 풍속(m/s)    26.0
평균 풍속(m/s)    14.9
dtype: float64
'''

weather_df.count()
'''
평균기온(°C)      3653
최대 풍속(m/s)    3649
평균 풍속(m/s)    3647
dtype: int64
'''



### 특정 컬럼에 대한 통계도 가능
pandas_std = weather_df['평균기온(°C)'].std()
'''
 8.53850701475343
'''



### Numpy 함수 이용도 가능
import numpy as np
numpy_std = np.std(weather_df['평균기온(°C)'])
'''
8.537338236838877
'''

"""
참고 : pandas 와 numpy 함수는 계산방식이 다르기 때문에 
       위와 같이 동일한 데이터에 대한 표준편차를 구하더라도 차이는 있을 수 있다!!!!!
"""




#### Pandas 집계함수를 이용한 데이터프레임 분석
weather_df.count()
'''
평균기온(°C)      3653
최대 풍속(m/s)    3649
평균 풍속(m/s)    3647
dtype: int64
'''

weather_df['최대 풍속(m/s)'].count()
'''
데이터프레임의 '최대 풍속(m/s)'컬럼에 대한 통계
 3649
'''

weather_df[['최대 풍속(m/s)', '평균기온(°C)']].count()
'''
데이터프레임의 '최대 풍속(m/s)' 과 '평균기온(°C)' 컬럼에 대한 통계

최대 풍속(m/s)    3649
평균기온(°C)      3653
dtype: int64
'''

weather_df.count()[['최대 풍속(m/s)', '평균기온(°C)']]
'''
위와 같은 형식으로 사용도 가능

최대 풍속(m/s)    3649
평균기온(°C)      3653
dtype: int64
'''




#### Pandas를 이용한 울릉도 바람세기 분석 및 시각화
# 1. 사용 모듈 import
import pandas as pd
import matplotlib.pyplot as plt

# 2. 분석할 데이터 읽기
weather = pd.read_csv("./data/csv/weather.csv", encoding="CP949")
weather.head(2)
'''
          일시  평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
0  2010-08-01      28.7         8.3         3.4
1  2010-08-02      25.2         8.7         3.8
'''

weather.tail(2)
'''

             일시  평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
3651  2020-07-30      22.9         9.7           2.4
3652  2020-07-31      25.7         4.8           2.5
'''

# 3. 분석시 필요한 데이터 저장 리스트 선언
# 월별로 구분된 12개 데이터를 저장할 리스트
monthly = [0 for x in range(12)]
'''
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''

# 각 월별 평균 풍속을 저장할 리스트 
monthly_wind = [0 for x in range(12)]
'''
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''

# 4. '일시' 컬럼의 데이터에서 2020-07-30 부분을 DataTime 형식의 index를 만들어서
#     데이터프레임에 신규컬럼('month')에 추가
weather['month'] = pd.DatetimeIndex(weather['일시']).month
weather.head()
'''
         일시  평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)  month
0  2010-08-01      28.7         8.3           3.4             8
1  2010-08-02      25.2         8.7           3.8             8
2  2010-08-03      22.1         6.3           2.9             8
3  2010-08-04      25.3         6.6           4.2             8
4  2010-08-05      27.2         9.1           5.6             8
'''

# 5. 월별로 분리하여 저장 테스트
# 모든 해의 1월에 해당하는 데이터 추출하여 저장
monthly[0] = weather[weather['month'] == 1]
monthly[0].mean()
'''
평균기온(°C)      1.598387
최대 풍속(m/s)    8.158065
평균 풍속(m/s)    3.757419
month         1.000000
dtype: float64
'''

# 모든 해의 2월에 해당하는 데이터 추출하여 저장
monthly[1] = weather[weather['month'] == 2]


monthly[1].mean()
'''
평균기온(°C)      2.136396
최대 풍속(m/s)    8.225357
평균 풍속(m/s)    3.946786
month         2.000000
dtype: float64
'''

# 6. 전체 데이터를 이용하여 1 ~ 12월까지의 평균 풍속을 저장
for i in range(12):    # i => 0 ~ 11
    monthly[i] = weather[weather['month'] == i+1]
    monthly_wind[i] = monthly[i].mean()['평균 풍속(m/s)']
    
# 7. matplotlib를 이용한 간단한 시각화
plt.plot(monthly_wind, 'red')
plt.show()



### Pandas : 그룹핑 / 필터링 / 결측치 삭제 및 보정 / 데이터 구조 변경 / 합 / 연결 / 병합 / 정렬



### Pandas를 이용한 그룹핑
"""
그룹핑 : 데이터를 특정 값에 기반하여 묶는 기능
Pandas.groupby() 함수를 이용

groupby()에 넘겨줄 값은 그룹을 묶을때 사용할 열(컬럼)이름
해당 컬럼의 데이터가 동일할 경우, 그룹으로 묶인다..
그리고 여기에 집계함수를 적용하면 그룹별 통계치를 구할 수 있다.
"""

# 1. 사용 모듈 import
import pandas as pd
import matplotlib.pyplot as plt

# 2. 분석할 데이터 읽기
weather = pd.read_csv("./data/csv/weather.csv", encoding="CP949")
weather.head(2)
'''
       일시  평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
0  2010-08-01      28.7         8.3         3.4
1  2010-08-02      25.2         8.7         3.8
'''

weather['month'] = pd.DatetimeIndex(weather['일시']).month
weather.head(2)
'''    일시      평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)  month
   0  2010-08-01      28.7         8.3         3.4              8
   1  2010-08-02      25.2         8.7         3.8              8                 
'''

# 월별 평균값
means = weather.groupby('month').mean()
'''
    평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
month                                   
1       1.598387    8.158065    3.757419
2       2.136396    8.225357    3.946786
3       6.250323    8.871935    4.390291
4      11.064667    9.305017    4.622483
5      16.564194    8.548710    4.219355
6      19.616667    6.945667    3.461000
7      23.328387    7.322581    3.877419
8      24.748710    6.853226    3.596129
9      20.323667    6.896333    3.661667
10     15.383871    7.766774    3.961613
11      9.889667    8.013333    3.930667
12      3.753548    8.045484    3.817097
'''

# 월별 합
sums = weather.groupby('month').sum()
'''
      평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
month                                  
1         495.5      2529.0      1164.8
2         604.6      2303.1      1105.1
3        1937.6      2750.3      1356.6
4        3319.4      2782.2      1377.5
5        5134.9      2650.1      1308.0
6        5885.0      2083.7      1038.3
7        7231.8      2270.0      1202.0
8        7672.1      2124.5      1114.8
9        6097.1      2068.9      1098.5
10       4769.0      2407.7      1228.1
11       2966.9      2404.0      1179.2
12       1163.6      2494.1      1183.3
'''



### 울릉도는 몇월에 바람이 가장 강한지?? : groupby()를 이용
# 1. 사용 모듈 import
import pandas as pd
import matplotlib.pyplot as plt

# 2. 분석할 데이터 읽기
weather = pd.read_csv("./data/csv/weather.csv", encoding="CP949")


weather['month'] = pd.DatetimeIndex(weather['일시']).month


means = weather.groupby('month').mean()

means['평균 풍속(m/s)'].plot()
plt.show()



### Pandas를 이용한 필터링 
"""
조건에 맞는 데이터 추출
ex. weather 데이터프레임에서 '최대 풍속(m/s)' 컬럼으로 되어있는 열의 값이
    10.0을 넘는지 확인하여 참과 거짓을 도출할때...
    
이 방법은 Numpy의 논리 인덱싱 동일..    
"""

weather['최대 풍속(m/s)'].head()
'''
0    8.3
1    8.7
2    6.3
3    6.6
4    9.1
Name: 최대 풍속(m/s), dtype: float64
'''

weather['최대 풍속(m/s)'] >= 10.0
'''
0       False
1       False
2       False
3       False
4       False
     ~~~
'''

weather['평균기온(°C)'] >= 30.0
'''
0       False
1       False
2       False
3       False
4       False
     ~~~
'''



### Pandas를 이용한 결측치(결손값) 확인하고 삭제
"""
데이터 과학자가 사용하는 실제 데이터는
완벽하지 않고, 상당한 수의 결측치를 가지고 있거나 이상치(의심스러운 값)를 가지고 있다.

결측치가 발생하는 이유
    1. 데이터가 처음부터 수집되지 않았을 경우
    2. 측정 기기의 고장
    3. 사건 사고가 발생한 경우
    
따라서 데이터를 분석(처리)하기 전에 반드시 거쳐야 할 작업이 데이터 정제 작업!!!

Pandas는 이와같이 결측치를 NaN(NA)으로 나타낸다.

Pandas의 isna()를 이용하면 결측치를 검사할 수 있다.    
"""

# 1. 사용 모듈 import
import pandas as pd
import matplotlib.pyplot as plt

# 2. 분석할 데이터 읽기
weather = pd.read_csv("./data/csv/weather.csv", encoding="CP949")

missing_data1 = weather[weather['평균기온(°C)'].isna()]
'''
Empty DataFrame
Columns: [일시, 평균기온(°C), 최대 풍속(m/s), 평균 풍속(m/s)]
Index: []
'''

missing_data2 = weather[weather['최대 풍속(m/s)'].isna()]
'''
           일시  평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
559   2012-02-11      -0.7         NaN         NaN
560   2012-02-12       0.4         NaN         NaN
561   2012-02-13       4.0         NaN         NaN
3183  2019-04-19       7.8         NaN         2.3

=> 최대 풍속(m/s)이 기록되지 않은 날은 4일
'''

missing_data3 = weather[weather['평균 풍속(m/s)'].isna()]
'''
          일시  평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
559   2012-02-11      -0.7         NaN         NaN
560   2012-02-12       0.4         NaN         NaN
561   2012-02-13       4.0         NaN         NaN
1694  2015-03-22      10.1        11.6         NaN
1704  2015-04-01       7.3        12.1         NaN
3182  2019-04-18      15.7        11.7         NaN
=> 평균 풍속(m/s)이 기록되지 않은 날은 4일
'''



### Pandas를 이용한 결측치 삭제 : dropna()
"""
dropna(axis=0, how='any', inplace=False)
    axis    : 0일 경우, 결측치를 포함한 행을 삭제
              1일 경우, 결측치를 포함한 열을 삭제
    how     : any일 경우, 결측치가 하나라도 포함되고 있으면 제거 대상
              all일 경우, 행 또는 열의 모든 데이터가 결측치일때만 경우 제거 대상
           
    inplace : True일 경우, 원본 데이터에서 결측치를 제거
              False일 경우, 원본 데이터는 그대로 유지하고, 수정된 데이터만 데이터프레임으로 반환
"""

# 1. 사용 모듈 import
import pandas as pd
import matplotlib.pyplot as plt

# 2. 분석할 데이터 읽기
weather = pd.read_csv("./data/csv/weather.csv", encoding="CP949")

missing_data = weather[weather['최대 풍속(m/s)'].isna()]
'''
           일시  평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
559   2012-02-11      -0.7         NaN         NaN
560   2012-02-12       0.4         NaN         NaN
561   2012-02-13       4.0         NaN         NaN
3183  2019-04-19       7.8         NaN         2.3
'''

# 행의 데이터 중에 하나라도 결측치가 발견되면 
# 해당 행을 삭제하고 기존 데이터프레임 수정
weather.dropna(axis=0, how='any', inplace=True)
missing_data = weather[weather['최대 풍속(m/s)'].isna()]
'''
Empty DataFrame
Columns: [일시, 평균기온(°C), 최대 풍속(m/s), 평균 풍속(m/s)]
Index: []
'''

# 행의 데이터 중에 하나라도 결측치가 발견되면 
# 해당 행을 삭제하고 기존 데이터프레임은 유지하고 결과값만 데이터프레임으로 반환
weather.dropna(axis=0, how='any', inplace=False)
missing_data = weather[weather['최대 풍속(m/s)'].isna()]
'''
            일시  평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
559   2012-02-11      -0.7         NaN           NaN
560   2012-02-12       0.4         NaN           NaN
561   2012-02-13       4.0         NaN           NaN
3183  2019-04-19       7.8         NaN           2.3
'''

# 행의 데이터가 모두 결측치일 경우에만
# 해당 행을 삭제하고 기존 데이터프레임 수정
weather.dropna(axis=0, how='all', inplace=True)
missing_data = weather[weather['최대 풍속(m/s)'].isna()]
'''
           일시  평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
559   2012-02-11      -0.7         NaN         NaN
560   2012-02-12       0.4         NaN         NaN
561   2012-02-13       4.0         NaN         NaN
3183  2019-04-19       7.8         NaN         2.3
'''

# 열의 데이터 중 하나라도 결측치가 발견되면
# 해당 열을 삭제하고 기존 데이터프레임 수정
weather.dropna(axis=1, how='any', inplace=True)
missing_data = weather[weather['최대 풍속(m/s)'].isna()]
'''
=> NaN값이 1개라도 있으면 오류 발생
KeyError: '최대 풍속(m/s)'
'''

missing_data = weather[weather['평균 풍속(m/s)'].isna()]
'''
=> NaN값이 1개라도 있으면 오류 발생
KeyError: '평균 풍속(m/s)'
'''



### Pandas를 이용한 결측치 보정 : fillna()
"""
결측치가 발견되면 지정한 값으로 대체
fillna(채울(대체할)값, inplace=False)

* 참고 : inplace의 기본값은 False
"""

# 1. 사용 모듈 import
import pandas as pd
import matplotlib.pyplot as plt

# 2. 분석할 데이터 읽기
weather = pd.read_csv("./data/csv/weather.csv", encoding="CP949")
missing_data = weather[weather['평균 풍속(m/s)'].isna()]
'''
             일시  평균기온(°C)  최대 풍속(m/s)  평균 풍속(m/s)
559   2012-02-11      -0.7         NaN           NaN
560   2012-02-12       0.4         NaN           NaN
561   2012-02-13       4.0         NaN           NaN
1694  2015-03-22      10.1        11.6           NaN
1704  2015-04-01       7.3        12.1           NaN
3182  2019-04-18      15.7        11.7           NaN
'''

# 결측치가 발견되면 0으로 채우기
weather.fillna(0, inplace=True)

# 최대 풍속(m/s) 컬럼의 결측치를 최대 풍속(m/s)의 평균값으로 채우기
weather = pd.read_csv("./data/csv/weather.csv", encoding="CP949")
weather['최대 풍속(m/s)'].fillna(weather['최대 풍속(m/s)'].mean(), inplace=True)

# 평균 풍속(m/s) 컬럼의 결측치를 평균 풍속(m/s)의 평균값으로 채우기
weather = pd.read_csv("./data/csv/weather.csv", encoding="CP949")
missing_data = weather[weather['평균 풍속(m/s)'].isna()]

weather['평균 풍속(m/s)'].fillna(weather['평균 풍속(m/s)'].mean(), inplace=True)
weather[weather['일시'] == '2012-02-11']
print(weather.loc['2012-02-11'])



### 데이터프레임 구조 변경
"""
데이터프레임을 CSV 또는 XML 파일을 읽어서 생성할 수도 있지만,
때에 따라서는 리스트나, 딕셔너리를 이용하여 생성할 수도 있다.

데이터프레임을 가장 쉽게 생성하는 방법은 파이썬의 딕셔너리를 이용.

파이썬의 딕셔너리를 이용하여 데이터프레임을 생성하면
    딕셔너리의 키는 데이터프레임의 컬럼명(열의 레이블)으로 되고,
    딕셔너리의 키에 해당하는 값을 채우는 데이터를 가진 리스트가 된다.
    
즉, 딕셔너리의 한 항목이 시리즈 데이터가 되는 것!!!    
"""

# 딕셔너리를 이용한 데이터프레임 생성
df_1 = pd.DataFrame({'item' : ['ring0', 'ring0', 'ring1', 'ring1'], 
                     'type' : ['Gold', 'Silver', 'Gold', 'Bronze'], 
                     'price': [20000, 10000, 50000, 30000]})
'''
    item    type  price    <= 'item' / 'type' / 'price' 는 컬럼명
0  ring0    Gold  20000
1  ring0  Silver  10000
2  ring1    Gold  50000
3  ring1  Bronze  30000
'''

# 데이터프레임 구조 변경
"""
pivot(index='', columns='', values='')
    index   : 데이터프레임의 index로 사용될 컬럼
    colunms : 데이터프레임의 컬럼명으로 사용될 컬럼
    values  : 데이터프레임의 데이터로 사용될 컬럼

ex. 위의 데이터프레임에서 
     index는 'item'
     columns 는 'type'
     values는 'price' 로 설정하여 데이터프레임의 구조를 변경 했을 경우
"""

pivot_df = df_1.pivot(index='item', columns='type', values='price')
'''
type    Bronze     Gold   Silver    <= 컬럼명을 기존 'type' 컬럼의 데이터로 설정
item                                <= 
ring0      NaN  20000.0  10000.0    <= ring0에 해당하는 Bronze 값이 없기때문에...
ring1  30000.0  50000.0      NaN    <= ring1에 해당하는 Silver 값이 없기때문에...

index를 기존 'item'으로 설정했을 경우, 중복된는 ring0와 ring1는 합해져서 하나로 생성
'''



### 데이터프레임 합하기 (즉 연결) : concat([데이터프레임, 데이터프레임])
df_1 = pd.DataFrame( {'A' : ['a10', 'a11', 'a12'], 
                      'B' : ['b10', 'b11', 'b12'],
                      'C' : ['c10', 'c11', 'c12']} , index = ['가', '나',  '다'] )

df_2 = pd.DataFrame( {'B' : ['b23', 'b24', 'b25'],
                      'C' : ['c23', 'c24', 'c25'],
                      'D' : ['d23', 'd24', 'd25']} , index = ['다', '라',  '마'] )

concat_df1 = pd.concat([df_1, df_2])
'''
     A    B    C    D
가  a10  b10  c10  NaN   <= df_1에는 D 컬럼이 없기때문에 
나  a11  b11  c11  NaN   <= df_1에는 D 컬럼이 없기때문에 
다  a12  b12  c12  NaN   <= df_1에는 D 컬럼이 없기때문에 
다  NaN  b23  c23  d23   <= df_1에는 A 컬럼이 없기때문에 
라  NaN  b24  c24  d24   <= df_1에는 A 컬럼이 없기때문에 
마  NaN  b25  c25  d25   <= df_1에는 A 컬럼이 없기때문에 
'''

concat_df2 = pd.concat([df_2, df_1])
'''
     B    C    D    A
다  b23  c23  d23  NaN
라  b24  c24  d24  NaN
마  b25  c25  d25  NaN
가  b10  c10  NaN  a10
나  b11  c11  NaN  a11
다  b12  c12  NaN  a12
'''



### 참고
"""
일반적으로 데이터들은 하나의 큰 테이블로 저장되지 않고,
여러개의 작은 테이블로 나뉘어서 저장되는 경우가 많다.

여러개의 작은 테이블로 저장하여 제공하는 이유 
    1. 데이터 제공 속도
    2. 관리에 대한 편의성
    3. 데이터 수집의 시기, 주체 등이 달라 별도로 생성되는 경우가 많기 때문에..
    
Pandas.concat(df_list, axis=0, join='outer')   <= 각 옵션에 대한 기본값
    df_list : 합할 데이터프레임 리스트
    axis    : 0일 경우, 행을 늘려서 합해진다. (즉, 행 기준)
              1일 경우, 열을 늘려서 합해진다. (즉, 열 기준)
    join    : 합 할때 레이블을 어떻게 사용할 지를 결정
              outer일 경우, 레이블들의 합집합으로 생성
              inner일 경우, 레이블들의 교집합으로 생성
"""



### 다양한 방법으로 합하기
df_1 = pd.DataFrame( {'A' : ['a10', 'a11', 'a12'], 
                      'B' : ['b10', 'b11', 'b12'],
                      'C' : ['c10', 'c11', 'c12']} , index = ['가', '나',  '다'] )

df_2 = pd.DataFrame( {'B' : ['b23', 'b24', 'b25'],
                      'C' : ['c23', 'c24', 'c25'],
                      'D' : ['d23', 'd24', 'd25']} , index = ['다', '라',  '마'] )

# 열 기준으로 교집합 : axis=1, join='inner'
df_axis1_inner = pd.concat([df_1, df_2], axis=1, join='inner')
'''
     A    B    C     B    C   D
다  a12  b12  c12  b23  c23  d23
'''

# 열 기준으로 합집합 : axis=1, join='outer'
df_axis1_inner = pd.concat([df_1, df_2], axis=1, join='outer')
'''
     A    B    C    B    C    D
가  a10  b10  c10  NaN  NaN  NaN
나  a11  b11  c11  NaN  NaN  NaN
다  a12  b12  c12  b23  c23  d23
라  NaN  NaN  NaN  b24  c24  d24
마  NaN  NaN  NaN  b25  c25  d25
'''

# 행 기준으로 교집합 : axis=0, join='inner'
df_axis0_inner = pd.concat([df_1, df_2], axis=0, join='inner')
'''
     B    C
가  b10  c10
나  b11  c11
다  b12  c12
다  b23  c23
라  b24  c24
마  b25  c25
'''

# 행 기준으로 합집합 : axis=0, join='outer'
df_axis0_inner = pd.concat([df_1, df_2], axis=0, join='outer')
'''
     A    B    C    D
가  a10  b10  c10  NaN
나  a11  b11  c11  NaN
다  a12  b12  c12  NaN
다  NaN  b23  c23  d23
라  NaN  b24  c24  d24
마  NaN  b25  c25  d25
'''



### Pandas를 이용한 데이터베이스의 JOIN 방식으로 데이터 병합 : merge()
"""
기본 형식 : 데이터프레임.join(데이터프레임, how='inner', on='None')
    how : 조인 방식(left, right, inner, outer) 
    on  : 기준 컬럼명  

"""

df_1 = pd.DataFrame( {'A' : ['a10', 'a11', 'a12'], 
                      'B' : ['b10', 'b11', 'b12'],
                      'C' : ['c10', 'c11', 'c12']} , index = ['가', '나',  '다'] )

df_2 = pd.DataFrame( {'B' : ['b23', 'b24', 'b25'],
                      'C' : ['c23', 'c24', 'c25'],
                      'D' : ['d23', 'd24', 'd25']} , index = ['다', '라',  '마'] )

df_outer_B = df_1.merge(df_2, how='outer', on='B')
'''
    A    B    C_x  C_y  D
0  a10  b10  c10  NaN  NaN
1  a11  b11  c11  NaN  NaN
2  a12  b12  c12  NaN  NaN
3  NaN  b23  NaN  c23  d23
4  NaN  b24  NaN  c24  d24
5  NaN  b25  NaN  c25  d25

'B' 컬럼이 조인되는 기준, 중복되는 컬럼명은 Pandas가 알아서 컬럼명_x, 컬럼명_y, 컬럼명_z 으로 재명명
'''



### 인덱스 키를 활용하여 병합
df_merge1 = df_1.merge(df_2, how='outer', left_index=True, right_index=True)
'''
     A   B_x  C_x  B_y  C_y   D
가  a10  b10  c10  NaN  NaN  NaN
나  a11  b11  c11  NaN  NaN  NaN
다  a12  b12  c12  b23  c23  d23
라  NaN  NaN  NaN  b24  c24  d24
마  NaN  NaN  NaN  b25  c25  d25

df_1의 index(가나다)와 df_2의 index(다라마)를 사용하여 병합
'''

merge_left_outer = df_1.merge(df_2, how='left', on='B')
'''
    A    B  C_x   C_y   D
0  a10  b10  c10  NaN  NaN
1  a11  b11  c11  NaN  NaN
2  a12  b12  c12  NaN  NaN

merge()의 왼쪽에 있는 df_1을 중심으로 데이터프레임이 생성
'''

merge_right_outer = df_1.merge(df_2, how='right', on='B')
'''
     A    B  C_x  C_y    D
0  NaN  b23  NaN  c23  d23
1  NaN  b24  NaN  c24  d24
2  NaN  b25  NaN  c25 

merge()의 오른쪽(괄호안)에 있는 df_2을 중심으로 데이터프레임이 생성
'''

merge_full_outer = df_1.merge(df_2, how='outer', on='B')
'''
    A    B  C_x  C_y    D
0  a10  b10  c10  NaN  NaN
1  a11  b11  c11  NaN  NaN
2  a12  b12  c12  NaN  NaN
3  NaN  b23  NaN  c23  d23
4  NaN  b24  NaN  c24  d24
5  NaN  b25  NaN  c25  d25

df_1과 df_2를 모두 합하여 데이터프레임이 생성
'''

merge_inner = df_1.merge(df_2, how='inner', on='B')
'''
Empty DataFrame
Columns: [A, B, C_x, C_y, D]
Index: []

df_1과 df_2의 공통 부분으로 데이터프레임 생성
'''



### Pandas를 이용한 데이터프레임의 데이터 정렬 : sort_values()
"""
sort_values(df_list, ascending=False, inplace=False)
    df_list   : 컬러명 리스트 ex. [컬럼명, 컬럼명] 
    ascending : 정렬 방식 (True / False)
    inplace   : 기존 데이터프레임에 적용(수정) 여부 (True / False)
"""
countries_df = pd.read_csv("./data/csv/countries.csv", index_col=0)
'''
   country      area     capital  population
KR   Korea     98480       Seoul    51780579
US     USA   9629091  Washington   331002825
JP   Japan    377835       Tokyo   125960000
CN   China   9596960     Beijing  1439323688
RU  Russia  17100000      Moscow   146748600
'''

sorted_df = countries_df.sort_values('population')
'''
    country     area     capital  population
KR   Korea     98480       Seoul    51780579
JP   Japan    377835       Tokyo   125960000
RU  Russia  17100000      Moscow   146748600
US     USA   9629091  Washington   331002825
CN   China   9596960     Beijing  1439323688

'population' 컬럼의 데이터를 기준으로 정렬
'''

sorted_df_two_column = countries_df.sort_values(['population', 'area'], ascending=False, inplace=False)
'''
   country      area     capital  population
CN   China   9596960     Beijing  1439323688
US     USA   9629091  Washington   331002825
RU  Russia  17100000      Moscow   146748600
JP   Japan    377835       Tokyo   125960000
KR   Korea     98480       Seoul    51780579
'''