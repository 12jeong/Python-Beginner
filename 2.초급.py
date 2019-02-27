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
    
    