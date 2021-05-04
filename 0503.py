#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


ar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ar)
ar


# In[4]:


print(ar)
type(ar)


# In[5]:


data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data = list(range(10))
print(data)
print(type(data))


# In[6]:


answer = []
for di in data:
    answer.append(2*di)
print(answer)


# In[7]:


x = np.array(data)
print(x)


# In[8]:


print(x*2)


# In[9]:


print(2 * data)


# In[10]:


a = np.array([1, 2, 3])
b = np.array([10, 20, 30])


# In[11]:


2 * a + b


# In[12]:


list_a = [1, 2, 3]
list_b = [10, 20, 30]
2 * list_a + list_b


# In[14]:


print(a)
a == 2


# In[15]:


print(b)
print(b>10)


# In[16]:


print((a==2) & (b>10))


# In[17]:


print((a==2)|(b>10))


# In[19]:


c = np.array([[0, 1, 2], [3, 4, 5]])
print(c)
c


# In[20]:


len(c)


# In[21]:


print(c[0])
len(c[0])


# In[22]:


np.array([[10, 20, 30, 40],[50, 60, 70,80]])


# In[26]:


d = np.array([[[1,2,3,4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]],
             [[11, 12, 13, 14],
             [15, 16, 17, 18],
             [19,20, 21, 22]]])
print(d)


# In[27]:


d1 = [[1,2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]
d2 = [[11, 12, 13, 14],
     [15, 16, 17, 18],
     [19, 20, 21, 22]]
d = np.array([d1, d2])
print(d)


# In[28]:


len(d), len(d[0]), len(d[0][0])


# In[29]:


print(a)
print(a.ndim)
print(a.shape)


# In[30]:


print(c)
print(c.ndim)
print(c.shape)


# In[32]:


#배열의 인덱싱
a = np.array([0, 1, 2, 3, 4])


# In[33]:


print(a[2])


# In[34]:


print(a[-1])


# In[36]:


a = np.array([[0,1,2],[3,4,5]])
print(a)


# In[38]:


print(a[0, 0])


# In[39]:


print(a[0, 1])
print(a[-1, -1])


# In[44]:


a = np.array([[0, 1, 2, 3], [4, 5, 6,7]])
print(a)


# In[43]:


print(a[0, :]) #첫번째 행 전체
print(a[:, 1]) #두번째 열 전체
print(a[1, 1:]) #두번째 행의 두번째 열부터 끝열까지
print(a[:2, :2])


# In[55]:


#연습문제 7값 출력하기
m = np.array([[0, 1, 2, 3, 4],
     [5, 6, 7, 8, 9],
     [10, 11, 12, 13, 14]])
print(m)
print(m[1, 2])


# In[56]:


print(m[2, 4], m[-1, -1])


# In[57]:


print(m[1, 1:3])
print(m[:2, -2:])


# In[63]:


import numpy as np
x =[2, 4, 6, 8]
y = [81, 93, 91, 97]

#x와y의 평균값
mx = np.mean(x)
my = np.mean(y)
print("x의 평균값:", mx)
print("y의 평균값:", my)

#기울기 공식의 분모
divisor = sum([(mx-i)**2 for i in x])

def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i]-my)
    return d
# dividend = top(x, mx, y, my)
dividend = sum([(x[i] - mx)*(y[i] - my) for i in range(len(x)) ])

print("분모:", divisor)
print("분자:",dividend)

#기울기와y절편구하기
a= dividend/divisor
b = my - (mx*a) 

#출력으로 확인
print("기울기 a=", a)
print("y절편 b =", b)


# In[66]:


x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [0.2, 0.3, 0.5, 0.6, 0.9, 0.95, 1.1, 1.5]

#물고기들 평균크기
mx = np.mean(x)
my = np.mean(y)
print("x의 평균주수:", mx)
print("y의 평균크기:", my)

divisor = sum([(mx-i)**2 for i in x])
dividend = sum([(x[i] - mx)*(y[i] - my) for i in range(len(x)) ])

print("분모:", divisor)
print("분자:",dividend)

a= dividend/divisor
b = (mx*a) - my

print("기울기 a=", a)
print("y절편 b =", b)


# In[205]:


x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [0.2, 0.3, 0.5, 0.6, 0.9, 0.95, 1.1, 1.5]

# #물고기들 평균크기
mx = np.mean(x)
my = np.mean(y)
# print("x의 평균주수:", mx)
# print("y의 평균크기:", my)

divisor = sum([(mx-i)**2 for i in x])
dividend = sum([(x[i] - mx)*(y[i] - my) for i in range(len(x)) ])

# print("분모:", divisor)
# print("분자:",dividend)

a= dividend/divisor
b = my - (mx*a)

# print("기울기 a=", a)
# print("y절편 b =", b)

# y = (200*0.175) + 0.033 #8주차 1.432  #15주차 2.685cm # 22주차 3.882 #77주차 13.508 #200주차 35.033
# print(y)

# xx = 5
# z = (xx * a) + b
# print("5주차 크기의 예측값: %.3f"%z)


# print("실제 크기와 예상크기의 차이:%.3f"%zz)

#위의 식으로 했을 때, 15주, 22주, 77주, 200주 예상크기
# x1 = [15, 22, 77, 200]
# x2 = []
# for i in x1:
#     z1 = (i * a) + b
#     if z1 < 30:
#         x2.append(z1)
# np.round(x2, 3)

zz = z-y[4]

def size(g):
    size_prediction = (g * a) + b
    return "30이상입니다" if size_prediction > 30 else round(size_prediction, 3)

print("5주차:", size(5), "cm"+" , "+"실제크기와 예상크기의 차이는:%.3f"%zz)
print("15주차:" ,size(15), "cm")
print("22주차:" ,size(22), "cm")
print("77주차:" ,size(77), "cm")
print("22주차:" ,size(200), "cm")


# In[207]:


x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [0.2, 0.3, 0.5, 0.6, 0.9, 0.95, 1.1, 1.5]

mx = np.mean(x)
my = np.mean(y)


divisor = sum([(mx-i)**2 for i in x])
dividend = sum([(x[i] - mx)*(y[i] - my) for i in range(len(x)) ])


a= dividend/divisor
b =(mx*a) - my

zz = z-y[4]

def size(g):
    size_prediction = (g * a) + b
    return "30이상입니다" if size_prediction > 30 else round(size_prediction, 3)

print("5주차:", size(5), "cm"+" , "+"실제크기와 예상크기의 차이는:%.3f"%zz)
print("15주차:" ,size(15), "cm")
print("22주차:" ,size(22), "cm")
print("77주차:" ,size(77), "cm")
print("22주차:" ,size(200), "cm")


# In[212]:


import numpy as np

maxsize = 30
xData = [1, 2, 3, 4, 5, 6, 7, 8]
yData = [0.2, 0.3, 0.5, 0.6, 0.9, 0.95, 1.1, 1.5]

xAvg = np.mean(xData)
yAvg = np.mean(yData)

print("x 평균", xAvg)
print("y 평균", yAvg)

divisor = sum([(i - xAvg) ** 2 for i in xData])

dividend = 0
for i in range(len(xData)):
    dividend += (xData[i] - xAvg) * (yData[i] - yAvg)
    
a = dividend/ divisor
b = yAvg - (xAvg * a)

print("분자", divisor)
print("분모", dividend)
print("기울기", a)
print("y절편", b)

def sizeof(x):
    v = a * x + b
    return maxsize if v > maxsize else round(v, 3)

print("15주 후의 크기 : ", sizeof(15), "cm")
print("25주 후의 크기 : ", sizeof(25), "cm")
print("77주 후의 크기 : ", sizeof(77), "cm")


# In[ ]:




