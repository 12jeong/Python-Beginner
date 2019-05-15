import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 노트북 안에 그래프 그리기?
%matplotlib inline
# ggplot 스타일 사용
plt.style.use('ggplot')
# 한글 코드에서 마이너스가 깨지는 문제 방지
mpl.rcParams['axes.unicode_minus']=False

# count - 자전거 대여량 데이터
train = pd.read_csv("C:/Users/MYCOM/Downloads/train.csv",parse_dates=["datetime"])
train.shape # 차원
train.info() # 정보
train.head() # 상위 5개  

train.temp.describe() # temp 변수 summary 

# null 시각화
train.isnull().sum()
import missingno as msno
msno.matrix(train, figsize=(12,5))

# 새로운 변수 지정
train["year"] = train["datetime"].dt.year       # int로 들어가네?
train["month"] = train["datetime"].dt.month
train["day"] = train["datetime"].dt.day
train["hour"] = train["datetime"].dt.hour
train["minute"] = train["datetime"].dt.minute
train["second"] = train["datetime"].dt.second
train.shape


# 막대그래프
figure, ((ax1,ax2,ax3), (ax4,ax5,ax6)) = plt.subplots(nrows=2,ncols=3)
figure.set_size_inches(18,8)
sns.barplot(data=train, x="year", y="count", ax=ax1)
sns.barplot(data=train, x="month", y="count", ax=ax2)
sns.barplot(data=train, x="day", y="count", ax=ax3)
sns.barplot(data=train, x="hour", y="count", ax=ax4)
sns.barplot(data=train, x="minute", y="count", ax=ax5)
sns.barplot(data=train, x="second", y="count", ax=ax6)
ax1.set(ylabel="count", title="연도별 대여량")
ax2.set(xlabel="month", title="월별 대여량")
ax3.set(xlabel="day", title="일별 대여량")
ax4.set(xlabel="hour", title="시간별 대여량")

# 박스플롯
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_size_inches(12,10)
sns.boxplot(data=train,y="count",orient="v",ax=axes[0][0])
sns.boxplot(data=train,y="count",x="season",orient="v",ax=axes[0][1])
sns.boxplot(data=train,y="count",x="hour",orient="v",ax=axes[1][0])
sns.boxplot(data=train,y="count",x="workingday",orient="v",ax=axes[1][1])
axes[0][0].set(ylabel="Count",title="대여량")
axes[0][0].set(xlabel="Season",title="계절별 대여량")
axes[0][0].set(xlabel="Hour Of The Day",title="시간별 대여량")
axes[0][0].set(xlabel="Working Day",title="근무일 여부에 따른 대여량")

train["dayofweek"] = train["datetime"].dt.dayofweek
train["dayofweek"].value_counts()

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=5)
fig.set_size_inches(18,25)
sns.pointplot(data=train, x="hour", y="count", ax=ax1)
# workingday에 따라 시계열 count가 다른지 보자
sns.pointplot(data=train, x="hour", y="count", hue="workingday", ax=ax2)
sns.pointplot(data=train, x="hour", y="count", hue="dayofweek", ax=ax3)
sns.pointplot(data=train, x="hour", y="count", hue="weather", ax=ax4)
sns.pointplot(data=train, x="hour", y="count", hue="season", ax=ax5)

# 히트맵? - 상관관계
corrMatt = train[["temp","atemp","casual","registered","humidity","windspeed","count"]]
corrMatt = corrMatt.corr()
print(corrMatt)

mask = np.array(corrMatt)
mask[np.tril_indices_from(mask)] = False

fig,ax = plt.subplots()
fig.set_size_inches(20,10)
sns.heatmap(corrMatt, mask=mask, vmax=.8, square=True, annot=True)

# 산점도
fig, (ax1,ax2,ax3) = plt.subplots(ncols=3)
fig.set_size_inches(12,5)
sns.regplot(x="temp",y="count",data=train,ax=ax1)
sns.regplot(x="windspeed",y="count",data=train,ax=ax2)
sns.regplot(x="humidity",y="count",data=train,ax=ax3)

# 년-월 붙여서 새 변수 만들기 
def concatenate_year_month(datetime) :
    return "{0}-{1}".format(datetime.year, datetime.month)

train["year_month"] = train["datetime"].apply(concatenate_year_month)
print(train.shape)
train[["datetime","year_month"]].head

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
fig.set_size_inches(18, 4)
sns.barplot(data=train, x="year", y="count", ax=ax1)
sns.barplot(data=train, x="month", y="count", ax=ax2)

fig, ax3 = plt.subplots(nrows=1, ncols=1)
fig.set_size_inches(18, 4)
sns.barplot(data=train, x="year_month", y="count", ax=ax3)

# 아웃라이어 제거하기
trainWithoutOutliers = train[np.abs(train["count"]-train["count"].mean()) <= 
                             (3*train["count"].std())]
print(train.shape)
print(trainWithoutOutliers.shape)

# count값의 데이터 분포도를 파악

figure, axes = plt.subplots(ncols=2, nrows=2)
figure.set_size_inches(12, 10)

sns.distplot(train["count"], ax=axes[0][0])
stats.probplot(train["count"], dist='norm', fit=True, plot=axes[0][1])
sns.distplot(np.log(trainWithoutOutliers["count"]), ax=axes[1][0])
stats.probplot(np.log1p(trainWithoutOutliers["count"]), dist='norm', fit=True, plot=axes[1][1])

