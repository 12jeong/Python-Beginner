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

#%% <<<초급>>>
#%% 016 정수형 자료 이해하기
int_data = 10
bin_data = 0b10  # 2진수
oct_data = 0o10  # 8진수
hex_data = 0x10  # 16진수
long_data = 1234567890123456789
print(int_data)
print(bin_data)  # 10진수로 출력된다.
print(oct_data) 
print(hex_data)
print(long_data) # 정수형 상수의 최대값은 존재하지 않는다?

#%% 017 실수형 자료 이해하기
f1 = 1.0
f2 = 3.14
f3 = 1.56e3
f4 = -0.7e4
print(f1) # 소수로 표현한 값은 실수형 자료로 취급된다.
print(f2) 
print(f3) # e는 10의 거듭제곱을 나타낸다.
print(f4)

print(4/2) # 나눗셈의 결과는 실수형 자료가 된다

#%% 018 복소수형 자료 이해하기
c1 = 1+7j
print(c1.real) # 복소수의 실수부
print(c1.imag) # 복소수의 허수부

c2 = complex(2,-3)
print(c2)
    
#%% 019 대입 연산자 이해하기(=)
a=1
b=2
ret=a+b
# print('a와 b를 더한 값은','\n',ret,end='',"입니다.")
print('a와 b를 더한값은','\n')
print(ret,end='')
print("입니다.")

#%% 020 사칙 연산자 이해하기
a=2; b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a+a*b/a)
print((a+b)*(a-b))
print(a*b**a)

#%% 021 연산자 축약 이해하기
a=0
a+=1 # a+1
a-=5 # a-5
print(a)
a*=2 # a*2
a/=4 # a-4
print(a)

#%% 022 True와 False 이해하기
a = True     # TRUE 안됨
b = False    # FALSE 안됨
print(a==1)
print(b!=0)

# 무한 루프 로직
a=0
while True:
   a=a+1
   if a==10000:
       break
       
   
#%% 023 관계 연산자 이해하기
x=1; y=2
str1 = 'abc'; str2 = 'python'
print(x==y)
print(x!=y)
print(str1==str2)
print(str2=='python')
print(stl1 < str2) # 문자열은 사전순서로 비교! 우와

#%% 024 논리 연산자 이해하기 (and,or,not)
bool1=True
bool2=False
bool3=True
bool4=False

print(bool1 and bool2)
print(bool1 and bool3)
print(bool2 or bool3)
print(bool2 or bool4)
print(not bool1)
print(not bool2)


#%% 025 비트 연산자 이해하기 (&,|,~,^,>>,<<)
# 비트는 0 또는 1로만 표현될 수 있는 데이터 단위
# 1비트로 나타낼 수 있는 경우의 수는 두 가지
# 8비트는 1바이트. 따라서 1바이트로 나타낼 수 있는 경우는 2^8=256가지
# 이건 뭔지 잘 모르겠다
bit1 = 0x61                   # 16진수 61 : 0110 0001
bit2 = 0x62                   # 16진수 62 : 0110 0010
print(hex(bit1 & bit2))       # 비트간 and 연산 : 0110 0000
print(hex(bit1 | bit2))       # 비트간 or 연산  : 0110 0011
print(hex(bit1 ^ bit2))       # 비트간 xor 연산 : 0000 0011 - 같으면0 다르면1
print(hex(bit1 >> 1))         # 1만큼 오른쪽이동: 0101 1001
print(hex(bit1 << 2))         # 2만큼 왼쪽이동  : 0001 1000 0100 


#%% 026 시퀀스 자료형 이해하기
# 순서를 가지고 나열되어 있는 것을 시퀀스 자료형이라고 한다.
# 공통적인 특성 - 인덱싱, 슬라이싱, 연결(+), 반복(*), 멤버체크(in), 크기정보(len)
# 문자형, 리스트, 튜플
strdata = 'abcde'
listdata = [1,[2,3],'안녕']
tupledata = (100,200,300)

#%% 027 시퀀스 자료 인덱싱 이해하기 
# 인덱싱은 0부터 시작한다
strdata = 'Time is money!'
print(strdata[5]) 
print(strdata[-1]) # 끝에서부터 1번째

listdata = [1,2,[1,2,3]]
print(listdata[0])
print(listdata[-1]) 
print(listdata[2][-1])

#%% 028 시퀀스 자료 슬라이싱 이해하기
strdata = 'Time is money!'
print(strdata[1:5])
print(strdata[:7])
print(strdata[9:])
print(strdata[:-3])
print(strdata[-3:])
print(strdata[:])    # 처음부터 끝까지 슬라이싱
print(strdata[::2])  # 처음부터 끝까지 스텝을 2로해서 슬라이싱(1,3,5,7,9,11,13)\

#%% 029 시퀀스 자료 연결 이해하기 (+)
strdata1 = 'I love '
strdata2 = 'Python'
strdata3 = 'you'
listdata1 = [1,2,3]
listdata2 = [4,5,6]

print(strdata1 + strdata2)
print(strdata1 + strdata3)
print(listdata1 + listdata2)

#%% 030 시퀀스 자료 반복 이해하기 (*)
artist = '빅뱅'
sing = '뱅~'
dispdata = artist + '이 부르는 ' +sing*3
print(dispdata)

#%% 031 시퀀스 자료 크기 이해하기 (len)
strdata1 = 'I love python'
strdata2 = '나는 파이썬을 사랑합니다'
listdata = ['a','b','c',strdata1,strdata2]

print(len(strdata1))
print(len(strdata2))
print(len(listdata))
print(len(listdata[3]))

#%% 032 멤버체크 이해하기 (in) **
listdata = [1,2,3,4]
ret1 = 5 in listdata
ret2 = 4 in listdata
print(ret1); print(ret2)

strdata='abcde'
ret3 = 'c' in strdata
ret4 = 'l' in strdata
print(ret3); print(ret4)

#%% 033 문자열 이해하기
strdata1 = '나는 파이썬 프로그래머다'
strdata2 = "You are a programmer"
strdata3 = """I love
    python. You love
    python too!
    """        # """ """ 을 이용하면 줄바꿈을 하여도 문자열로 정의됩니다.
strdata4 = "My son's name is John"    # 문자열 내에 '가 있으면 "" 로 선언
strdata5 = '문자열 "abc"의 길이는 3입니다.' # 문자열 내에 "가 있으면 ''로 선언

#%% 034 문자열 포맷팅 이해하기 ***
# %s 문자열, %c 문자나 기호 한개, %f 실수, %d 정수, %% %기호고정

txt1 = '자바' ; txt2 = '파이썬'
num1 = 5; num2 = 10
print('나는 %s보다 %s에 더 익숙합니다.' %(txt1, txt2))
print('%s은 %s보다 %d배 더 쉽습니다.' %(txt2, txt1, num1))
print('%d + %d = %d' %(num1,num2,num1+num2))
print('작년 세계 경제 성장률은 전년에 비해 %d%% 포인트 증가했다.' %num1)

#%%
# 캐리지 리턴 '\r'
# 현재 위치를 나타내는 커서를 화면 맨 앞으로 이동
from time import sleep
for i in range(100):
    msg = '\r진행률 %d%%'%(i+1)
    print(' '*len(msg),end='')
    print(msg,end='')
    sleep(0.1)

#%% 035 이스케이프 문자 이해하기
print('나는 파이썬을 사랑합니다.\n파이썬은 자바보다 훨씬 쉽습니다.') # \n 줄바꾸기
print('Name:John Smith\tSex:Male\tAge:22') # \t 탭
print('이 문장은 화면폭에 비해 너무 길어 보기가 힘듭니다.\
      그래서 \\Enter키를 이용해 문장을 다음줄과 연속되도록 했습니다.') # \다음 줄도 계속된다는 표시 \\ 기호 자체
print('작은따옴표(\')와 큰 따옴표(\")는 문자열을 정의할 때 사용합니다.') # \', \" 기호 자체 사용

#%% 036 리스트이해하기 []
list1 = [1,2,3,4,5]
list2 = ['a','b','c']
list3 = [1,'a','abc',[1,2,3,4,5],['a','b','c']]
list1[0] = 6  # 리스트는 튜플과 달리 값 변경이 가능
print(list1)

def myfunc():
    print("안녕하세요")
list4 = [1,2,myfunc]
list4[2]
list4[2]()

#%% 037 튜플이해하기 ()
tuple1 = (1,2,3,4,5)
tuple2 = ('a','b','c')
tuple3 = (1,'a','abc',[1,2,3,4,5],['a','b','c'])
tuple1[0] = 6  # 에러. 튜플의 요소는 그 값을 변경할 수 없다!

def myfunc():
    print('안녕하세요')

tuple4 = (1,2,myfunc)
tuple4[2]()

#%% 038 사전이해하기 {}
dict1 = {'a':1,'b':2,'c':3}
print(dict1['a'])
dict1['d']=4
print(dict1)
dict1['b']=7
print(dict1)
print(len(dict1))

#%% 039 함수이해하기(def)
def add_number(n1,n2):
    ret=n1+n2
    return ret

def add_txt(t1,t2):
    print(t1+t2)
    
ans = add_number(10,15)
print(ans)

txt1 = '대한민국~'; txt2='만세!'
add_txt(txt1,txt2)


#%% 040 함수인자이해하기  **
def add_txt(t1,t2='파이썬'):
    print(t1+':'+t2)
    
add_txt('베스트')

add_txt(t2='대한민국',t1='1등')

# 가변인자는 인자 이름앞에 *를 붙인다
# *args : 튜플, *kwargs : 사전
def func1(*args):
    print(args)
    
def func2(width,height,**kwargs):
    print(kwargs)
    
func1()
func1(3,5,1,5)    
func2(10,20)
func2(10,20,depth=50,color='blue')

#%% 041 지역변수와 전역변수 이해하기 (global)
param = 10
strdata = '전역변수'

def func1():
    strdata='지역변수'
    print(strdata)
    
def func2(param):
    param = 1
    
def func3():
    global param
    param = 50

func1()
print(strdata)
print(param)
func2(param)
print(param)
func3()
print(param)
    
#%% 042 함수 리턴값 이해하기(return)
def reverse(x,y,z):
    return z,y,x        # 리턴값이 여러개인 경우에는 튜플로 리턴

ret=reverse(1,2,3)
print(ret)

r1,r2,r3=reverse('a','b','c')  # 튜플 요소 개수만큼 나누어서 리턴값을 받을 수 있다.
print(r1);print(r2);print(r3)


#%% 043 파이썬 모듈 이해하기

# 검증된 함수들이 하나의 파이썬 파일에 묶여있는 것이 모듈
# 모듈을 가져와서 사용하는 것을 임포트 한다고 한다.

import time

print('5초간 프로그램을 정지합니다')
time.sleep(5) # time 모듈이 제공하는 sleep()함수 
print('5초가 지나갔습니다')

# myplib.py에 있는 함수를 이용할 수 있다.
import myplib

ret1 = myplib.add_txt('대한민국','1등')
ret2 = myplib.reverse(1,2,3,)
print(ret1)
print(ret2) 

#%%  ######### 044 파이썬 패키지 이해하기  
# 파이썬 모듈을 계층적인 디렉터리 형태로 구성한 것 


#%% 049 클래스 이해하기 (class) *
# 프로그래머가 지정한 이름으로 만든 하나의 독립된 공간, 이름공간(name space)
# 클래스 멤버(변수역할), 클래스 메소드(함수 역할)

class MyClass: # 클래스 정의
    var = '안녕하세요'  # 클래스 멤버 정의, 메소드 밖에서 정의됨
    def sayHello(self): # 클래스 메소드 정의, 클래스 내에서 정의됨.
        print(self.var) # 첫번째 인자가 반드시 self로 시작되어야 한다.
                        # self는 이 클래스의 인스턴트 객체를 가리키는 참조자
obj = MyClass()         # 클래스를 활용하려면 인스턴스 객체로 만들어야 한다. 호출하면 됨.
print(obj.var)          
obj.sayHello()

