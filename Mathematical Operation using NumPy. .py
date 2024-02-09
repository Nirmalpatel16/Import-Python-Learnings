#!/usr/bin/env python
# coding: utf-8

# # Addition 

# In[1]:


import numpy as np


# In[19]:


np.sum([10,20])


# In[4]:


#Using a variable that is sum of a+b

a,b = 10,40
np.sum([a,b])


# In[15]:


a = np.array([[1,2],[3,4]])
print(a)


# In[11]:


np.sum(a)


# In[12]:


np.sum(a,axis=0)


# In[13]:


np.sum(a,axis=1)


# # Subtarction

# In[26]:


np.subtract(20,30)


# In[32]:


b=np.array([4,5,6])
c=np.array([1,2,3])

np.subtract(b,c)


# # Multiplying

# In[33]:


np.multiply(20,30)


# In[36]:


b=np.array([4,5,6])
c=np.array([1,2,3])

np.multiply(b,c)


# # Division

# In[25]:


np.divide(10/2)


# In[43]:


b=np.array([4,5,6])
c=np.array([1,2,3])

z=np.divide(c,b)
print(z)
y=np.divide(b,c)
print(y)


# # Other Function

# Exponential,Square root,sin,cos,log

# In[54]:


print('Exponent :',np.exp(a))
print('Exponent :',np.exp(b))
print('Square root :',np.sqrt(b))
print('Sin :',np.sin(b))
print('Cos :',np.cos(b))
print('Log :',np.log(b))


# # Array Comparison

# In[55]:


# Element-wise Comparison

a = [1,2,3]
b = [2,4,6]
c = [1,2,3]

# here element wise comparision is done i.e 1!=2, 2!=4, 3!=6
np.equal(a,b)


# In[56]:


# Array-Wise omparison

a = [1,2,3]
b = [2,4,6]
c = [1,2,3]

np.array_equal(a,b)


# # Aggregate Function

# In[59]:


a = [1,2,3]
b = [2,4,6]
c = [1,2,3]

print('sum :',np.sum(a))
print('Minimum:',np.min(a))
print('Mean :',np.mean(a))
print('median :',np.median(a))
print('Coorelation coefficient :',np.corrcoef(a))
print('Standard Deviation :',np.std(a))


# # Concept of Broadcasting

# In[60]:


a= np.array([[0,0,0],[1,2,3],[4,4,4]])
b= np.array([1,2,3])

print(a+b)


# In[62]:


a= np.array([[0,0,0],[1,2,3],[4,4,4]])
b= np.array([[1,2,3],[2,3,4],[5,6,7]])

print(a+b)


# # Array Manipulation 

# In[66]:


a= np.array([0,0,0])
b= np.array([1,2,3])


# In[67]:


#Cancatenation of two arrays
np.concatenate((a,b))


# In[68]:


#Stack array row-wise: Vertically
np.vstack((a,b))


# In[69]:


#Stack array row-wise: Horizontally  (gives same results as concatenation function)
np.hstack((a,b))


# In[70]:


#Combinig  Column-wise
np.column_stack((a,b))


# In[ ]:




