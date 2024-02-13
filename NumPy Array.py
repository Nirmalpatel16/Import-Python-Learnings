#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
->Linear Algebra library in python.
->Used for performing mathematical and logical oprations on Arrays.
->Provides features for oprations on multidimentional arrays and matrices in Python.
'''


# # 1-Dimentional Array

# In[3]:


import numpy as np


# In[3]:


a = np.array([1,2,3])
print(a)


# # 2-Dimentional Array

# In[5]:


b=np.array([[1,2,3],[4,5,6]])
print(b)


# # Initializing Numpy Array

# 1. Initialize all the elements of x*y array to 0

# In[6]:


np.zeros((3,4))


# 2.Arrange the number between z and y with interval of z

# In[9]:


np.arange(1,10,2)  #last number is not consider i.e 'y'


# In[27]:


#even number between 10 to 20
np.arange(10,20,2)  # last number is not consider here i.e 20


# 3.Arrange z numbers between x and y

# In[11]:


np.linspace(5,10,10)  # here it gives 10 different numbers between the given interval with equal space.


# 4.Filling SAME numbers in a array of dimension x*y

# In[13]:


np.full((2,3),5)


# 5.Filling RANDOM numbers in a array of dimension x*y

# In[15]:


np.random.random((2,3))


# # Numpy Array Inspection

# In[19]:


#Checking the sixe of the array

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)

b= np.array([[1,2,3],[4,5,6],[1,1,1]])
print(b.shape)


# In[9]:


# Resizing the shape of the array

a = np.array([[1,2,3],[4,5,6]])
print('\n',a.shape)
a.shape = (3,2)
print(a)
print('\nReshape of array',a.shape)


# In[33]:


b= np.array([[1,2,3],[4,5,6],[1,1,1],[2,2,2]])
b.shape=(3,4)
print(b)


# In[41]:


#Return the Dimension of the Array

a = np.arange(24)
print('\nI-d :',a)
print('\nDimenson :',a.ndim)

b= a.reshape(2,3,4)
d=b.reshape(2,3,4,1)
print('\n3-D :\n',b)
print('\nReshape\n',d)
print('\nDimenson :',b.ndim)

c= a.reshape(12,2)
print(c)
print(c.ndim)


# In[34]:


#Find the numbers of element in an array
#SIZE: will return the number of element in array

a = np.arange(24)
print(a.size)


# In[38]:


b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b.size) # will return the number of element in array


# # Find the DATATYPE of the Array

# In[45]:


b = np.arange(24)
print(b.dtype)
print(b)

a = np.arange(24,dtype=float)
print(a.dtype)
a


# In[ ]:




