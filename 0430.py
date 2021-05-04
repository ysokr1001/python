#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tensorflow as tf
print(tf.__version__)


# In[9]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np 
import tensorflow as tf
np.random.seed(3)
tf.random.set_seed(3)
Data_set = np.loadtxt("C:/Users/ysokr/Desktop/딥러닝/ThoraricSurgery.csv", delimiter = ",")
X = Data_set[:,0:17]
Y = Data_set[:,17]
model = Sequential()
model.add(Dense(30, input_dim=17, activation = 'relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=100, batch_size=10)
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))


# In[ ]:




