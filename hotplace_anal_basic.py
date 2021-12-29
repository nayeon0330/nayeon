# -*- coding: utf-8 -*-
"""
Created on Thurs Dec 23 16:00 2021

hot_place analyze
"""

"""
실제적용 : 핫플레이스 인구 분석 파이썬 프로젝트

### 프로젝트 주제 ###
핫플레이스의 인구 데이터를 분석하여
유명한 맛집이나 카페 등
언제 가야 가장 덜 붐빌지 인구 분석을 통해 사람이 적은 시간대를 파악


### 1. 프로젝트 목표 수립 ###
첫 단계인 데이터를 선정해 수집하고 프로젝트 목표를 수립
여기서는 핫플레이스 인구를 표현할 수 있는 데이터를 수집한 후,
수집한 데이터를 바탕으로 목표를 수립

## 데이터 선정 : 시간대별 인구 데이터/ 지역을 서울로 한정
'서울 열린데이터 광장'이라는 사이트의 서울 생활인구 페이지 => 행정동 단위 데이터로 데이터 분석 프로젝트를 진행
각 연도별 데이터 중세어, 코로나 발생 직전인 "LOCAL_PEOPLE_DONG_201912.zip"를 이용하여 데이터를 분석

'행정동코드_매핑정보.xmls'

인구 데이터 : 서울 생활인구(내국인) ('LOCAL_PEOPLE_DONG_201912.csv')
행정동코드 데이터 : 행정구역 코드정보('행정동코드_매핑정보.xlsl')


## 목표 수립
핫플레이스가 있는 행정동에서 인구가 가장 적은 시간대 파악하기

행정동의 시간대별 인구는 어떻게 구할까?
먼저,
dong_code.csv 파일에서 핫플레이스가 있는 행정동의 행정동코드를 알아내고
lOCAL_PEOPLE_DONG_201912.csv 파일에서 알아낸 행정동코드와 일치하는 행만 골라낸다.
그리고
시간대별로 나뉜, 네번째 항목에 있는 생활인구수를 더한 후, 평균 구하기

첫번째 하위목표는
핫플레이스가 있는 행정동의 시간대별 평균 인구 그래프를 그려 분석

두번째 목표는
핫플레이스가 있는 행정동의 주중 / 주말 시간대별 평균 인구 그래프를 그려 분석

세번째 목표는
핫플레이스가 있는 행정동의 남녀 시간대별 평균 인구 그래프를 그려 분석

마지막 하위목표는
핫플레이스가 있는 행정동과 나에게 익숙한 행정동의 시간대별 평균 인구 그래프를 그려 비교 분석
"""

# 인구데이터 파일 읽기 : ./data/LOCAL_PEOPLE_DONG_201912.csv
import csv

f = open("./data/LOCAL_PEOPLE_DONG_201912.csv", encoding="utf-8")
data = csv.reader(f)
next(data)

data = list(data)
print(len(data))


# 행정동의 코드 데이터 읽기 : ./data/dong_code.csv
f2 = open("./data/dong_code.csv", encoding="utf-8")
code_data = csv.reader(f2)
next(code_data)


f2 = open("./data/dong_code.csv", encoding="cp949")
code_data = csv.reader(f2)
next(code_data)

next(code_data)

code_data = list(code_data)
print(len(code_data))


# 인구데이터 확인
print(data[0])

# 데이터 변환이 필요
"""
시간대 / 행정동 코드 : int()를 이용하여 정수형으로
총생활인구부터 맨 마지막 컬럼까지 : float()를 이용하여 실수로 데이터 변환
"""
for row in data:
    for i in range(1, 32):
        if i <= 2:
            row[i] = int(row[i])
        else:
            row[i] = float(row[i])
            
print(code_data[0])

# 프로그램 구현시, 사용할 '행정부행정동코드'만 정수로 변환
for row in code_data:
    row[1] = int(row[1])
print(code_data[0])



"""
### 2. 프로그램으로 구현

## 데이터 파일 읽고 행정동명과 행정동코드 연결
분석할 핫플레이스가 위치한 행정동을 선택

사용자가 알고싶은 행정동명을 직접 입력할 수 있도록 작성.
사용자가 서울시의 행정동 중 하나를 입력하면,
행정동명과 행정동코들의 매핑정보가 담긴 dong_code.csv에서
해당하는 행정동코드를 찾는다.

알고리즘에 해당하는 코드를 작성

<알고리즘>
1. 사용자에게 행정동명을 입력받아 변수(dong_name)에 저장하기
2. 행정동코드 데이터(code_data)를 돌며 반복하기
2-1. 행정동코드 데이터의 마지막 열인 행정동명(열 인덱스[-1])이 입력된 행정동명(dong_name)과 같다면
2-1-1. 해당하는 행정동코드를 변수(dong_code)에 저장하기

<알고리즘 코드>
1. dong_name = input()
2. for row in code_data:
    2.1. if row[-1] == dong_name:
        2.1.1. dong_code = row[1]
"""          

dong_name = input("알고싶은 핫플레이스가 위치한 행정동을 입력 : ")
    for row in code_data:
        if row[-1] == dong_name:
            dong_code = row[1]
            
print(dong_name, '-', dong_code, '을 분석합니다')

"""
하위목표 1 - 시간대별 인구 분석
핫플레이스가 있는 행정동의 시간대별 평균 인구수를 그래프로 시각화

<알고리즘>
1. 시간대별 평균 인구를 저장할 리스트(population)를 길이 24로 만들고 초깃값 0 저장하기
2. 인구 데이터(data)의 첫 행부터 마지막 행까지 돌며 반복하기
2-1 사용자가 입력한 행정도의 행정동코드(dong_code)와 인구 데이터(data)의 행정동코드(row[2])가 같다면
2.1.1 해당 행의 시간대(row[1])와 총생활인구수(row[3])를 각각 변수(time, p)에 저장하기
2.1.2 과정 2.1.1에서 저장한 시간대(time)가 population의 인덱스이므로 population[time]에 총생활인구수(p)에 더하기
3. 반복이 끝나면 population 리스트의 모든 값을 31로 나눈 후 population에 다시 저장하기
4. 완성된 population 리스트로 시간대별 평균 인구 그래프 그리기

<알고리즘 코드>
1. population = []
   for i in range(24):
       population.append(0)
       
1을 리스트 내포 방식으로 변경
population = [0 for i in range(24)]

2. for row in data:
   2.1 if row[2] == dong_code:
   2.1.1 time = row[1]
         p = row[3]
         2.1.2 population[time] += p
         
3. population = [p/31 for p in population]

4. import matplotlib.pyplot as plt
   plt.plot(range(24), population, color='red')
   plt.show()

<코드 작성 후 확인>
"""            
import matplotlib.pyplot as plt

population = [0 for i in range(24)]

for row in data:
    if row[2] == dong_code:
        time, p = row[1], row[3]
        population[time] += p
        
population = [p/31 for p in population]

plt.rc('font', family='Malgun Gothic')
plt.title(dong_name + '시간대별 평균 생활 인구수')
plt.plot(range(24), population, color='red')
plt.xticks(range(24), range(24))
plt.xlabel('시간대')
plt.ylabel('평균생활인구수')
plt.show()

"""
하위 목표 1에 대한 결과 분석

압구정동은
새벽 1시 ~ 6시 정도에 생활인구가 적다.

새벽 1시 ~ 6시에 인구 이동이 매우 적으므로
이 시간에 인구는 대부분 거주민일 확률이 높다..

12시 ~ 18시 사이에는 인구가 가장 많음.

따라서 
압구정동에 있는 핫플레이스에 가려면
20시 ~ 23시 정도에 약속을 잡는 것이 좋을 것 같다.

또는
10시 ~ 11시 정도에 브런치 약속을 잡아도 될 것 같다..
"""

