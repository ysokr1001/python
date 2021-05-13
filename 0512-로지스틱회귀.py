#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

data = [[2,0], [4,0], [6,0], [8,1], [10,1], [12,1], [14,1]]
x_data = [x_row[0] for x_row in data]
y_data = [y_row[1] for y_row in data]

a = tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))

y = 1/(1 + np.e**-(a*x_data+b))
loss = -tf.reduce_mean(np.array(y_data)* tf.log(y) + (1 - np.array(y_data)) * tf.log(1-y))

learning_rate = 0.5

gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(60001):
        sess.run(gradient_decent)
        if i % 6000 == 0:
            print("Epoch: %.f, loss = %.4f, 기울기a = %.4f, y절편 = %.4f"%(i, sess.run(loss), sess.run(a), sess.run(b)))


# In[ ]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

data = [[2,0], [4,0], [6,0], [8,1], [10,1], [12,1], [14,1]]
x_data = [x_row[0] for x_row in data]
y_data = [y_row[1] for y_row in data]

a = tf.Variable(tf.random.normal([1], dtype=tf.float64, seed=0))
b = tf.Variable(tf.random.normal([1], dtype=tf.float64, seed=0))

y = 1/(1 + np.e**-(a*x_data+b))
loss = -tf.reduce_mean(np.array(y_data)* tf.log(y) + (1 - np.array(y_data)) * tf.log(1-y))

learning_rate = 0.5

gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(60001):
        sess.run(gradient_decent)
        if i % 6000 == 0:
            print("Epoch: %.f, loss = %.4f, 기울기a = %.4f, y절편 = %.4f"%(i, sess.run(loss), sess.run(a), sess.run(b)))
#         if i == 60000:
#             new_x_data = 5
#             y_test = 1/(1 + np.e**-((a*new_x_data)+b))
#             print(sess.run(y_test))
#             print(sess.run(y_test[0]))
            
#             new_x_data = 7
#             y_test = 1/(1 + np.e**-((a*new_x_data)+b))
#             print(sess.run(y_test))
#             print(sess.run(y_test[0]))
            
#             new_x_data = 13
#             y_test = 1/(1 + np.e**-((a*new_x_data)+b))
#             print(sess.run(y_test))
#             print(sess.run(y_test[0]))
#             print(y_test)
#         if i % 6000:    
#             x_data1 = [5, 7, 13]

#             for i in x_data1:
#                 y1 = 1/(1 + np.e**-(a*x_data1+b))
#                 print(sess.run(y1))
#                 print(sess.run(y1[i]), end=' ')
    calc_a = sess.run(a)
    calc_b = sess.run(b)
    
def NewDataCalc(new_x_data):
    return 1/(1 + np.e**-(a*new_x_data+b))
print(NewDataCalc(5))
print(NewDataCalc(7))
print(NewDataCalc(13))


# In[ ]:


import tensorflow as tf

import numpy as np

data = [[2,0], [4,0], [6,0], [8,1], [10,1], [12,1], [14,1]]
x_data = [x_row[0] for x_row in data]
y_data = [y_row[1] for y_row in data]

a = tf.Variable(tf.random.normal([1], dtype=tf.float64, seed=0))
b = tf.Variable(tf.random.normal([1], dtype=tf.float64, seed=0))


def hypothesis(a, b):
    return 1/(1 + np.e**-(a*x_data+b))
def cost(a1, b):
    return -tf.reduce_mean(np.array(y_data) * tf.math.log(hypothesis(a, b)) + (1 - np.array(y_data))*tf.math.log(1-hypothesis(a,b)))
def costFunc():
    return -tf.reduce_mean(np.array(y_data) * tf.math.log(hypothesis(a, b)) + (1 - np.array(y_data))*tf.math.log(1-hypothesis(a,b)))

opt = tf.keras.optimizers.SGD(learning_rate = 0.5)
for i in range(1001):
    opt.minimize(costFunc, var_list = [a, b])
    if i % 100 == 0:
        print(i, f'{cost(a, b)}, {a.numpy()}, {b.numpy()}')       
    if i == 1000:
        new_x_data = 5
        y_test = 1/(1 + np.e**-((a*new_x_data)+b))
        print(y_test.numpy())
        print('%.40f'%float(y_test.numpy()))
            
        new_x_data = 7
        y_test = 1/(1 + np.e**-((a*new_x_data)+b))
        print(y_test.numpy())
        print("%.40f"%float(y_test.numpy()))
            
        new_x_data = 13
        y_test = 1/(1 + np.e**-((a*new_x_data)+b))
        print(y_test.numpy())
        print("%.40f"%float(y_test.numpy()))


# In[ ]:


a = np.arange(12)
print(a)

b= a.reshape(3,4)
print(b)

# a.reshape(3, -1)


# a.reshape(2, 2, -1)

# a.reshape(2, -1, 2)

a.flatten()

a.ravel()


# In[ ]:


x = np.arange(5)
x

# x.reshape(1,5)

# x.reshape(5, 1)

x[:, np.newaxis]


# In[ ]:


np.arange(3)


# In[ ]:


np.arange(3.0)


# In[ ]:


np.arange(3,7)


# In[ ]:


np.arange(3, 7, 2)


# In[ ]:


import numpy as np
a = [1, 2, 3, 4, 5]
b = np.array(a)
c = np.array([1, 3, 5])
print(a)
print(b)
print(c)


# In[1]:


import numpy as np
a = [1, 2, 3, 4, 5]
b = np.array(a)
c = np.array([1, 3, 5])
print(a*2)
print(b*2)
print(c+3)

#numpy는 벡터연산이 가능하므로 


# In[3]:


import numpy as np
a = np.ones((2,2), dtype=int)
b = [1, 2, 3, 4, 5]
c = np.ones_like(b, dtype = int)
print(a)
print(b)
print(c)


# In[5]:


a = np.zeros((2,2), dtype=int)
b = [1, 2, 3, 4, 5]
c = np.zeros_like(b, dtype = int)
print(a)
print(b)
print(c)


# In[6]:


a = np.empty((2,2), dtype=int)
b = [1, 2, 3, 4, 5]
c = np.empty_like(b, dtype = int)
print(a)
print(b)
print(c)


# In[ ]:




