###################################################
########### 초보자를 위한 파이썬 200제 ############
###################################################

import pandas as pd
import numpy as np
from matplotlib import rcParams
from scipy import stats

from matplotlib.pyplot import *
from numpy import sin, exp,  absolute, pi, arange
from numpy.random import normal

# 부가설명
# 4spaces

#%% <<<입문>>>>
#%% 001 대화식 모드
print("안녕하세요?")

#%% 002 텍스트에디터 

#%% 003 변수명 만들기
# 변수명은 _ 또는 영문자로 시작
# 변수명은 대소문자를 구분

_myname = 'ijeong'
my_name = '이정'
MyName2 = 'Han Ijeong'
counter = 8
Counter = 27

#%% 004 변수에 값 대입하기
# 숫자형인지 문자형인지 명시하지 않아도 된다
a=1
b=2
print(a+b)

#%% 005 주석처리하기
"""
a=2
b=4
print(a+b)
"""


#%% 006 자료형 개념 배우기 *
int_data = 1                      # 정수 선언
float_data = 3.14                 # 실수 선언 
complex_data = 1+5j               # 복수수 선언
str_data = 'I love python'        # 문자열 선언
list_data = [1,2,3]               # 리스트 선언
tuple_data = (1,2,3)              # 튜플 선언
dict_data1={0:'FALSE',1:'TRUE'}   # 사전 선언
dict_data2={'a':97,'b':98}

#%% 007 자료형 출력 개념 배우기(print)
print(int_data)
print(str_data)
print(list_data)
print(list_data[0])
print(dict_data1)
print(dict_data1[0])
print(dict_data2[0]) # error
print(dict_data2['a'])

print('#','\n','#')
print('#',end='')
print('#')
print('#')

#%% 008 들여쓰기 개념 배우기 ***
# 실행 코드 구분을 괄호{}로 하지 않고 들여쓰기를 한다 (무조건)
# 제어문(if,for,while)이나 함수이름, 클래스 이름의 긑을 ':'로 표시한다.
# 가장 바깥쪽의 실행코드는 들여쓰기 없이 시작해야 한다.                                                                                                        
# 같은 제어문내의 실행코드는 들여쓰기 간격이 동일해야 한다.

listdata = ['a','b','c']
if 'a' in listdata :
    print('a가 listdata에 있습니다')
    print(listdata)
else:
    print('a가 listdata에 존재하지 않습니다')
    

# error
"""
if 'a' in listdata :
    print('a가 listdata에 있습니다')
        print(listdata)
else:
    print('a가 listdata에 없습니다')
"""

#%% 009 if문 개념 배우기 1(if~else)
x=1
y=2
if x>=y:
    print('x가 y보다 크거나 같습니다')
else :
    print('x가 y보다 작습니다')


#%% 010 if문 개념 배우기 2(if~elif)
# 여러 개의 조건을 순차적으로 체크하고 특정 로직을 수행하고자 할 때
if x>y:
    print('x가 y보다 큽니다')
elif x<y:
    print('x가 y보다 작습니다')
else:
    print('x가 y와 같습니다')
    
#%% 011 for문 개념 배우기1(for)
# for문의 범위로 사용되는 것은 시퀀스 자료형 또는 반복 가능한 자료이어야 한다.
# 문자열, 리스트나 튜플, 사전, range() 등
scope = [1,2,3,4,5]
for x in scope:
    print(x)
    
str1 = 'abcdef'
for c in str1:
    print(c)
    
list1 = [1,2,3,4,5]
for c in list1:
    print(c)
    
ascii_codes = {'a':97,'b':98,'c':99} 
for c in ascii_codes:
    print(c)
    
for c in range(10):
    print(c)
    

#%% 012 for문 개념 배우기2(for~continue~break)
scope = [1,2,3,4,5]
for x in scope:
    print(x)
    if x<3:
        continue # 다음 반복문 수행, 3보다 작으면 그 다음 숫자를 출력한다.
    else:
        break    # for 반복문 탈출

for x in scope:
    print(x)
    if x>3: # 3의 다음 숫자까지 출력하고 멈춘다
        break
    
for x in scope:
    print(x)
    if x>=3:
        break # 3의 다음 숫자부터 멈춘다
        
#%% 013 for문 개념 배우기3(for~else)
# 왜 안되지
        
scope=[1,2,3,]

for x in scope:
    print(x)
    #break
else:
    print('Perfect')        


#%% 014 while문 개념 배우기(while~continue~break)
x=0
while x<=10:
    x=x+1
    if x<3:
        continue  # while 구문 처음으로 이동하여 반복문 계속
    print(x)
    if x>7:
        break     # while 구문 탈출
    
x=1
total = 0
while 1:    
    total = total + x
    if total > 100000 :
        print(x)
        print(total)
        break
    x=x+1
    
#%% 015 None 개념 배우기
val = None
condition = 1
if condition ==1:
    val = [1,2,3]
else:
    val="I love Python"
print(val)