"""
하위목표 2 : 핫플레이스가 있는 행정동의 주중 / 주말 시간대 평균 인구 그래프 그리고 분석하기

알고리즘 작성

1. 주중 시간대별 생활인구수를 저장할 리스트(weekday)와 주말시간대별 생활인구를 저장할 리스트(weekend)를
   길이 24로 만들고 초깃값 0 저장하기
2. 인구 데이터의 첫 행부터 마지막 행까지 돌며 반복하기
2.1 사용자가 입력한 행정동의 행정동코드(dong_code)와 인구 데이터와 인구 데이터의 행정동코드(row[2])와 같다면
2.1.1 해당 행이 시간대(time)와 총생활인구수(p), 기준일ID의 연도(year), 월(mon), 일(day)을 각각 변수에 저장하기
2.1.2 과정 2.1.1에서 저장한 연도, 월, 일을 datetime.date().weekday()에 넣어 주중 / 주말 구분하기
2.1.3 주중이면 주중 리스트(weekday[time])에 총생활인구수, 주말이면 주말 리스트(weekend[time])에 총생활인구수 더하기

# 주중 인구와 주말 인구의 평균을 구하기 위해 2019년 12월의 주중 일수와 주말 일수를 알아야 함(3~4)

3. 2019년 12월의 주중 일수(weekday_cnt)와 주말 일수(weekend_cnt)를 저장할 변수를 만들고 초깃값 0 저장하기

4. 2019년 12월의 일수만큼 반복하기
4.1 datetime.date(2019, 12, i)가 주중이면 주중 일수에 1, 주말이면 주말 일수에 1 더하기

5. 주중 리스트의 각 요소를 주중 일수로 , 주말 리스트의 각 요소를 주말 일수로 나누어 주중 / 주말 평균 인구 구하기

6. 완성된 weekday와 weekend 리스트로 주중 / 주말 시간대별 평균 인구 그래프 그리기
"""

weekday = [0 for i in range(24)]
weekend = [0 for i in range(24)]

for row in data:
    if row[2] == dong_code:
        time, p = row[1], row[3]
        year, mon, day = int(row[0][:4]), int(row[0][4:6]), int(row[0][6:])
        num = datetime.date(year, mon, day).weekday()
        
    if num < 5:
        weekday[time] += p
    else:
        weekend[time] += p
        
# 2019년 12월의 주중 / 주말 일수 구하기
weekday_cnt, weekend_cnt = 0, 0

for i in range(1, 32):
    if datetime.date(2019, 12, i).weekday() < 5:
        weekday_cnt += 1
    else:
        weekend_cnt += 1
        
print('2019년 12월의 주중 일수 =', weekday_cnt, '주말 일수 =', weekend_cnt)

weekday = [w/weekday_cnt for w in weekday]
weekend = [w/weekend_cnt for w in weekend]

print('주중 인구 : ', weekday)
print('주말 인구 : ', weekend)

plt.rc('font', family='Malgun Gothic')
plt.title(dong_name + '주중 / 주말 시간대별 평균 인구')
plt.plot(range(24), weekday, color='indigo', label='주중')
plt.plot(range(24), weekend, color='orangered', label='주말')
plt.legend()
plt.xlabel('시간대')
plt.ylabel('평균 인구수')
plt.xticks(range(24), range(24))
plt.show()     
        
"""
하위목표 2에 대한 결과 분석

압구정동은 주말보다 주중 인구가 더 많다.
주말에 압구정에 간다면 그리 걱정하지 않아도 된다..
"""     
        
"""
하위목표3 : 핫플레이스가 있는 행정동의 남 / 녀 시간대별 평균 인구 그래프 그리고 분석하기

알고리즘 작성

1. 남성 시간대별 생활인구를 저장할 리스트(male)와 여성 시간대별 생활인구를 저장할 리스트(female)를 길이 24로 만들고 초깃값 0 저장하기

2. 인구 데이터의 첫 행부터 마지막 행까지 돌며 반복하기
2.1 사용자가 입력한 행정동의 행정동코드(dong_code)와 인구 데이터의 행정동 코드(row[2])가 같다면
2.1.1 해당 행의 시간대(열 인덱스[1])를 변수(time)에 저장하기
2.1.2 열 인덱스[4]부터 [17]까지의 합을 male[time]에 더하기
2.1.3 열 인덱스[18]부터 [31]까지의 합을 female[time]에 더하기

3. 반복이 끝나면 남성 생활인구 리스트(male)와 여성 생활인구 리스트(female)를 각각 31로 나누어 시간대별 평균 인구 구하기

4. 완성된 male과 female 리스트로 시간대별 평균 인구 그래프 그리기
"""
male = [0 for i in range(24)]
female =  [0 for i in range(24)]

for row in data:
    if row[2] == dong_code:
        time = row[1]
        male[time] += sum(row[4:18])
        female[time] += sum(row[18:32])
        
male = [m/31 for m in male]
female = [f/31 for f in female]

plt.rc('font', family='Malgun Gothic')
plt.title(dong_name + '남녀 시간대별 평균 인구')
plt.plot(range(24), male, color='b', label='남성')
plt.plot(range(24), female, color='r', label='여성')
plt.xlabel('시간대')
plt.ylabel('평균 인구수')
plt.legend()
plt.xticks(range(24), range(24))
plt.show()

"""
하위목표 3의 결과 분석

압구정동에는 여성이 남성보다 항상 더 많다.
남성 인구의 증감폭보다 여성 인구의 증감폭이 더 크다.
만약 압구정동의 여성이 선호하는 핫플레이스라면 점심시간에 붐빌수도 있다...
""" 
        
"""
하위목표 4: 핫플레이스가 있는 행정동과 익숙한 행정동의 시간대별 평균 인구 그래프 그려서 비교 분석하기

알고리즘 작성

1. 사용자에게서 행정동명을 입력받아 행정동코드를 구한 후 이 값을 dong_code에 저장하기

2. 비교할 행정동명을 입력받아 행정동코들르 구한 후 이 값을 dong_code2에 저장하기

3. 핫플레이스의 행정동 인구를 저장할 리스트(population)와 비교할 행정동 인구를 저장할 리스트(population2)를 길이 24로 만들고
   초깃값 0 저장하기 
   
4. 인구 데이터의 첫 행부터 마지막 행까지 돌며 반복하기
4.1 사용자가 입력한 행정동의 행정동코도와 인구 데이터의 행정동코드(row[2])가 같다면
4.1.1 해당 행의 시간대(row[1])와 총생활인구수(row[3])를 각각 변수(time, p)에 저장하기
4.1.2 인덱스가 time인 population 리스트의 요소(population[time])에 총생활인구수를 더하기

4.2 비교할 행정동의 행정동코드와 인구 데이터의 행정동코드(열 인덱스[2])가 같다면
4.2.1 해당 행의 시간대(열 인덱스[1])와 총생활인구수(열 인덱스[3]) 각각 변수(time, p)에 저장하기
4.2.2 인덱스가 tim인 population2 리스트의 요소(population2[time])에 총생활인구수를 더하기

5. 반복이 끝나면 두 리스트(population, population2)의 모든 값을 31로 나누어 다시 저장하기

6. 완성된 리스트로 두 지역의 시간대별 평균 인구 그래프 그리기
"""
# 핫플레이스가 있는 행정동
dong_name = input('핫플레이스가 위치한 행정동을 입력하세요 ==>')
for row in code_data:
    if row[-1] == dong_name:
        dong_code = row[1]
        
# 비교할 행정동
dong_name2 = input('비교할 행정동을 입력하세요 ==>')
for row in code_data:
     if row[-1] == dong_name2:
         dong_code2 = row[1]
         
population = [0 for i in range(24)]
population2 = [0 for i in range(24)]

for row in data:
    # 핫플레이스가 있는 행정동인 경우
if row[2] == dong_code:
        time, p = row[1], row[3]
        population[time] += p

    # 비교할 지역이 행정동인 경우
elif row[2] == dong_code2:
        time, p = row[1], row[3]
        population2[time] += p

population = [p/31 for p in population]
population2 = [p/31 for p in population2]

plt.rc('font', family='Malgun Gothic')
plt.title(dong_name + '과' + dong_name2 + '의 시간대별 평균 인구 비교')
plt.plot(range(24), population, color='m', label=dong_name)
plt.plot(range(24), population2, color='orange', label=dong_name2)
plt.legend()
plt.xlabel('시간대')
plt.ylabel('평균 인구수')
plt.xticks(range(24), range(24))
plt.show()

"""
하위목표 4의 결과 분석

인구이동이 적은 새벽 인구가 해당 동에 거주하는 인구라 가정한다면
역삼 2동이 압구정동보다 거주 인구가 많다.

인구 이동이 역삼 2동보다 압구정동이 더 많다.

대부분의 시간에는 역삼 2동의 인구가 더 많지만 17 ~ 20시 사이에는 압구정동이 더 많다.

17 ~ 20시에는 역삼 2동으로, 그 외 시간대에는 압구정동으로 가는 것이 사람이 덜 붐빈다...
"""
