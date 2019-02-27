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

#%% 104 리스트에서 짝수 번째 요소만 추출하기
listdata= list(range(1,21))
evenlist = listdata[1::2] # 두번째(index=1)부터 끝까지 스텝 2로 슬라이싱
print(evenlist)

oddlist = listdata[::2] # 홀수 번째 요소
print(oddlist) # 첫번째(index=0)부터 끝까지 스텝 2로 슬라이싱

#%% 105 리스트 요소 순서를 역순으로 만들기1 (reverse)
listdata = list(range(5))
listdata.reverse()
print(listdata)

#%% 106 리스트 요소 순서를 역순으로 만들기2 (reversed)
listdata = list(range(5))
ret1 = reversed(listdata)
print('원본리스트',end='');print(listdata)
print('역순리스트',end='');print(list(ret1))

ret2 = listdata[::-1]
print("슬라이싱이용 역순리스트",end='');print(ret2)

#%% 107 리스트 합치기 (+)
listdata1 = ['a','b','c','d','e']
listdata2 = ['f','g','h','i','j']
listdata3 = listdata1 + listdata2
listdata4 = listdata2 + listdata1
print(listdata3)
print(listdata4)

#%% 108 리스트 반복하기 (*)
listdata = list(range(3))
ret = listdata*3
print(ret)

#%% 109 리스트에 요소 추가하기 (append)
listdata = []
for i in range(3):
    txt = input('리스트에 추가할 값을 입력하세요[%d/3]:'%(i+1))
    listdata.append(txt) 
    print(listdata) # 대박, 멋있다
    
#%% 110 리스트의 특정 위치에 요소 삽입하기 (insert)
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
pos = solarsys.index('목성')
solarsys.insert(pos,'소행성')
print(solarsys)

#%% 111 리스트의 특정 위치의 요소 제거하기 (del)
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
del solarsys[0]  # 태양 제거
print(solarsys)
del solarsys[-2] # 해왕성 제거
print(solarsys)

#%% 112 리스트에서 특정 요소 제거하기 (remove)
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
solarsys.remove("태양")
print(solarsys)

#%% 113 리스트에서 특정 구간에 있는 모든 요소 제거하기
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
del solarsys[1:3]
print(solarsys)

#%% 114 리스트에 있는 요소 개수 구하기
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
listsize = len(listdata)
print(listsize)

#%% 115 리스트에서 특정 요소 개수 구하기 (count)
listdata = [2,2,1,3,8,5,7,6,2,3,9,4,4]
c1 = listdata.count(2)
c2 = listdata.count(7)
print(c1)
print(c2)

#%% 116 리스트 제거하기 (del)
listdata = [2,2,1,3,6,7,3,2,4,2,2,7]
del listdata
#print(listdata)

#%% 117 리스트 요소 정렬하기 1 (sort)
namelist = ['Mary','Sams','Aimy','Tom','Michale','Bob','Kelly']
namelist.sort() # 원본리스트를 변경한다.
print(namelist)
namelist.sort(reverse=True)
print(namelist)

#%% 118 리스트 요소 정렬하기 2 (sorted)
namelist = ['Mary','Sams','Aimy','Tom','Michale','Bob','Kelly']
ret1 = sorted(namelist)
ret2 = sorted(namelist,reverse=True)
print(namelist)
print(ret1)
print(ret2)

#%% 119 리스트 요소 무작위로 섞기 (shuffle)
from random import shuffle

listdata = list(range(1,11))
for i in range(3):
    shuffle(listdata)
    print(listdata)
    
#%% 120 리스트의 모든 요소를 인덱스와 쌍으로 추출하기 (enumerate)
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
ret = list(enumerate(solarsys))
print(ret) # 인덱스와 요소의 쌍으로 이루어져 있는 리스트

for i, body in enumerate(solarsys):  # for 문에 자주 쓰인다
    print('태양계의 %d번째 천체:%s'%(i,body))


#%% 121 리스트의 모든 요소의 합 구하기(sum)
listdata = [2,2,1,3,6,3,2,2,2,4,5,3]
ret = sum(listdata)
print(ret)

#%% 122 리스트 요소가 모두 참인지 확인하기 (all,any)
# all은 모두가 참
# any는 하나이상 참
listdata1 = [0,1,2,3,4]
listdata2 = [True, True, True]
listdata3 = ['',[],(),{},None,False]
print(all(listdata1)) # 거짓(0)인 요소를 가지고 있으므로 FALSE
print(any(listdata1))
print(all(listdata2))
print(any(listdata2))
print(all(listdata3)) # 모두 거짓
print(any(listdata3))


#%% 123 사전에 요소 추가하기
solar1 = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
solar2 = ['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
solardict = {}
for i,k in enumerate(solar1):
    val = solar2[i]
    solardict[k] = val

print(solardict)

ret = list(enumerate(solar1))
print(ret)
print(enumerate(solar1))

#%% 124 사전의 특정 요소값 변경하기
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
names['Aimy']=10000 # key가 Aimy에 해당하는 값 val을 10000으로 변
print(names)

#%% 125 사전의 특정 요소 제거하기 (del)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
del names['Sams']
print(names)

#%% 126 사전의 모든 요소 제거하기 (clear)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
names.clear()
print(names)

#%% 127 사전에서 키만 추출하기 (keys)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
ks = names.keys()
print(ks) # 사전 뷰 객체로 리턴

for k in ks:
    print('Key:%s \tValue:%d' %(k,names[k]))

#%% 128 사전에서 값만 추출하기 (values)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
vals = names.values()
print(vals)

vals_list=list(vals)
ret = sum(vals_list)
print('출생아 수 총계: %d'%ret)

#%% 129 사전 요소를 모두 추출하기 (items)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
items = names.items()
print(items)

for item in items:
    print(item)

#%% 130 사전에 특정 키가 존재하는지 확인하기 (in)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
k = input('이름을 입력하세요')
if k in names:
    print('이름이 <%s>인 출생아 수는 <%d>명입니다.'%(k,names[k]))
else:
    print('자료에 <%s>인 이름이 존재하지 않습니다.'%k)

# 사전에 key가 있는지 확인    
'Mary' in names
'Han' in names

#%% 131 사전 정렬하기 (sorted)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
ret1 = sorted(names)
print(ret1) # key 값이 정렬됨

# 키:값 모두 정렬된 쌍으로 나오려면?
def f1(x):
    return x[0]

def f2(x):
    return x[1]

# sorted()는 key인자를 이용하여 정렬할 기준이 되는 값을 지정해줌. 함수여야한다
ret2 = sorted(names.items(),key=f1) # 정렬할 데이터의 첫번째 요소(key)를 기준으로 정렬
print(ret2)

ret3 = sorted(names.items(),key=f2) # 정렬할 데이터의 두번째 요소(values)를 기준으로 정렬
print(ret3)

#%% 132 문자 코드값 구하기(ord)
ch = input('문자를 1개 입력하세요:')
if len(ch)!=0:
    ch=ch[0]
    chv=ord(ch) # ord : 문자를 컴퓨터가 인식하는 코드값으로 반환. 아스키(ASCII)코드값?
    print('문자:%s\t코드값:%d[%s]'%(ch,chv,hex(chv)))
    
#%% 133 코드값이 대응하는 문자 얻기 (chr)
val = input('문자 코드값을 입력하세요:')
val = int(val) # 정수값을 입력하면
try:
    ch = chr(val) # chr은 코드값을 입력받아 이에 해당하는 문자를 출력한다
    print('코드값:%d[%s],문자:%s'%(val,hex(val),ch))
except ValueError:
    print('입력한<%d>에 대한 문자가 존재하지 않습니다!'%val)
    
#%% 134 문자열로 된 식을 실행하기 (eval)
expr1 = '2+3'
expr2 = 'round(3.7)'
ret1 = eval(expr1)
ret2 = eval(expr2)
print('<%s>를 eval()로 실행한 결과:'%expr1,end='');print(ret1)
print('<%s>를 eval()로 실행한 결과:'%expr2,end='');print(ret2)
    
#%% 135 이름없는 한줄짜리 함수 만들기(lambda)
# def가 아니라
add = lambda x,y:x+y # labmda 인자, 인자, ..., : 실행코드
ret=add(1,3)
print(ret)

funcs = [lambda x:x+'.pptx', lambda x:x+'docx']
ret1 = funcs[0]('Intro')
ret2 = funcs[1]('Report')
print(ret1)
print(ret2)

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
ret3 = sorted(names.items(),key=lambda x:x[0]) # names.items() : 사전 요소를 모두 추출
print(ret3)

#%% 136 인자를 바꾸어 함수를 반복 호출하여 결과값 얻기 (map) **좋
f = lambda x:x*x
args = [1,2,3,4,5]
ret = map(f,args)
print(list(ret))




    