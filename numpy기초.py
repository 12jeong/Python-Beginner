# 파이썬 넘파이 23분에 끝내기 
# https://www.youtube.com/watch?v=OIV14ItViP0

import numpy as np

a = np.arange(21)
a # 0에서 20까지 21개

b=a.reshape(3,7)
b # 3X7
b.shape (3,7)

a.ndim # 1차원
b.ndim # 2차원

a.dtype.name # int
type(a) # darray

c = np.array([(1,2,3),(4,5.5,6)])
c # 5.5 때문에
c.dtype # float 이라고 뜸

d = np.array([(1,2,3),(4,5.5,6)], dtype=int) # type을 강제하면
d # 5 not 5.5

np.zeros((3,5)) # 3x5의 array를 만들어라 
np.full((3,3),7) # 7을 넣어라

np.array(1,20,2) # 1에서 20까지 2씩 띄어서 넣어라 (r의 seq(by))

np.linspace(1,10,11) # 시작=1, 끝=10, 11개 (r의 seq(length))

e = np.array([1,2,3,4])
f = np.arange(4)
f
e*f # 각 성분 곱해짐 
e-f # 각 성분 빼짐 
e*3 
e**3

g = np.arange(9) .reshape(3,3)
g

h = np.arange(9) .reshape(3,3) +1
h

g*h # 원소곱
g**2
g**h

g.dot(h) # 행렬곱 (R의 %*%)
np.dot(g,h) # 위와같음

g>3 # 행렬에서 3보다 큰 값 TRUE,FALSE

i = np.array([[[[1,2],[3,4]]]],dtype=np.float64)
i.dtype # int인데 float으로 강제
i.ndim # [] 괄호 4개 차원

#random
j = np.random.random((5,2)) # runiform을 (5x2)로 뽑는다
j

j.min()
j.max()
j.mean()
j.sum(axis=0) # |방향으로 sum
j.sum(axis=1) # ㅡ방향으로 sum

np.exp(j) 
np.sqrt(j) 
np.add(j,j) # j+j
np.sin(j)

# 요소추출
np.sin(j[0,0]) # 첫번째값 j[1,1]

j[3]
j[3:] # 3이후
j[:3] # 3까지... 0,1,2>3  헷갈리네
j
j[:3,:1] # 중요
j[:3,1] # 중요

j[0,1]
j[0,1] = 3.333 # 값 바꾸기
j
j[-1] # 마지막 열
j[-3] # 뒤에서 세번째 열
j[:-1] # 맨뒤 전까지
j[:-1,-2] # 여기서는 j[:-1,0] 과 같음

for i in j[1:3] :
    print(i)      # 첫번째, 두번째 1<= <3

def multiplier(x,y):
    return x*y

k=np.arange(5)
multiplier(k,k) # 0*0, 1*1, 2*2, 3*3, 4*4

def biggerThanZero(x):
    if x>0:
        return True
    else:
        return False

l = np.arange(100)-59
biggerThanZero(l.sum()) # l 다 더한값이 0보다 큰지 확인

m = np.arange(18).reshape(3,3,2)
m

m[1,2] # 1번(맨끝 괄호)의 2번
m[1,2,1] 
m[:,1,:] # 2,3, 8,9, 14,15
m[2,1,:]
m[2,...] # m[2,:,:]와 같다

for i in m :
    print(i)
    
for i in m.flat : # flat : 다 펼쳐
    print(i)
    
m.shape
n = m.reshape(2,9) # 차원이 안맞으면 error
n
n.T # transpose
n.T.shape (9,2)
n.shape (2,9)

# reshape vs resize
n.resize(3,6) # n = n.reshape 로 새로 지정하지 않고
n # 기존의 n을 바꿔버림
n.shape

n.reshape(6,-1) # 6만 지정해주면 나머지는 알아서

np.vstack((n,n)) # vertical로 쌓는다
np.stack((n,n)) # 차원 밖으로 따로 쌓아준다
np.stack((n,n), axis=1) # 축에 끼어서 쌓아주고
np.stack((n,n), axis=2) # 이건뭐지?

o = np.hstack((n,n)) # horizonal로 쌓는다
o

p,q,r = np.hsplit(o,3) # 3개로 쪼개자
p
q
r

s,t,u = np.hsplit(o,(2,4)) # 어디서 쪼갤지 지정
s # 0,1
t # 2,3
u # 4~

t==s # boolin
t is s
i is t

id(t)
id(q)

type(t)
t.dtype

u = np.arange(10)
u
v= [x*2 for x in u if x % 2 ==0] # 2의배수일시 u에 있는 원소들을 2로 곱해라 
v

import matplotlib.pyplot as plt
w = np.arange(0, 20*np.pi, 0.1) # 0 부터 20pi 까지
x = np.tan(w)

plt.plot(w,x)
plt.show()

y = np.arange(0, 20*np.pi, 0.1)
z_s = np.sin(y)
z_c = np.cos(y)
z_t = np.tan(y)/100

plt.plot(y, z_s)
plt.plot(y, z_c)
plt.plot(y, z_t)
plt.title("Test")
plt.legend(['sine','cosine','tangent'])
plt.show() # 이걸 해야 보여진다는데, spyder랑 jupyter 다른가?