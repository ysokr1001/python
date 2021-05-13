#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

data = [[2, 0, 81], [4, 4, 93], [6, 2, 91], [8, 3, 97]]
x1 = [x_row1[0] for x_row1 in data]
x2 = [x_row2[1] for x_row2 in data]
y_data = [y_row[2] for y_row in data]

a1 = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed = 0))
b = tf.Variable(tf.random_uniform([1], 0, 100, dtype=tf.float64, seed = 0))
a2 = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed = 0))

y = a1* x1 + a2 * x2 + b

rmse = tf.sqrt(tf.reduce_mean(tf.square(y-y_data)))

learning_rate = 0.1

gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(2001):
        sess.run(gradient_decent)
        if step % 100 == 0:
             print("Epoch: %.f, RMSE = %.04f, 기울기 a1 = %.4f, 기울기 a2 = %.4f, y절편 b = %.4f"%(step, sess.run(rmse),sess.run(a1),sess.run(a2), sess.run(b)))
    


# In[ ]:


actuality = [81, 93, 91, 97]
# pre1 = [80.2, 91.3, 89.5, 94.1]
# pre2 = [83.6, 88.2, 92.8, 97.4]

pre1 = [[2, 0, 81], [4, 4, 93], [6, 2, 91], [8, 3, 97]]
pre2 = [[2, 81], [4, 93], [6, 91], [8, 97]]

x1 = [x_row1[0] for x_row1 in data]
x2 = [x_row2[1] for x_row2 in data]
y_data = [y_row[2] for y_row in data]

m_a1 = 1.2301
m_a2 = 2.1633
m_b = 77.8117
m_result_y = []
for i in range(4):
    m_result_y.append(m_a1*x1[i]+m_a2*x2[i]+m_b)
print(m_result_y)

m_avr = sum(m_result_y)/4
print("다중선형회귀의 점수 평균 : " , m_avr)

m_diff_y = []
for i in range(4):
    m_diff_y.append(abs(y_data[i] - m_result_y[i]))
avr_d1 = sum(m_diff_y)/4
print("다중선형회귀의 오차 평균 : " , avr_d1)

s_a1 = 2.3
s_b = 79
s_result_y = []
for i in range(4):
    s_result_y.append(s_a1*x1[i]+s_b)
print(s_result_y)
s_avr2 = sum(s_result_y)/4
print("단순 선형회쉬의 점숨 평균: " ,s_avr2)

s_diff_y = []
for i in range(4):
    s_diff_y.append(abs(y_data[i] - s_result_y[i]))
avr_d2 = sum(s_diff_y)/4
print(avr_d2)
print("단순 선형회쉬의 오차 평균: " ,avr_d2)


# In[ ]:


#다시 해보기 
import numpy as np

data = [[2, 0, 81], [4, 4, 93], [6, 2, 91], [8, 3, 97]]
x1 = np.array([x_row1[0] for x_row1 in data], dtype = 'f')
x2 = np.array([x_row2[1] for x_row2 in data], dtype = 'f')
y_data = np.array([y_row[2] for y_row in data], dtype = 'f')

m_a1 = 1.2301
m_a2 = 2.1633
m_b = 77.8117
m_y2 = m_a1 * x1 + m_a2 * x2 + m_b
print("다중 선형회귀의 점수 평균 :", m_y2.mean())
# m_diff_y = abs(y - m_y2)
# print("다중 선형회귀의 오차 평균 : " , m_diff_y.mean())

s_a1 = 2.3
s_b = 79
s_y1 = s_a1 * x1 + s_b
print("단순 선형회귀의 점수 평균: ", s_y1.mean())
s_diff_y = abs(y - s_y1)
print("단순 선형회귀의 오차 평균: ", s_diff_y.mean())


# In[ ]:


import tensorflow as tf

data = [[2, 0, 81], [4, 4, 93], [6, 2, 91], [8, 3, 97]]
x1 = [x_row1[0] for x_row1 in data]
x2 = [x_row2[1] for x_row2 in data]
y_data = [y_row[2] for y_row in data]

a1 = tf.Variable(tf.random.uniform([1], 0, 10, dtype=tf.float64, seed = 0))
b = tf.Variable(tf.random.uniform([1], 0, 100, dtype=tf.float64, seed = 0))
a2 = tf.Variable(tf.random.uniform([1], 0, 10, dtype=tf.float64, seed = 0))

def hypothesis(a1, b, a2):
    return a1* x1 + a2 * x2 + b

def costFunc():
    return tf.sqrt(tf.reduce_mean(tf.square(hypothesis(a1,b, a2) - y_data)))

def cost(a1, b, a2):
    return tf.sqrt(tf.reduce_mean(tf.square(hypothesis(a1,b, a2) - y_data)))
    
opt = tf.keras.optimizers.SGD(learning_rate = 0.1)
for i in range(2001):
    opt.minimize(costFunc, var_list = [a1, b, a2])
    if i % 100 == 0:
        print(i, f'{cost(a1, b, a2)}, {a1.numpy()}, {b.numpy()}, {a1.numpy()}')


# In[ ]:


import tensorflow as tf
from datetime import datetime

data = [[2, 0, 81], [4, 4, 93], [6, 2, 91], [8, 3, 97]]
x1 = [x_row1[0] for x_row1 in data]
x2 = [x_row2[1] for x_row2 in data]
y_data = [y_row[2] for y_row in data]

a1 = tf.Variable(tf.random.uniform([1], 0, 10, dtype=tf.float64, seed = 0))
b = tf.Variable(tf.random.uniform([1], 0, 100, dtype=tf.float64, seed = 0))
a2 = tf.Variable(tf.random.uniform([1], 0, 10, dtype=tf.float64, seed = 0))

def hypothesis(a1, b, a2):
    return a1* x1 + a2 * x2 + b

@tf.function()
def costFunc():
    return tf.sqrt(tf.reduce_mean(tf.square(hypothesis(a1,b, a2) - y_data)))

def cost(a1, b, a2):
    return tf.sqrt(tf.reduce_mean(tf.square(hypothesis(a1,b, a2) - y_data)))
    

stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
logdir = 'logs/mylogs/%s'%stamp
writer = tf.summary.create_file_writer(logdir)
tf.summary.trace_on(graph=True, profiler=True)
costFunc()
with writer.as_default():
    tf.summary.trace_export(name='graph_t1', step=0, profiler_outdir=logdir)
    
opt = tf.keras.optimizers.SGD(learning_rate = 0.1)
for i in range(2001):
    opt.minimize(costFunc, var_list = [a1, b, a2])
    if i % 100 == 0:
        print(i, f'{cost(a1, b, a2)}, {a1.numpy()}, {b.numpy()}, {a1.numpy()}')


# In[ ]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import numpy as np

data = np.loadtxt("C:/Users/ysokr/Downloads/Blood_fat.csv", delimiter =",")

x1 = [x_row1[0] for x_row1 in data]
x2 = [x_row2[1] for x_row2 in data]
y_data = [y_row[2] for y_row in data]


a1 = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed = 0))
b = tf.Variable(tf.random_uniform([1], 0, 100, dtype=tf.float64, seed = 0))
a2 = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed = 0))

y = a1* x1 + a2 * x2 + b

rmse = tf.sqrt(tf.reduce_mean(tf.square(y-y_data)))

learning_rate = 0.001

gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for step in range(2001):
#         sess.run(gradient_decent)
#         if step % 100 == 0:
#              print("Epoch: %.f, RMSE = %.04f, 기울기 a1 = %.4f, 기울기 a2 = %.4f, y절편 b = %.4f"%(step, sess.run(rmse),sess.run(a1),sess.run(a2), sess.run(b)))


epoch_step = 2001
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(epoch_step):
        sess.run(gradient_decent)
        if step % 100 == 0:
            print("Epoch: %.f, RMSE = %.04f, 기울기 a1 = %.4f, 기울기 a2 = %.4f, y절편 b = %.4f"%(step, sess.run(rmse), sess.run(a1), sess.run(a2), sess.run(b)))
        if step == epoch_step-1:
            da1 = sess.run(a1)
            da2 = sess.run(a2)
            db = sess.run(b)
            print(da1)
            print(da2)
            print(db)
            print(type(da1))
            
calc_y = []
for i in range(25):
    new_y = (da1*x1[i])+(da2*x2[i])+db
    calc_y.append(new_y)
    print(new_y)
    
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(111, projection ='3d')
ax.scatter(x1, x2, calc_y)
ax.set_xlabel('Weight')
ax.set_ylabel('Age')
ax.set_zlabel('Blood fat')
ax.view_init(15, 15)
plt.show()


# In[10]:


import tensorflow as tf

import numpy as np

data = np.loadtxt("C:/Users/ysokr/Downloads/Blood_fat.csv", delimiter =",")

x1 = [x_row1[0] for x_row1 in data]
x2 = [x_row2[1] for x_row2 in data]
y_data = [y_row[2] for y_row in data]


a1 = tf.Variable(tf.random.uniform([1], 0, 10, dtype=tf.float64, seed = 0))
b = tf.Variable(tf.random.uniform([1], 0, 100, dtype=tf.float64, seed = 0))
a2 = tf.Variable(tf.random.uniform([1], 0, 10, dtype=tf.float64, seed = 0))


def hypothesis(a1, b, a2):
    return a1* x1 + a2 * x2 + b

def costFunc():
    return tf.sqrt(tf.reduce_mean(tf.square(hypothesis(a1,b, a2) - y_data)))

def cost(a1, b, a2):
    return tf.sqrt(tf.reduce_mean(tf.square(hypothesis(a1,b, a2) - y_data)))
    
opt = tf.keras.optimizers.SGD(learning_rate = 0.001)
for i in range(2001):
    opt.minimize(costFunc, var_list = [a1, b, a2])
    if i % 100 == 0:
        print(i, f'{cost(a1, b, a2)}, {a1.numpy()}, {b.numpy()}, {a1.numpy()}')
#     if i== 2001-1:
#         da1 = val_list[0]
#         da2 = val_list[2]
#         db = val_list[1]
#         print(da1)
#         print(da2)
#         print(db)
#         print(type(da1))
da1 = a1.numpy()
da2 = a2.numpy()
db = b.numpy()
for i in range(25):
    print((da1*x1[i])+da2*x2[i]+db)

            


# In[ ]:




