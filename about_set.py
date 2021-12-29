# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 09:20:31 2021

set 정리

1. 수학의 집합과 유사
2. 리스트나 튜플과 달리 순서가 없다.
3. 리스트나 튜플과 달리 index가 없고, 딕셔너리처럼 key도 없다.
   오로지 데이터만 존재!!!
4. 데이터의 중복이 허용되지 않는다.
5. 교집합 / 합집합 / 차집합 / 등의 집합연산 수행이 가능,

선언 : {데이터, 데이터, ...}
"""
### set 생성 방법
## 1. { }을 이용하여 데이터를 갖는 set 생성
# 세가지 숫자로 구성된 set
numbers = {2, 3, 1, 5}
type(numbers)
'''
set
'''

## 2. 생성자를 이용하는 방법
# 2-1. 리스트를 이용하여 생성자에게 전달
data_list = [2, 4, 6, 1, 5]
type(data_list)
'''
list
[2, 4, 6, 1, 5]
'''

set_list = set(data_list)
type(set_list)
'''
set
{1, 2, 4, 5, 6}
'''

# 2-2. 문자열을 생성자에게 전달
# 문자열도 각각의 문자에 index가 부여되는 시퀀스의 일종이기 때문에 가능
set_str = set('absdeffggfgsd')
type(set_str)
'''
set
{'a', 'b', 'd', 'e', 'f', 'g', 's'}
문자열을 생성자에게 전달하면
각 문자의 index를 이용하여 문자열이 각각의 문자로 분리가 된다.
그리고 동일 문자가 발견되면
처음 하나의 문자만 저장하고 동일한 다른 문자는 저장하지 않는다..
 
index 번호가 없어서 출력하는 순서가 달라질 수도 있다(딕셔너리도 동일)
'''

## 3. 비어있는(데이터가 없는) set 생성 : set()을 이용!!!!!
set_empty = set()
type(set_empty)
'''
set
'''

set_empty2 = {}
type(set_empty2)
'''
dict
주의!!
'''

## 4. set의 항목(데이터)에 접근하는 연산
# 1. 어떤 항목이 set 안에 포함되어 있는지 확인 : 확인항목 in set 과 같이 사용
numbers = {2, 1, 5}  

if 2 in numbers:
    print("항목 존재!!")
else:
    print("존재하지 않는 항목 !!")
'''
항목 존재!!
'''

# 2. set은 index가 없기 때문에, index로는 각 항목을 조회할 수 없다.
#    하자만 for를 이용하여 각 항목을 추출할 수는 있다.
numbers = {2, 1, 5}

for x in numbers:
    print(x, end=" ")
'''
1 2 5  <== 와 같이 각 항목 뒤에 띄어쓰기가 붙은 이유는

print()의 end="  "을 이용하였기 때문
'''
for x in numbers:
    print(x, end=" _ ")
'''
1 _ 2 _ 5 _ 
'''

"""
참고 : set은 index가 존재하지 않는 데도
for를 이용하여 각 항목을 추출할 수 있는 이유는
for in  :
의  특징 때문에..

for 저장변수 in 다중데이터 : 는
다중데이터의 데이터를 더이상 찾을 수 없을 경우에 False 값을 유발시켜
반복을 중지하는 구조로 되어있는 반복문!!!
"""

"""
주의 : in 과 for in은 다르다!!
in : in 키워드(연산자)를 기준으로 왼쪽의 데이터가 오른쪽 내에 포함되어 있는 지를 확인하는 연산자 

if x in numbers:
   x => numbers
   비교결과

for in : 과 같은 반복문에서의 in 
===> in을 기준으로 오른쪽의 데이터를 추출하여 왼쪽에 저장하는 연산자

for x in numbers:
    x <= numbers
"""

# 3. set은 index는 없지만, 데이터를 이용한 정렬은 가능 : 파이썬 기본함수 sorted()
for x in sorted(numbers):
    print(x, end="=>")
'''
1=>2=>5=>
'''

# 4. 기존 set에 새로운 데이터 추가 : set()의 add() 함수를 이용
numbers = {2, 1, 5} 

numbers.add(5)
numbers.add(2)
numbers.add(1)
'''
{1, 2, 5}
와 같이 기존 데이터(항목)와 동일한 데이터를 추가하면 추가 되지 않는다!!!
'''

numbers.add(9)
numbers.add(0)
numbers.add(7)
'''
{0, 1, 2, 5, 7, 9}
와 같이 기존에 존재하지 않는 새로운 데이터만 저장된다..
'''

# 5. set의 항목 제거 : set의 remove() 함수를 이용
numbers = {2, 1, 5} 

numbers.remove(5)
'''
{1, 2}
remove() 는 데이터를 이용하여 제거한다(index가 없기 때문에)
'''


### set에 적용할 수 있는 다양한 연산들
## 1. set 비교연산 : == / !=
A = {1, 2, 3}
B = {1, 2, 3}

# A와 B가 같은지
A == B
'''
True
'''

# A와 B가 다른지
A != B
'''
False
'''

## 2. 진부분집합 : < / <=
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}

# A가 B의 진 부분 집합인지
A < B
'''
False
'''

# B가 A의 진 부분 집합인지
B < A
'''
True
'''

## 3. set도 파이썬이 제공하는 집계함수들을 적용할 수 있다.
a_set = {1, 5, 4, 3, 7, 4 }
type(a_set)
'''
set
'''

# 집계함수 : len()
len(a_set)
'''
5
{1, 3, 4, 5, 7}
'''

# 집계함수 : max()
max(a_set)
'''
7
'''

# 집계함수 : min()
min(a_set)
'''
1
'''

# 집계함수 : sorted() <== 원본데이터는 정렬이 되지 않고, 정렬된 결과만 리스트로 반환!!
sorted(a_set)
'''
[1, 3, 4, 5, 7]
주의 : 리스트로 반환
'''

sorted(a_set, reverse=True)
'''
[7, 5, 4, 3, 1]
주의 : 리스트로 반환
'''

# 집계함수 : sum()
sum(a_set)
'''
20
'''

## 4. set에 적용할 수 있는 논리 연산 : any() / all()
a_set1 = { 1, 0, 2, 3, 3}
any(a_set1)
# => True

all(a_set1)
# => False


a_set2 = { 1, 4, 2, 6, 3}
any(a_set2)
# => True

all(a_set2)
# => True


a_set3 = { 0, 0, 0, 0, 0}
any(a_set3)
# => False

all(a_set3)
# => False

"""
any() / all() 은 데이터에 0이 포함되어 있는지를 확인하는 함수
any() : 전체 데이터가 0일 경우에만 False
all() : 0이 하나라도 있으면 False
"""

## 5. set의 집합연산 : 두개의 set을 이용 
"""
합집합 : "|" 또는 union() 
교집합 : "&" 또는 intersection()
차집합 : "-" 또는 difference() 
대칭차집합 : "^" 또는 symmetric_defference()
"""

# 합집합 : "|" 또는 union() 
# 두개의 set을 하나로 합하기
A = {1, 2, 3}
B = {3, 4, 5}

A | B
'''
{1, 2, 3, 4, 5}
만약 각 set에 중복값이 있을 경우에는 한가지 값만 저장
'''

A.union(B)
'''
{1, 2, 3, 4, 5}
union()은 대상 set의 순서를 바꾸어도 됨
ex. A.union(B) 또는 B.union(A)
'''

# 교집합 : "&" 또는 intersection()
# 두개의 set 데이터 중 공통적인 데이터만 추출
A = {1, 2, 3}
B = {3, 4, 5}

A & B
'''
{3}
'''

A.intersection(B)
'''
{3}
순서를 바꾸어도 됨
ex. A.intersection(B) 또는 B.intersection(A)
'''

# 차집합 : "-" 또는 difference() 
# 하나의 set 데이터들 중 다른 set 데이터를 뺀 결과
A = {1, 2, 3}
B = {3, 4, 5}

A - B
'''
{1, 2}
'''

B - A
'''
{4, 5}
'''

A.difference(B)
'''
{1, 2}
'''

B.difference(A)
'''
{4, 5}
차집합은 대상 set의 순서가 바꾸면 결과 값도 바뀔 수 있으므로 주의!!!
'''

# 대칭차집합 : "^" 또는 symmetric_defference()
# 두개의 set에 대한 합집합에서 교집합을 뺀 결과
A = {1, 2, 3}
B = {3, 4, 5}


A ^ B
'''
{1, 2, 4, 5}
1. A와 B의 합집합을 구한 후,     : {1, 2, 3, 4, 5}
2. A와 B의 교집합을 구하여       : {3}
3. 합집합에서 교집합을 뺀 결과   : {1, 2, 3, 4, 5} - {3}
   {1, 2, 4, 5}
'''


### 파티에 동시에 참여하는 사람 알아내기
"""
1. partyA 참석자 명단과 partyB 참석자 명단을 각각 set으로 생성
2. 두개의 set에 모두 포함되어 있는 참석자를 출력
"""

partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

print("두개의 파티에 모두 참석한 사람의 명단은 아래와 같습니다.")
print(partyA.intersection(partyB))
'''
{'Park'}
'''



### 파일 읽고, 쓰기
"""
컴퓨터 용어의 파일이란?
   컴퓨터 내의 저장장치에 데이터를 저장하기 위해 사용되는 논리적인 단위

저장장치 : 내장 디스크(HDD/SDD) 또는 외장 디스크
        : 디스크 내의 저장 형식 : FAT32 exFAT NTFS 방식 등이 존재
        : NTFS 방식으로 포맷되어 있는 디스크는 Mac과 호환 불가
        
파일의 종류는 다양하다
파일 : 파일명과 확장자로 구성
       단, 일부 파일은 확장자가 없는 것도 있다.

주요 파일 확장자 : 
    .py : 파이썬 파일
    .ipynb : 쥬피터 노트북 파일
"""

## 1. 파일 쓰기 : 파이썬이 제공하는 open() 함수를 이용
"""
파일을 읽거나 쓰거나 파일내에 어떤 내용을 쓰려면
1. open() 함수에 해당 모드를 설정해야 한다.
2. 파일을 모두 읽거나, 쓸 내용이 완료되면 해당 파일은 반드시 닫아주어야 한다.

ex.
   f = open('작업 파일', '작업 모드')
   f.read() / f.write() 등을 이용하여 작업 수행
   f.close()를 이용하여 해당 파일 닫기
   
작업모드의 종류 : 읽기('r') / 쓰기('w') 등
     교재 105p 상단 표 참조..   
"""
## 2. 파일 쓰기 : 파이썬이 제공하는 open() 함수 내에 파일에 대한 경로 및 파일, 쓰기 모드로 설정
f = open('hello.txt', 'w')
f.write('Hello Python File Write')
f.close()

## 3. 파일 읽기 : 파이썬이 제공하는 open() 함수 내에 파일에 대한 경로 및 파일, 읽기 모드로 설정
f = open('./hello.txt', 'r')
read_data = f.read()
f.close()

print(read_data)


### 파일내의 중복되지 않는 단어의 갯수 구하기 : ./data/proverb.txt
'''
proverb.txt

All's well that ends well. 
Bad news travels fast. 
Well begun is half done. 
Birds of a feather flock together. 
'''

f = open('./proverb.txt', 'r')
r = f.read()
f.close()
print(r)
'''
All's well that ends well. 
Bad news travels fast. 
Well begun is half done. 
Birds of a feather flock together. 
'''


"""
참고 : 일반적으로 작문(자소서)를 할 때 다양한 단어를 사용하면 점수가 높은 경향이 있다.
       텍스트 파일을 읽어서 단어를 얼마나 다양하게 사용하여 문서를 작업했는지를 계산

작업내용       
1. 중복된 단어는 하나만 인정
2. 1의 조건에 해당하는 자료구조인 set을 이용
3. 파일 열기
4. 파일 읽기
    4-1. 파일을 읽을때 단어들을 분리
    4-2. 분리된 단어들을 set에 추가
5. 파일 닫기
6. set에 저장된 단어 갯수와 해당 단어들을 출력       
"""


# 1. 단어를 저장할 비어있는 set객체 생성 : set생성자를 이용
words = set()

# 2. 파일 열기 : 파이썬의 open()를 이용하여 읽기 모드('r') 설정
file = open('./proverb.txt', 'r')

"""
file_path = './ ~~'
file_name = input("검사할 파일명 입력 : ")
read_file = file_path + file_name
file = open(read_file,'r')
"""

# 3. 읽은 내용을 단어들로 분리 : str의 split()을 이용하여 띄어쓰기를 기준으로 분리
# 구두점을 제거하고, 단어를 소문자로 변환하는 사용자 정의 함수 선언
def process(w):
    output = ""
    for ch in w:
        if ch.isalpha():
            output += ch
    return output.lower()
        
    
for line in file:
    linewords = line.split()
    for word in linewords:
        words.add(process(word))            # 구두점을 제거하고, 단어를 소문자로 변환하는 사용자 정의 함수 이용
        
print('문서내에서 사용된 단어의 갯수 : ', len(words))
'''
문서내에서 사용된 단어의 갯수 :  18
'''

print(words)
'''
{'fast', 'together', 'is', 'well', 'a', 'that', 'bad', 'news', 'feather', 
 'travels', 'alls', 'half', 'ends', 'birds', 'flock', 'of', 'begun', 'done'}
'''



"""
실행흐름

file의 내부

    All's well that ends well. 
    Bad news travels fast. 
    Well begun is half done. 
    Birds of a feather flock together. 

for line in file:
=> line : All's well that ends well.   

linewords = line.split()
=> linewords : ["All's" "well" "that" "ends" "well."] 

for word in linewords:
=> word : "All's"  

process(word)
=> "All's" 문자열이 전달
------------------------------
def process(w):
=> w : "All's" 문자열     

for ch in w:
=> ch : "A" / "l" / "l" / " ' " / "s"

if ch.isalpha():
=> isalpha() : 문자가 알파벳이면 True / False

   output += ch
   => output : "Alls"  

 output : "Alls"
 output.lower() : "alls" 
----------------------------------- 
words.add("alls" )

words : {"alls"}
"""