#%% 050 클래스 멤버와 인스턴스 멤버 이해하기
class MyClass:
    var = '안녕하세요!!'          # 클래스 메소드 바깥에서 선언되었으므로 클래스 멤버
    def sayHello(self):           # 클래스 메소드
        param1 = '안녕'           # sayHello()에서만 유효한 지역변수
        self.param2 = '하이'      # 클래스 매소드 안에서 slef와 함께 선언되는 변수 : 인스턴스 멤버
        print(param1)
        print(self.var)
        
obj = MyClass 
print(obj.var) 
obj.sayHello()                    # 안된다,,,

#%% 051 클래스 메소드 이해하기
class MyClass:
    def sayHello(self):
        print('안녕하세요')
        
        def sayBye(self,name):
            print('%s! 다음에보자!'%name)
            
obj = MyClass()
obj.sayHello()
obj.sayBye('철수')               # 안된다,,,




#%% 055 예외처리이해하기 1(try~except)
try:
    print('안녕하세요')
    print(param)
except:
    print('예외가 발생했습니다!') # param이 정의되지 않은 변수이므로 예외를 발생시킴
    
#%% 056 예외처리이해하기 2(try~except~else)
try:
    print('안녕하세요')
    # print(param)
except:
    print('예외가 발생했습니다!')
else:
    print('예외가 발생하지 않았습니다.')
    
    
#%% 057 예외처리이해하기 3(try~except~finally)
try:
    print('안녕하세요')
    print(param)
except:
    print('예외가 발생했습니다!')
finally:
    print('무조건 실행하는 코드')
    
#%% 058 예외처리이해하기 4(try~except Exception as e)
try:
    print(param)
except Exception as e:
    print(e)                  # e: 예외 발생 내요이 담긴 변수... 자세한건 문서
    
    
#%% 059 예외처리이해하기 5(try~except 특정 예외)
import time
count = 1
try : 
    while True:
        print(count)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt:
    print('사용자에 의해 프로그램이 중단되었습니다')  # ctrl+c
    
    
    
#%% <<<중급>>>>
#%% 060 사용자 입력받기(input)
k = input('<값>을 입력하세요:')
print('당신이 입력한 값은 <' +k+ '>입니다.')
    
#%% 061 자료형 확인하기(type)
numdata = 57
strdata = '파이썬'
listdata = [1,2,3]
dictdata = {'a':1,'b':2}

def func():
    print('안녕하세요.')
    
print(type(numdata))
print(type(strdata))
print(type(listdata))
print(type(dictdata))
print(type(func))
    
#%% 062 나눗셈에서 나머지만 구하기(%)
a = 11113
b = 23
ret = a%b
print('<%d>를 <%d>로 나누면 <%d>가 나머지로 남습니다.' %(a,b,ret))
    

12 % 3 
12 % 5

#%% 063 몫과 나머지 구하기 (divmod)
a = 11113
b = 23
ret1, ret2= divmod(a,b)

print(ret1)
print(ret2)

#%% 064 10진수를 16진수로 변환하기(hex)
h1 = hex(97)    # 문자열
h2 = hex(98)
ret1 = h1+h2
print(ret1)
a = int(h1,16)
b = int(h2,16)  # 정수로 변환
ret2 = a+b
print(hex(ret2))

#%% 065 10진수를 2진수로 변환하기(bin)
b1 = bin(97)
b2 = bin(98)
ret = b1+b2
print(ret)
a = int(b1,2)
b = int(b2,2)
ret2 = a+b
print(bin(ret2))

#%% 066 2진수, 16진수를 10진수로 변환하기(int)
bnum = 0b11110000
bstr = '0b11110000'
hnum = 0xf0
hstr = 'oxf0'     # 이후 생략

#%% 067 절대값 구하기(abs)
abs1 = abs(-3)
abs2 = abs(-5.72)
abs3 = abs(3+4j) # 복소수의 크기 root(3^2+4^2)
print(abs1)
print(abs2)
print(abs3)

#%% 068 반올림수 구하기(round)
ret1 = round(1118) # 1118
ret2 = round(16.554) #17
ret3 = round(1118,-1) #1120
ret4 = round(16.554,2) #16.55
ret5 = round(16.554,1) #16.6
ret6 = round(16.554,0) #17
print(ret6) 

#%% 069 실수형 자료를 정수형 자료로 변환하기(int)
idata1 = int(-5.4)      # -5
idata2 = int(1.78e1)    # 17 
idata3 = int(171.56)    # 171

#%% 070 정수형 자료를 실수형 자료로 변환하기 (float)
fdata = float(10)
print(fdata) #10.0

#%% 071 정수 리스트에서 소수만 걸러내기(filter) **
def getPrime(x):
    for i in range(2,x-1):
        if x%i == 0:
            break
    else:
        return x

listdata = [117,119,1113,11113,11119]
ret = filter(getPrime,listdata)
print(list(ret))

#%% 072 최대값, 최소값 구하기
listdata=[9.96, 1.27, 5.07, 6.45, 8.38, 9.29, 4.93, 7.73, 3.71, 0.93]
maxval = max(listdata)
minval = min(listdata)
print(maxval)
print(minval)

txt = "Alotofthingsoucvcreachday"
maxval = max(txt)
minval = min(txt)
print(maxval)
print(minval)

maxval = max(2+3, 2+3, 2**3, 3**2)
minval = min('abz','a12')
print(maxval)
print(minval) # 이건 뭘까?

#%% 073 1바이트에서 하위 4비트 추출하기 ?
a = 107
b = a & 0x0f
print(b)

#%% 074 1바이트에서 상위 4비트 추출하기 ?
a = 107
b = (a>>4) & 0x0f
print(b)

#%% 075 문자열에서 특정 위치의 문자 얻기
txt1 = 'A tale that was not right'
txt2 = '이또한 지나가리아'
print(txt1[5])
print(txt2[-2])

#%% 076 문자열에서 지정한 구간의 문자열 얻기
txt1 = 'A tale that was not right'
txt2 = '이또한 지나가리아'
print(txt1[3:7])
print(txt1[:6])
print(txt2[-4:])

txt3 = 'python'
for i in range(len(txt3)):
    print(txt3[:i+1])
    
#%% 077 문자열에서 홀수 번째 문자만 추출하기
txt = 'aAbBcCdDeEfFgGhHiIjJkK'
ret = txt[::2] # 처음부터 끝까지 스텝 2로 슬라이싱
print(ret)

#%% 078 문자열을 거꾸로 만들기
txt = 'abcdefghik'
ret = txt[::-1] # 처음부터 끝까지 스텝 -1로 슬라이싱
print(ret)

#%% 079 두개의 문자열 합치기(+)
filename = input('저장할 파일이름을 입력하세요:')
filename = filename + '.jpg'
display_msg = '당신이 저장한 파일을 <' +filename+ '>입니다.'
print(display_msg)

#%% 080 문자열을 반복해서 새로운 문자열로 만들기(*)
msg1 = '여러분'
msg2 = '파이팅!'
display_msg = msg1 + ',' + msg2*3 + '~!'
print(display_msg)

#%% 081 문자열에서 특정 문자가 있는지 확인하기(in)
msg = input('임의의 문장을 입력하세요:')
if 'a' in msg:
    print('당신이 입력한 문장에는 a가 있습니다.')
else:
    print('당신이 입력한 문장에는 a가 없습니다.')

#%% 082 문자열에서 특정 문자열이 있는지 확인하기(in)
msg = input('임의의 문장을 입력하세요:')
if 'is' in msg:
    print('당신이 입력한 문장에는 is가 있습니다.')
else:
    print('당신이 입력한 문장에는 is가 없습니다.')
    
#%% 083 문자열 길이 구하기(len)
msg = input('임의의 문장을 입력하세요:')
msglen = len(msg) # 유니코드로 처리하기 때문에 6으로 같지만
#msglen = len(msg.encode()) # 영어는 6바이트, 한글은 16바이트
print("당신이 입력한 문장의 길이는 <%d>입니다." %msglen)

#%% 084 문자열이 알파벳(언어 문자)인지 검사하기(isalpha)
txt1 = 'A'
txt2 = '안녕'
txt3 = 'Warcraft Three'
txt4 = '3PO'
ret1 = txt1.isalpha()
ret2 = txt2.isalpha()
ret3 = txt3.isalpha()
ret4 = txt4.isalpha()
print(ret1)
print(ret2)
print(ret3) # 공백은 언어 문자가 아니다
print(ret4) # 숫자는 언어 문자가 아니다

#%% 085 문자열이 숫자인지 검사하기(isdigit)
txt1 = '010-1234-5678'
txt2 = 'R2D2'
txt3 = '1212'
ret1 = txt1.isdigit()
ret2 = txt2.isdigit()
ret3 = txt3.isdigit()
print(ret1)
print(ret2)
print(ret3)


#%% 086 문자열이 알파벳 또는 숫자인지 검사하기(isalnum)
txt1 = '안녕하세요?'
txt2 = '1.Title-제목을 넣으세요'
txt3 = '3피오R2D2'
ret1 = txt1.isalnum()
ret2 = txt2.isalnum()
ret3 = txt3.isalnum()
print(ret1) # 물음표가 들어있어서 FALSE
print(ret2) # .와 -가 들어있어서 FALSE
print(ret3) # 문자와 숫자로 구성되어 있으므로 TRUE

#%% 087 문자열에서 대소문자 변환하기(upper,lower)
txt = 'A lot of Things occur each day.'
ret1 = txt.upper()
ret2 = txt.lower()
print(ret1)
print(ret2)

#%% 088 문자열에서 좌우 공백 제거하기(lstrip, rstrip, strip)
txt = ' 양쪽에 공백이 있는 문자열입니다. '
ret1 = txt.lstrip() # 왼쪽 공백 제거
ret2 = txt.rstrip() # 오른쪽 공백 제거
ret3 = txt.strip()  # 좌우 공백 제거
print('<'+txt+'>')
print('<'+ret1+'>')
print('<'+ret2+'>')
print('<'+ret3+'>')

#%% 089 문자열을 수치형 자료로 변환하기(int, float)
numbstr = input('숫자를 입력하세요:') # 문자열입니다.
try:
    num = int(numbstr) # 정수 형식만 정수형 자료로 변환합니다.  
    print('당신이 입력한 숫자는 정수 <%d>입니다.'%num) # %d : 정수
except:
    try:
        num = float(numbstr) # 실수 형식만 실수형 자료로 변환합니다.
        print('당신이 입력한 숫자는 실수 <%f>입니다.'%num) # %f : 실수
    except:
        print('+++ 숫자를 입력하세요~ +++')


#%% 090 수치형 자료는 문자열로 변환하기 (str)
num1 = 1234
num2 = 3.14

numstr1 = str(num1)
numstr2 = str(num2)
print('num1을 문자열로 변환한 겂은 "%s"입니다.'%numstr1) # %s : 문자열
print('num2을 문자열로 변환한 값은 "%s"입니다.'%numstr2)

#%% 091 문자열에 있는 문자(열) 개수 구하기 (count)
txt = ' A lot of day things.'
word_count1 = txt.count('o')
word_count2 = txt.count('day')
word_count3 = txt.count(' ')
print(word_count1)
print(word_count2)
print(word_count3)

#%% 092 문자열에서 특정 문자(열) 위치 찾기 (find)
txt = 'A lot of things occur each day. every day.'
offset1 = txt.find('e')
offset2 = txt.find('day') # each day의 day
offset3 = txt.find('day',30) # 30번 인덱스 이후부터 day를 찾는다. every day의 day
print(offset1)
print(offset2)
print(offset3) 
offset4 = txt.find('ijeong')
print(offset4) # find()에서 찾을 수 없으면 -1 리턴

#%% 093 문자열을 특정 문자(열)로 분리하기(split)
url = "http://www.naver.com/news/today=20160831"
log = 'name:홍길동 age:17 sex:남자 nation:조선'

ret1 = url.split('/') # 슬래쉬 구분되어 있는 문자 파싱
print(ret1)

ret2 = log.split()  # 공백과 콜론(:)으로 구분되어 있는 문자열을 정의 
print(log)
print(ret2)
for data in ret2:
    d1,d2 = data.split(':')
    print('%s -> %s'%(d1,d2))

#%% 094 문자열을 특정 문자(열)로 결합하기 (join)
loglist = ['2016/08/26 10:12:11','200','OK','이 또한 지나가리라']
bond = ';' # 세미콜론을 변수로 만들고
log = bond.join(loglist) # 세미콜론으로 **리스트**의 요소를 연결한다
print(log)

#%% 095 문자열에서 특정 문자(열)를 다른 문자(열)로 바꾸기 (replace)
txt = 'My password is 1234'
ret1 = txt.replace('1','0')
ret2 = txt.replace('1','python')
print(ret1)
print(ret2)

txt = '매일 많은 일들을 일어납니다.'
ret3 = txt.replace('매일','항상')
ret4 = ret3.replace('일','사건')
print(ret3)
print(ret4)


#%% 096 문자열을 바이트 객체로 바꾸기 (encode)
u_txt = 'I love python'
b_txt = u_txt.encode() # u_txt를 UTF-8로 인코딩한 바이트 객체로 변환
print(u_txt)
print(b_txt) # 파이썬 3에서 바이트 객체는 문자열 앞에 b를 붙여 나타낸다

ret1 = 'I' == u_txt[0]  # u_txt[0]은 문자 'I'
ret2 = 'I' == b_txt[0]  # b_txt[0]은 정수 73, # 대문자 I는 컴퓨터 메모리에 73이라는 정수값으로 기록
print(ret1) 
print(ret2)

#%% 097 바이트 객체를 문자열로 바꾸기 (decode)
b_txt = b'A lot of things occur each day.'
u_txt = b_txt.decode() # decode를 유니코드 문자열로 변환
print(u_txt)

#%% 098 문자열을 정렬하기 (sorted, join)
strdata = input('정렬할 문자열을 입력하세요:')
ret1 = sorted(strdata) 
ret2 = sorted(strdata,reverse=True)
print(ret1) # 오름차순 리스트
print(ret2) # 내림차순 리스트
 
ret1 = ''.join(ret1) # 정렬한 결과 리스트를 문자열로 생성***
ret2 = ''.join(ret2) 
print('오름차순으로 정렬된 문자열은 <' +ret1 +'>입니다.')
print('내림차순으로 정렬된 문자열은 <' +ret2 +'>입니다.')

#%% 099 순차적인 정수 리스트 만들기 (range)
range1= range(10) # 0 이상 10 미만 정수 
range2 = range(10,20) # 10이상 20 미만 정수
print(range1) # range 객체는 리스트가 아니다.
print(range2)
print(list(range1)) # list를 통해 ragne객체의 실제 값이 출력됨
print(list(range2))

ret = 0 
for i in range(10):
    ret += (i+1)

print(ret)

#%% 100 리스트에서 특정 위치의 요소 얻기
listdata = [1,2,'a','b','c',[4,5,6]]
val1 = listdata[1]
val2 = listdata[3]
val3 = listdata[5][1]
print(val1)  # 2
print(val2)  # b
print(val3)  # 5

#%% 101 리스트에서 특정 요소의 위치 구하기 (index)
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
planet = '지구'
pos = solarsys.index(planet) # 리스트객체의 index : 요소가 최초로 나타나는 위치의 인덱스 리턴
print("%s은(는) 태양계에서 %d번째에 위치하고있습니다."%(planet,pos))
pos = solarsys.index(planet,5)  # 인덱스가 5 이상인 요소부터 검색하여 planet이 나타내는 위치 리턴
print("%s은(는) 태양계에서 %d번째에 위치하고있습니다."%(planet,pos))

#%% 102 리스트에서 특정 위치의 요소를 변경하기 
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
planet = '화성'
pos = solarsys.index(planet)
solarsys[pos]='Mars'
print(solarsys)

#%% 103 리스트에서 특정 구간에 있는 요소 추출하기
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
rock_planets = solarsys[1:4] # 슬라이싱한 리스트
gas_planet = solarsys[4:]
print('태양계의 암석형 행성:',end='');print(rock_planets)

#%% 104 리트스에서 짝수 번째 요소만 추출하기
listdata= list(range(1,21))
evenlist = listdata[1::2] # 두번째(index=1)부터 끝까지 스텝 2로 슬라이싱
print(evenlist)

oddlist = listdata[::2] # 홀수 번째 요소
print(oddlist) # 첫번째(index=0)부터 끝까지 스텝 2로 슬라이싱


















