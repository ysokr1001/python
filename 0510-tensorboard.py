#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib as mpl
import matplotlib.pyplot as plt


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


plt.plot([1, 4, 9, 16, 18])


# In[ ]:


plt.title("제목")
plt.plot([10, 20, 30, 40], [1, 7, 9, 16])
plt.show()


# In[ ]:


set(sorted([f.name for f in mpl.font_manager.fontManager.ttflist]))


# In[ ]:


mpl.rc('font', family='NanumGothic')
mpl.rc('axes',unicode_minus=False)


# In[ ]:


import numpy as np
x_data = np.array([10, 20, 30, 40])
y_data = np.array([1, 4, 9, 16])
plt.plot(x_data, y_data)


# In[ ]:


plt.title("타이틀")
plt.plot([10, 20, 30, 40], [1, 7, 9, 16], 'g*--')
plt.show()


# In[ ]:


plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c="b", lw=3, ls="-.", marker="*", ms=20, mew=4,mec="g", mfc="r")
plt.title("Style")
plt.show()
         


# In[ ]:


plt.title("x축, y축의 범위 설정")
plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
plt.xlim(0, 50)
plt.ylim(-10, 30)
plt.show()


# In[ ]:


import numpy as np
X = np.linspace(-np.pi, np.pi, 100)
C = np.cos(X)
plt.title("x축과 y축의 tick label 설정")
plt.plot(X, C)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
plt.yticks([-1, 0, +1])
plt.show()


# In[ ]:


import tensorflow.compat.v1 as tf
tf.compat.v1.disable_v2_behavior()
import matplotlib.pyplot as plt
import numpy as np

population_inc = [0.3, -0.78, 1.26, 0.03, 1.11, 15.17, 0.24, -0.24, -0.47, -0.77, -0.37, -0.85, -0.41, -0.27, 0.02, -0.76, 2.66]
population_old = [12.27, 14.44, 11.87, 18.75, 17.52, 9.29, 16.37, 19.78, 19.51, 12.65, 14.74, 10.72, 21.94, 12.83, 15.51, 17.14, 14.42]
del population_inc[5]
del population_old[5]

a=tf.Variable(tf.random_uniform([1], 0, 10, dtype = tf.float64, seed=0))
b=tf.Variable(tf.random_uniform([1], 0, 100, dtype = tf.float64, seed = 0))

y = a * population_inc + b

rmse = tf.sqrt(tf.reduce_mean(tf.square( y - population_old)))

learning_rate = 0.1

gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(2001):
        sess.run(gradient_decent)
        if step % 100 ==0:
            print("Epoch: %.f, RMSE = %.04f, a 기울기 a = %.4f, y절편 b = %.4f"%(step, sess.run(rmse),sess.run(a),sess.run(b)))
    data_a=sess.run(a)
    data_b=sess.run(b)

line_x = np.arange(min(population_inc), max(population_inc), 0.01)
line_y = data_a * line_x + data_b
print(line_x)
print(line_y)

plt.plot(line_x, line_y, 'r-')
plt.plot(population_inc, population_old, 'bo')
plt.xlabel('population Frowth Rate (%)')
plt.ylabel('Elderly Frowth Rate (%)')
plt.show()


# In[ ]:


import tensorflow as tf
data = [[2, 81], [4, 93], [6, 91], [8, 97]]
x_train = [x_row[0] for x_row in data]
y_train = [y_row[1] for y_row in data]
w= tf.Variable(tf.random.uniform([1], 0, 10, dtype=tf.float64, seed = 0))
b= tf.Variable(tf.random.uniform([1], 0, 100, dtype=tf.float64, seed = 0))

def hypothesis(w,b):
    return x_train* w + b
def costFunc():
    return tf.sqrt(tf.reduce_mean(tf.square(hypothesis(w,b) - y_train)))

def cost(w,b):
    return tf.sqrt(tf.reduce_mean(tf.square(hypothesis(w,b) - y_train)))

opt = tf.keras.optimizers.SGD(learning_rate=0.1)
for i in range(2000):
    opt.minimize(costFunc, var_list=[w,b])
    if i % 100 == 0:
        print(i, f'{cost(w,b)}, {w.numpy()}, {b.numpy()}')


# In[25]:


import tensorflow as tf
from datetime import datetime

data = [[2, 81], [4, 93], [6, 91], [8, 97]]
x_train = [x_row[0] for x_row in data]
y_train = [y_row[1] for y_row in data]
w= tf.Variable(tf.random.uniform([1], 0, 10, dtype=tf.float64, seed = 0))
b= tf.Variable(tf.random.uniform([1], 0, 100, dtype=tf.float64, seed = 0))

def hypothesis(w,b):
    return x_train* w + b

@tf.function
def costFunc():
    return tf.sqrt(tf.reduce_mean(tf.square(hypothesis(w,b) - y_train)))

def cost(w,b):
    return tf.sqrt(tf.reduce_mean(tf.square(hypothesis(w,b) - y_train)))

stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
logdir = 'logs/mylogs/%s'%stamp
writer = tf.summary.create_file_writer(logdir)
tf.summary.trace_on(graph=True, profiler=True)
costFunc()
with writer.as_default():
    tf.summary.trace_export(name='graph_t1', step=0, profiler_outdir=logdir)
    
opt = tf.keras.optimizers.SGD(learning_rate=0.1)
for i in range(2000):
    opt.minimize(costFunc, var_list=[w,b])
    if i % 100 == 0:
        print(i, f'{cost(w,b)}, {w.numpy()}, {b.numpy()}')


# In[ ]:




