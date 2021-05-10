#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

x = tf.Variable(5, dtype=tf.int32)
print(x)
z=tf.assign(x,7)
# tf.global_variables_initializer()
sess=tf.Session()
sess.run(z)
y=sess.run(x)
print(y)
sess.close()


# In[ ]:


#왜 안되징 해보기
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

x=tf.Variable(tf.zeros((2,2)), dtype=tf.float32)
print(x)
y = tf.Variable([[1,2],[3,4]],dtype=tf.float32)
x = tf.assign(x.y)
sess=tf.Session()
z=tf.global_variables_initializer()
sess.run(z)
y=sess.run(x)
sess.close()

print(y)


# In[ ]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

mat_img = [1,2,3,4,5]
label = [10,20, 30, 40, 50]

ph_img = tf.placeholder(dtype=tf.float32)
ph_lb=tf.placeholder(dtype=tf.float32)

ret_tensor=ph_img + ph_lb

sess=tf.Session()
y = sess.run(ret_tensor, feed_dict = {ph_img:mat_img, ph_lb:label})
sess.close()
print(y)


# In[ ]:


import tensorflow as tf
x = tf.constant([[1.0,2.0,3.0]])
w=tf.constant([[2.0], [2.0], [2.0]])
y=tf.matmul(x,w)
print(y)
print(y.shape)
print(y.dtype)
print("y data = {}".format(y))


# In[ ]:


node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print(node1.numpy(), node2.numpy())
print(node3.numpy())
'''
tf.print(node1, node2)
tf.print(node3)
'''


# In[ ]:





# In[ ]:


import tensorflow.compat.v1 as tf
tf.compat.v1.disable_v2_behavior()

data = [[1, 0.2], [2, 0.3], [3, 0.5], [4, 0.6], [6, 0.95], [7, 1.1], [8, 1.5]]
x_data=[x_data[0] for x_data in data]
y_data=[y_data[1] for y_data in data]

learning_rate = 0.005
a = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float32, seed=0))
b = tf.Variable(tf.random_uniform([1], 0, 100, dtype = tf.float32, seed = 0))

y = a * x_data + b
print(y)

rmse = tf.sqrt(tf.reduce_mean(tf.square(y - y_data)))
print(rmse)


gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(11001):
        sess.run(gradient_decent)
        print("Epoch: %.f, RMSE = %.04f, a 기울기 a = %.4f, y절편 b = %.4f"%(step, sess.run(rmse),sess.run(a),sess.run(b)))


# In[ ]:


import tensorflow.compat.v1 as tf
tf.compat.v1.disable_v2_behavior()

data=[[100,20],[150,24],[300,36],[400,47],[130,22],[240,32],[350,47],[200,42],[100,21],[110,21],[190,30], [120,25],[130,18],[270,38],[255,28]]

x_data=[x_data[0] for x_data in data]
y_data=[y_data[1] for y_data in data]

learning_rate = 0.0001

a = tf.Variable(tf.random_uniform([1], 0, 1, dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_uniform([1], 0, 15, dtype = tf.float64, seed = 0))

y = a * x_data + b

rmse = tf.sqrt(tf.reduce_mean(tf.square(y - y_data)))


gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(1000001):
        sess.run(gradient_decent)
        if step % 10000 ==0:
            print("Epoch: %.f, RMSE = %.04f, a 기울기 a = %.4f, y절편 b = %.4f"%(step, sess.run(rmse),sess.run(a),sess.run(b)))


# In[3]:


import matplotlib as mpl
import matplotlib.pyplot as plt


# In[4]:


get_ipython().run_line_magic('matplotlib.inline', '')


# In[5]:


plt.plot([1, 4, 9, 16, 8])


# In[ ]:


#

