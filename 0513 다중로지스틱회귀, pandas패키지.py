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

y = 1/(1+np.e**-(a * x_data + b))
loss = -tf.reduce_mean(np.array(y_data) * tf.log(y) + (1 - np.array(y_data)) * tf.log(1 - y))

learning_rate = 0.5

gradient_decent = tf.train.GradientDescentOptimizer(learning_rate). minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(60001):
        sess.run(gradient_decent)
        if i % 6000 == 0 :
            print("Epoch : %.f, loss = %.4f, 기울기a = %.4f, y절편 = %.4f"%(i, sess.run(loss), sess.run(a), sess.run(b)))


# In[ ]:


# 여러 입력 값을 가지는 로지스틱 회귀
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

seed = 0
np.random.seed(seed)
tf.set_random_seed(seed)
x_data = np.array([[2,3], [4,3], [6,4], [8,6], [10,7], [12,8], [14,9]])
y_data = np.array([0,0,0,1,1,1,1]).reshape(7, 1)

X = tf.placeholder(tf.float64, shape=[None,2])
Y = tf.placeholder(tf.float64, shape = [None,1])

a = tf.Variable(tf.random_uniform([2,1], dtype=tf.float64))
b = tf.Variable(tf.random_uniform([1], dtype=tf.float64))

y = tf.sigmoid(tf.matmul(X,a) +b)

loss = -tf.reduce_mean(Y * tf.log(y) + (1-Y) * tf.log(1-y))

learning_rate = 0.1

gradient_decent = tf.train.GradientDescentOptimizer(learning_rate). minimize(loss)

predicted = tf.cast(y > 0.5, dtype=tf.float64)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype = tf.float64))

with tf. Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for i in range(3001):
        a_, b_, loss_, _ = sess.run([a, b, loss, gradient_decent], feed_dict = {X: x_data, Y: y_data})
        if (i + 1) % 300 == 0:
            print("step=%d, a1=%.4f, a2=%.4f, b=%.4f, loss=%.4f"%(i+1, a_[0], a_[1], b_, loss_))

    print("predicted=", sess.run(predicted, feed_dict={X:x_data}))

    p_val, h_val = sess.run([predicted, y], feed_dict={X:[[1,5], [10,5], [4,5]]}) 
    print("check predivted=",p_val)
    print("check hypothesis=", h_val)

    h, c, a = sess.run([y, predicted, accuracy], feed_dict = {X:x_data, Y:y_data})
    print("|nHypothesis: ", h, "|nCorrect (Y):", c, "|nAccuracy: ", a)


# In[ ]:


#위 코드 2.0으로 짜기
#이거 해보기
import tensorflow as tf
import numpy as np

seed = 0
np.random.seed(seed)
tf.random.set_seed(seed)

x_data = np.array([[2,3], [4,3], [6,4], [8,6], [10,7], [12,8], [14,9]], dtype=np.float32)
y_data = np.array([0,0,0,1,1,1,1]).reshape(7, 1)

W = tf.Variable(tf.random.uniform([2,1], dtype=tf.float64)) #shape = (2,1) -> 들어오는 값은 2개, 나가는 값은 1개
b = tf.Variable(tf.random.uniform([1], dtype=tf.float64)) #shape = (1,)

def hypothesis(W,b):
    return tf.sigmoid(tf.matmul(x_data,W) +b)

def costFunc():
    return -tf.reduce_mean(y_data * tf.math.log(hypothesis(W,b)) + (1 - y_data) * tf.math.log(1-hypothesis(W,b)))

def cost(W,b):
    return -tf.reduce_mean(y_data * tf.math.log(hypothesis(W,b)) + (1 - y_data) * tf.math.log(1-hypothesis(W,b)))


opt = tf.keras.optimizers.SGD(learning_rate = 0.1)
for i in range(3001):
    opt.minimize(costFunc, val_list=[W,b])
    if i % 100 == 0:
        print(f'epochs={i}, cost={cost(W,b)}, W1={W.numpy()[0,0]}, W2={W.numpy()[1, 0]}, b = {b.numpy()}')


print("=================")
print("W=", W.numpy())
print("b=", b.numpy())
print("sigmoid=", hypothesis(W,b).numpy())
print()
print("Accuravy=%.4f"%(sum((y_data==(hypothesis(W,b).numpy()>0.5)).flatten())/len(y_data)))


# In[ ]:



#해보기
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import numpy as np

data = np.loadtxt("C:/Users/ysokr/Downloads/data-03-diabetes.csv", delimiter =",", dtype = np.float32)

x_data = data[:, 0:-1]
y_data = data[:,[-1]]
      
X = tf.placeholder(tf.float32, shape=[None, 8])
Y = tf.placeholder(tf.float32, shape = [None,1])

W = tf.Variable(tf.random_normal([8, 1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis = tf.sigmoid(tf.matmul(X,W) +b)

cost = tf.reduce_mean(Y * tf.log(hypothesis) + (1 -Y) * tf.log(1-hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01). minimize(cost)

predicted = tf.cast(y > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype = tf.float32))


with tf. Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for step in range(10001):
        cost_val, _ = sess.run([cost, train], feed_dict={X:x_data, Y:y_data})
        if step % 200 == 0:
            print(step, cost_val)
            
    _, _, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X:x_data, Y:y_data})
    print("Accuracy: ", a)


# In[1]:


import pandas as pd


# In[3]:


s = pd.Series([990412, 3448737, 2890451, 2466052], index =["서울", "부산", "인천", "대구"])
s


# In[4]:


s.ndim  #numpy와 동일 


# In[5]:


s.shape


# In[8]:


pd.Series(range(10, 14), index={'a', 'b', 'c', 'd'})


# In[9]:


s.index


# In[10]:


type(s.index)


# In[11]:


s.values


# In[13]:


type(s.values)


# In[14]:


s.name = "인구"
s.index.name = "도시"
s


# In[15]:


s/1000000


# In[16]:


s[1]


# In[17]:


s["부산"]


# In[18]:


s[3], s["대구"]


# In[20]:


s[[0, 3, 1]]


# In[21]:


s[["서울", "대구", "부산"]]


# In[22]:


(250e4 <s) & (s < 500e4)


# In[23]:


s[(250e4 <s) & (s < 500e4)]


# In[24]:


s[1:3]


# In[26]:


s["부산":"대구"]


# In[27]:


s0 = pd.Series(range(3), index = ["a", "b", "cc"])
s0


# In[28]:


s0.a


# In[29]:


s0.b


# In[30]:


s0.cc


# In[ ]:




