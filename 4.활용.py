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

import os
os.getcwd()
from os import chdir
chdir('C:\\Users\\UOS\\Documents\\GITHUB\\Python-Beginner')

# 부가설명
# 4spaces

#%% <<<활용>>>>
#%% 137 텍스트 파일을 읽고 출력하기(read)
f = open('C:\\Users\\UOS\\Documents\\GITHUB\\Python-Beginner\\stockcode.txt','r') #파일이름, r:텍스트모드로 읽기

data = f.read() # 한꺼번에 읽는다
print(data)

f.close() # 왜 해야하지?

#%% 138 텍스트 파일을 한줄씩 읽고 출력하기1 (readline) 
# 어디에쓰는거지?
f = open('C:\\Users\\UOS\\Documents\\GITHUB\\Python-Beginner\\stockcode.txt','r')

# 초기값
line_num = 1
line = f.readline()
while line: # line이 빈 문자열일때까지 while 루프 반복
    print('%d %s'%(line_num,line),end='') # end=''를 해야 다음줄에 빈줄이 안생긴다
    line = f.readline()
    line_num +=1
f.close()

#%% 139 텍스트 파일을 한줄씩 읽고 출력하기2 (readlines)
f = open('C:\\Users\\UOS\\Documents\\GITHUB\\Python-Beginner\\stockcode.txt','r')
lines = f.readlines()

print(lines)

for line_num, line in enumerate(lines):     # enumerate : 리스트의 모든 요소를 인덱스와 쌍으로 추출
    print('%d %s'%(line_num+1,line),end='')
f.close

#%% 140 화면에서 사용자 입력을 받고 파일로 쓰기(write)
text = input("파일에 저장할 내용을 입력하세요:")
f = open('mydata.txt','w') # w: 텍스트 모드로 쓰
f.write(text) # 이미 내용이 있으면 덮어 씀
f.close()

#%% 141 텍스트 파일에 한줄씩 쓰기 (wirtelines)
count = 1
data = []
print("파일에 내용을 저장하려면 내용을 입력하지 말고 [Enter]를 누르세요.")
while True:
    text = input("[%d]파일에 저장할 내용을 입력하세요 :"%count)
    if text == '':
        break
    data.append(text+'\n') # 데이터 추가
    count +=1

f = open('mydata.txt','w')
f.writelines(data)
f.close() # 여기까지 해야 데이터가 저장됨

#%% 142 텍스트 파일 복사하기 (read, write)
f = open('stockcode.txt','r')
h = open('stockcode_copy.txt','w')

data = f.read()
h.write(data)

f.close()
h.close()

#%% 143 바이너리 파일 복사하기 (read.write)
bufsize = 1024 # 1KB 단위로 파일을 읽기 위해서 정의한다
f = open('img_sample.jpg','rb')
h = open('img_sample_copy.jpg','wb')

data = f.read(bufsize)            # 바이너리 데이터는 용량이 크므로 한번에 읽고쓰지말고 일정한 크기 단위로 읽고 쓴다
while data:
    h.write(data)
    data = f.read(bufsize)
    
f.close()
h.colse()

#%% 144 파일을 열고 자동으로 닫기 (with~as)
# f = open('stockcode.txt','r')
# 파일 처리 코드
# f.close()

with open('stockcode.txt','r') as f:                   # 끝나면 자동으로 파일을 닫아줌
    for line_num, line in enumerate(f.readlines()):
        print('%d %s' %(line_num+1,line),end='')

#%% 145 파일의 특정 부분만 복사하기 (seek,read,write)
spos = 105 # 파일 읽는 위치
size = 500 # 읽을 크기

f = open('stockcode.txt','r')
h = open('stockcode_part.txt','w')

f.seek(spos)
data = f.read(size)
h.write(data)

h.close() # 105바이트 위치부터 500바이트를 읽어 저장
f.close()


#%% 146 파일 크기 구하기 (os.path.getsize)
from os.path import getsize

file1 = 'stockcode.txt'
file2 = 'img_sample.jpg'
file_size1 = getsize(file1)
file_size2 = getsize(file2)

print('File Name: %s \tFile Size: %d'%(file1,file_size1))
print('File Name: %s \tFile Size: %d'%(file2,file_size2))


#%% 147 파일 삭제하기 (os.remove)
from os import remove

target_file = 'stockcode_copy.txt'
k = input('[%s] 파일을 삭제하겠습니까? (y/n)'%target_file)
if k == 'y':
    remove(target_file)
    print('[%s]를 삭제했습니다.'%target_file)

#%% 148 파일이름 바꾸기 (os.remove)
from os import rename

target_file = 'stockcode.txt'
newname = input('[%s]에 대한 새로운 파일이름을 입력하세요.'%target_file)
rename(target_file,newname)
print('[%s]->[%s]로 파일이름이 변경되었습니다.'%(target_file,newname))


#%% 149 파일을 다른 디렉토리로 이동하기 (os.rename)
from os import rename

target_file = 'stockcode2.txt'
newpath = input('[%s]를 이동할 디렉터리의 절대경로를 입력하세요:'%target_file)

if newpath[-1] == '/':
    newname = newpath + target_file
else :
    newname = newpath + '/' + target_file

try :
    rename(target_file,newname)
    print('[%s]->[%s]로 이동되었습니다.'%(target_file,newname))
except FileNotFoundError as e:
    print(e)


#%% 150 디렉터리에 있는 파일목록 얻기 (os.listidr, glob.glob)
import os, glob

folder = 'C:\\Users\\UOS\\Documents\\GITHUB\\Python-Beginner'
file_list = os.listdir(folder)
print(file_list)

files = '*.txt'
file_list = glob.glob(files) # 조건에 맞는 파일 리턴
print(file_list)

#%% 151 현재 디렉터리 확인하고 바꾸기 (os.getcwd, os.chair)
import os

pdir = os.getcwd() ;print(pdir)
os.chdir('..'); print(os.getcwd()) # 현재 작업 디렉터리의 부모 디렉터리로 이동
os.chdir(pdir); print(os.getcwd())

#%% 152 디렉터리 생성하기 (os.mkdir)
import os

newfolder ='C:\\Users\\UOS\\Documents\\GITHUB\\Python-Beginner\\tmp'
try:
    os.mkdir(newfolder)
    print('[%s] 디렉터리를 새로 생성했습니다.'%newfolder)
except Exception as e:
    print(e)
    
#%% 153 디렉터리 제거하기 (os.rmdir)
import os

target_folder = 'tmp'
k = input('[%s] 디렉터리를 삭제하겠습니까?(y/n)'%target_folder)
if k == 'y':
    try:
        os.rmdir(target_folder)
        print('[%s] 디렉터리를 삭제합습니다.'%target_folder)
    except Exception as e:
        print(e)


#%% 154 하위 디렉터리 및 파일 전체 삭제하기 (shutil.rmtree)
import shutil
import os

target_folder = 'C:\\Users\\UOS\\Documents\\GITHUB\\Python-Beginner\\tmp'
print('[%s] 하위 모든 디렉터리 및 파일들을 삭제합니다.'%target_folder)
for file in os.listdir(target_folder):
    print(file)
k = input('[%s]를 삭제하겠습니까? (y/n)'%target_folder)
if k == 'y':
    try :
        shutil.rmtree(target_folder)    # shutil 모듈의 rmtree() 이용
        print('[%s] 하위 모든 디렉터리 및 파일들을 삭제했습니다.'%target_folder)
    except Exception as e:
        print(e)
        
#%% 155 파일이 존재하는지 체크하기 (os.path.exists)
import os
from os.path import exists

dir_name = input('새로 생성할 디렉터리 이름을 입력하세요:')
if not exists(dir_name):
    os.mkdir(dir_name)
    print('[%s] 디렉터리를 생성했습니다.'%dir_name)
else:
    print('[%s]은(는) 이미 존재합니다.'%dir_name) # mydata.txt / tmp
    
    
#%% 156 파일인지 디렉터리인지 확인하기 
import os
from os.path import exists,isdir,isfile

files = os.listdir()
for file in files:
    if isdir(file):
        print('DIR:%s'%file)

for file in files:
    if isfile(file):
        print('FILE:%s'%file)
        
#%% 157 현재 시간을 년-월-일 시:분:초로 출력하기 (localtime, strtime)
from time import localtime, strftime

# localtime : 대한민국의 현재시각을 time,struct_Time 형식의 데이터로 리턴
# 대한민국 표준시는 UTC기준 UTC+9

print(strftime('%Y-%m-%d %X\t',localtime()) )

logfile = 'test.log'
def writelog(logfile,log):
    time_stamp = strftime('%Y-%m-%d %X\t',localtime()) 
    log = time_stamp + log + '\n'
    
    with open(logfile,'a') as f:
        f.writelines(log)
    
writelog(logfile,'첫 번째 로깅 문장입니다.')

###

t = localtime()
print(t) # struc_time 형식
t[0]
t.tm_year

#%% 158 올해 경과된 날짜수 계산하기 (localtime)

from time import localtime

t = localtime() # 현재 시간
start_day = '%d-01-01'%t.tm_year # 2019-01-01
elpased_day = t.tm_yday          # t.tm_yday : 해당 년도의 1월 1일부터 현재 날짜까지 경과된 날짜수 나타냄

print('오늘은 [%s]이후 [%d]일째 되는 날입니다.' %(start_day,elpased_day))

#%% 159 오늘의 요일 계산하기
from time import localtime

weekdays = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일'] # 0이면 월요일 문자열 리스트 정의

t = localtime() # 현재 시간을 struct_time 형식으로 구한다 print(t)
today = '%d-%d-%d'%(t.tm_year,t.tm_mon,t.tm_mday) # 오늘 날짜를 문자열로 구성한다
week = weekdays[t.tm_wday] # 요일 문자열 구한다

print('[%s] 오늘은 [%s]입니다.'%(today,week))

#%% 160 프로그램 실행 시간 계산하기
from datetime import datetime

start = datetime.now()
print('1에서 백만까지 더합니다.')
ret=0
for i in range(1000000):
    ret += i
print('1에서 백만까지 더한 결과:%d'%ret)
end = datetime.now()

elpased = end - start
print('총 계산 시간',end='');print(elpased)
elapsed_ms = int(elpased.total_seconds()*1000)
print('총 계산 시간:%dms' %elapsed_ms)


#%% 161 주어진 숫자를 천 단위로 구분하기

# num_ex = '12345'
# num_ex = num_ex[::-1]
# print(num_ex)

num = input('아무 숫자를 입력하세요:') # 단, 문자형

if num.isdigit():         # 숫자로만 구성되어있으면
    num = num[::-1]       # 숫자를 거꾸로 배열한다.
    ret = ''
    for i,c in enumerate(num):      # enumerate하면 인덱스(i) + 객체(c)가 리턴됨
        i += 1                      # i는 추출 위치
        if i != len(num) and i%3 == 0:        # 추출위치가 num의 마지막이 아니고 3의 배수이면 
            ret += (c+',')     # 추출 요소 뒤에 콤마를 더한 값을 ret에 추가,,, c가 이해가 안된다
        else:  
            ret += c           # 나머지는 그냥 추가
    ret = ret[::-1]
    print(ret)
else:
    print('입력한 내용 [%s]:숫자가 아닙니다.'%num)
        

#%% 162 문자열의 각 문자를 그 다음 문자로 변경하기
text = input('문장을 입력하세요:')

ret = ''
for i in range(len(text)):
    if i != len(text)-1:    # 마지막글자는
        ret += text[i+1]
    else:
        ret += text[0]      # 맨 앞에 오도록
        
print(ret)

#%% 163 URL에서 호스트 도메인 추출하기
url = 'http://news.hankyung.com/article/2019031277366?nv=3&utm_source=naver&utm_medium=naver_newsstandcast&utm_campaign=newsstandcast_naver_all'

tmp = url.split('/')
domain = tmp[2] # 3번째 위치
print(domain)

#%% 164 URL에서 쿼리 문자열 추출하기

tmp = url.split('?') # url을 ?로 구분한 문자열이 요소인 리스트
queries = tmp[1].split('&')
for query in queries :
    print(query)
    
#%% 165 스택 구현하기 (append,pop)
# 리스트를 이용해 스택을 구현
# 스택은 데이터를 임시로 저장하는 공간
# 스택은 나중에 저장된 것이 먼저 추출되는 형식으로 동작함
    
mystack = []

def putdata(data):
    global mystack
    mystack.append(data)
    
def popdata():
    global mystack
    if len(mystack) == 0:
        return None
    return mystack.pop()

putdata('데이터1')
putdata([3,4,5,6])
putdata(12345)

print('<스택상태>:',end='');print(mystack)

ret = popdata()
while ret != None :
    print('스택에서 데이터 추출:',end='');print(ret)
    print('<스택상태>:',end='');print(mystack)
    ret = popdata()



##%% 180


















