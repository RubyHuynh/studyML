
# coding: utf-8

# In[1]:

import tensorflow as tf
a = tf.constant(r'Hello World python - via jupyter!')
s = tf.Session()
print(s.run(a))


# In[2]:

import tensorflow as tf
a = tf.constant(r'Hello World !')
s = tf.Session()
print(s.run(a))


# In[3]:

import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
print("x:\n{}".format(x))


# In[5]:

from scipy import sparse

eye = np.eye(4)
print ("numPy array: \n {}" . format(eye))
sparse_matrix = sparse.csr_matrix(eye)
print ("\n Scipy sparse CSR matrix: \n{}".format(sparse_matrix))


# In[ ]:



