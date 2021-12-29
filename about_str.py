# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:48:24 2021

@author: Playdata

문자열(str)에 대한 정리

텍스트는 오랫동안 정보를 효율적으로 교환하는 가장 중요한 수단.

텍스트의 종류
     구조화된 문서          : HTML / XML / JSON 등
     구조화되지 않은 문서   : 자연어로 이루어진 텍스트
     
일반적으로 원천 데이터는 가공된 형태가 아니기 때문에
이를 데이터를 수정하여 완전한 데이터로 만들어 사용해야 한다.

텍스트 데이터 처리
    파이썬이 기본적으로 제공하는 str 관련 함수들로 처리 가능.
    비교적 쉽게 텍스트 데이터를 처리하기 위한 다양한 외부 모듈을 지원
        BeautifulSoup / csv / json / nltk(영문 분석) / konlpy(한글 분석) : 3.6 / 3.7    
        단, 외부 모듈은 파이썬을 지원하는 방식이기 때문에
        파이썬 버전이 상향되었다고 외부모듈도 같이 상향되는 것은 아니다!!!
        
따라서 텍스트 데이터 처리시,
기본적인 부분은 str 관련 함수들로 처리하고,

특수한 경우에는 적절한 외부모듈을 사용..
"""

### 문자열 슬라이싱 및 인덱싱
"""
문자열(str 타입)은 내부적으로 각 문자마다 index가 존재
따라서 슬라이싱 및 인덱싱 작업은 문자열의 index를 이용
슬라이싱 및 인덱싱 방법은 list / tuple과 동일
"""

s = 'Monty Python'
'''
-12        -7             -1
 0 1 2 3 4  5  6 7 8 9 10 11
 M o n t y     P y t h o n
'''

# 1. index
print(s[0])         # <= M

# 2. slice : str[startIndex : endIndex]
print(s[6 : 10])    # <= Pyth

# 음수(-) index를 이용한 slice
print(s[-12 : -7])  # <= Monty

print(s[ :-2])      # <= Monty Pyth


t = s[ :-2]
'''
 'Monty Pyth'
'''

t = s[-2:]
'''
'on'
'''

# 3. 문자열 연산 (+)
s[:-2] + s[-2:]     # <= 'Monty Python'


# 4. 문자열 분리 : str의 split()
s = 'Welcome to Python'  

s.split()           # <= ['Welcome', 'to', 'Python']

type(s)  # <= str


s = '2021.8.15'
s.split()           # <= ['2021.8.15']
s.split('.')        # <= ['2021', '8', '15']
s.split('8')        # <= ['2021.', '.15']


s = 'Hello, World!'
s.split()           # <= ['Hello,', 'World!']
s.split(',')        # <= ['Hello', ' World!']


# 5. 공백 제거 : strip() /lstrip() /rstrip()
# 단, 문자열 내부의 공백은 예외..
# => ex. " ㄴㄴㄴ  ㄴㄴㄴ" => 양쪽은 공백 제거 가능하지만 중간 공백은 제거되지 않는다..

s = '   hello   '
print('left', s.strip(), 'right')   # <= left hello right(양쪽 공백 제거)
print('left', s.lstrip(), 'right')  # <= left hello    right(왼쪽 공백 제거)
print('left', s.rstrip(), 'right')  # <= left    hello right(오른쪽 공백 제거)


s = 'Welcome, to,  Python, and ,  bla, bla   '
s.split()
'''
['Welcome,', 'to,', 'Python,', 'and', ',', 'bla,', 'bla']
'''

s.split(',')
'''
['Welcome', ' to', '  Python', ' and ', '  bla', ' bla   ']
'''

s = 'Welcome, to,  Python, and ,  bla, bla   '
[x.strip() for x in s.split(',')]
'''
['Welcome', 'to', 'Python', 'and', 'bla', 'bla']
'''


# 6. 문자열끼리 연결(합하기) : str의 join()
# => join()은 순서가 바뀌면 결과도 바뀐다!!

# 문자열과 문자열을 보유하는 리스트 연결
str_list = ['apple', 'grape', 'banana']
sep = ","

sep.join(str_list)
'''
'apple,grape,banana'
와 같이 리스트의 각 항목을 하나씩 꺼내어 ","로 연결
'''

# split()으로 분리된 문자열 등을 특정 부호로 변경 (연결)
split_str = "010.1234.5678".split(".")
sep="-"
sep.join(split_str)
'''
 '010-1234-5678'
 위의 리스트 형식과 동일
'''

# 7. 문자열의 일부를 다른 문자로 변경 : str의 replace()
phone = "010.1234.5678"
phone.replace(".", "-")
'''
'010-1234-5678'
'''

# 8. 문자열을 각각의 문자로 분리 : 문자열을 list() 에게 전달하면 자동 분리
txt = "replace"
char_list = list(txt)
'''
['r', 'e', 'p', 'l', 'a', 'c', 'e']
'''

# 9. 문장 내부에 줄바꿈(\n) 탭(\t) 와 같은 데이터가 들어있을 경우
# => 해당 문장을 split()하면 각각의 단어들로 자동 분리
# 부호 있는 경우 : 반드시 print()로 출력
a_string = 'Actions \n\t speak louder than words'
a_string
'''
변수의 값을 확인했을 경우 : 'Actions \n\t speak louder than words'
'''

print(a_string)
'''
변수의 값을 출력했을 경우
Actions 
	 speak louder than words
'''

word_list = a_string.split()
'''
['Actions', 'speak', 'louder', 'than', 'words']
'''

# 10. 문장 내부에 줄바꿈(\n) 탭(\t)를 제거 : join()
sep = " "
replace_text = sep.join(word_list)
replace_text
'''
'Actions speak louder than words'
'''

print(replace_text)
'''
A c t i o n s   
 	   s p e a k   l o u d e r   t h a n   w o r d s
'''

# 11. 대소문자로 변경(단, 영문만 가능) : upper() / lower()
a_string = 'Actions speak louder than words'
a_string.upper()
'''
'ACTIONS SPEAK LOUDER THAN WORDS'
'''

a_string.lower()
'''
'actions speak louder than words'
'''

# 12. strip() / istrip / rstrip를 이용한 좌우 문자 제거
s = "########this is an example#####"
s.strip("#")
'''
 'this is an example'
'''

s.lstrip("#")
'''
'this is an example#####'
'''

s.rstrip("#")
'''
'########this is an example'
'''

s.strip("#").capitalize()
'''
'This is an example'
맨 처음 문자가 대문자로 바뀌는 이유:
    양쪽 # 들을 제거한 후,
    첫 글자를 대문자로 변경해주는 capitalize()를 사용했기 때문..
'''

# 13. 문자열 내부에 지정한 문자의 index를 반환 : find() / 해당 문자가 없으면 -1을 반환
# ==> 해당문자가 없으면 -1을 반환
url = "http://www.naver.com"

url.find('h')     # <= 0

url.find('http')  # <= 0

url.find('.')     # <= 10

url.find('.com')  # <= 16
'''
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19
h  t  t  p  :  /  /  w  w  w  .  n  a  v  e  r  .  c  o  m

find()는 지정한 문자, 문자열을 찾아 해당 위치의 index를 반환하는데,
동일한 문자가 여러개일 경우, 
    맨 처음 찾은 문자에 대한 index만 반환

문자열을 찾았을 경우, 
    찾은 문자열의 맨처음 문자의 index를 반환

'''
url.find('https')  # <= -1

url.find('-')      # <= -1


# 14. 지정한 문자를 몇 개 찾았는지 갯수를 반환 : count()
url = "http://www.naver.com"

url.count('/')     # <=  2

url.count('.')     # <= 2


# 15. 문자열 내의 unicode 값이 가장 큰 값(max())의 unicode를 반환
#     문자열 내의 unicode 값이 가장 작은 값(min())의 unicode를 반환
#     ord()를 이용 : unicode 반환
url = "http://www.naver.com"

uni_1 = ord(max(url))   # <= 119
uni_2 = ord(min(url))   # <= 46


# 16. unicode를 문자로 변환 : chr()
char_1 = chr(119)       # <= 'w'

char_2 = chr(46)        # <= '.'


#### 16. 외부 모듈인 string의 주요내용
import string

# 영문 대소문자 전체를 반환
result = string.ascii_letters
'''
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
'''

# 영문 소문자 전체를 반환
result = string.ascii_lowercase
'''
'abcdefghijklmnopqrstuvwxy
'''

# 영문 대문자 전체를 반환
result = string.ascii_uppercase
'''
'ABCDEFGHIJKLMNOPQRSTUVWXY
'''

# 숫자 구성 반환 (10진수)
result = string.digits
'''
'0123456789'
'''

result = string.hexdigits
'''
'0123456789abcdefABCDEF'
'''

result = string.octdigits
'''
'01234567'
'''

# 지정한 문자의 다음 문자를 대문자로 변환 : string의 capwords()
test_cap = "abcde"

# 1. 첫번째 문자를 지정했을 경우
result = string.capwords(test_cap, 'a')
'''
'aBcde'
'''

# 첫번째가 아닌 문자를 지정했을 경우
result = string.capwords(test_cap, 'b')
'''
'AbCde'
'''

"""
string 내부의 각 값들은
API Key 또는 인증서 값을 암호화할 때 주로 사용
"""


#### 숫자로 이루어진 일회용 비밀번호 추출기
# 예를들면 금융거래시 필요한 OTP 번호
# 매번 숫자가 임의의 값으로 섞여서 출력 : random 모듈을 사용
import random

n_digit = int(input("임시로 발급받을 비밀번호의 자릿수 입력 : "))
'''
6 입력시
'''
otp= ''
for k in range(n_digit):
    otp += str(random.randrange(0, 10))

print(otp)
'''
040674
'''