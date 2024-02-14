#!/usr/bin/env python
# coding: utf-8

# # Create an Empty Numpy Array

# To create an empty NumPy array, we can use the numpy.empty() function. 
# The empty() function in NumPy is used to create an empty array with a specified shape.
# Random values are filled.

# In[1]:


import numpy as np


# In[12]:


a = np.empty((2,3))
print(a)


# In[10]:


b = np.empty((3,4))
print(b)


# # Create a Full Numpy Array

# To create a full NumPy array, you can use the numpy.full() function.
# The full() function in NumPy creates an array of a given shape and fills it with a specified value. A full NumPy array is an array where all the elements have the same predefined value.

# In[14]:


c= np.full((2,3),6)
print(c)


# In[16]:


d= np.full((4,5),0.5)
print(d)


# Example 1: In the example, we create an empty array of 3X4 and a full array of 3X3 of INTEGER type.

# In[32]:


#Create an empty array

a = np.empty((3,4), dtype = int)
print("Empty Array")
print(a)

# Create Full numpy array

b = np.full((3,3),2.1,dtype=int)
print('\n \n Full Array')
print(b)


# Example 2: In the example, we create an empty array of 4X2 and a full array of 4X3 of INTEGER and FLOAT type.

# In[36]:


# Create empty array

a = np.empty((4,2),dtype=int)
print('Empty Array')
print(a)

#Create Full array

b = np.full((4,2),50.3,dtype=float)
print('\nFull Array')
print(b)


# # Create a Numpy array filled with all zeros

# We can use Numpy.zeros() method to do this task.
# Budefult datatype is FLOAT

# In[40]:


a=np.zeros((2),dtype=int)
print(a)


# In[46]:


b = np.zeros([3,4])
print('without data type---Bydefult it takes FLOAT')
print(b)

c = np.zeros([3,4],dtype=int)
print('\nwith data type')
print(c)


# # Find the number of rows and columns of a given matrix using NumPy

# The shape attribute of a NumPy array returns a tuple representing the dimensions of the array.
# For a two-dimensional array, the shape tuple contains two values: the number of rows and the number of columns.

# Example 1: Using .shape Attribute

# In[50]:


#Here we are finding the number of rows and columns of a given matrix using Numpy.shape.

a = np.array([[1,2,3],[4,5,6]])
print(a)
print('\ndimenson')
print(a.shape)
rows,columns=np.shape(a)
print('\nrows',rows)
print('\ncolumns',columns)


# In[65]:


a= np.arange(1,12,2)
print('\nArray\n',a)
print('\nReshape\n',a.reshape(2,3))
rows,columns=a.reshape(2,3)
print('\nRows\n',rows)
print('\ncolumns\n',columns)


# Example 2: Using Indexing

# In[66]:


#Here we are finding the number of rows and columns of a given matrix using Indexing.


# In[113]:


a = np.array([[11,12,13],[14,15,16],[17,18,19],[1,2,3]])
print('\n Array\n',a)
print('\nShape\n',a.shape)
print('\nrows\n',a.shape[0])
print('\ncolumns\n',a.shape[1])
print('\nReshape\n',a.reshape(3,4))
print('\nReshape Again\n',a.reshape(2,3,2,1))
b = a.reshape(2,3,2,1)
c= np.shape(b)
print('\nShape of Reshape Matrix\n',c)
print('\nrows\n',b.shape[0])
print('\ncolumns\n',b.shape[1])
print('\ncolumns\n',b.shape[2])
print('\ncolumns\n',b.shape[3])


# # Find length of one array element in bytes and total bytes consumed by the elements in Numpy

# In NumPy we can find the length of one array element in a byte with the help of itemsize . It will return the length of the array in integer. And in the numpy for calculating total bytes consumed by the elements with the help of nbytes

# In[106]:


a = np.array([1,2,3])
print(a)
print('\nSize of the array\n',a.size)
print('\nlength(int) of the array in bytes\n',a.itemsize,'(in bytes)')
print('\ntotal bytes consumed by the elements\n',a.nbytes)


# In[125]:


b = np.arange(30)

print('\nSize of the array\n',b.size)
print('\nlength(int) of the array in bytes\n',b.itemsize,'(in bytes)')
print('\ntotal bytes consumed by the elements\n',b.nbytes)


# # Create a Numpy array filled with all ones

# In[1]:


import numpy as np


# In[2]:


#We can use Numpy.ones() method to do this task.


# In[10]:


a = np.ones([3],dtype=int)
print('\nMatrix a\n',a)

b= np.ones((3,4),dtype=float)
print('\nMatrix b\n',b)


# # Check whether a Numpy array contains a specified row

# In[14]:


a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print('\nMatrix a\n',a)

#Check wheather any list value is ptesent in array 'a'
print("\nCheck, is this list present in array 'a'\n",[1,2,3,4,5] in a.tolist())
print("\nCheck, is this list present in array 'a'\n",[11,12,14,15,13] in a.tolist())


# # How to Remove rows in Numpy array that contains non-numeric values?

# In[26]:


a = np.array([[1,2,3],[np.nan,2,5],[5,5,6]])
print(a)

# Remove non-numeric values
print('\nNew matrix comes with non null values as below\n',a[~np.isnan(a).any(axis=1)])


# In[27]:


n = np.array([[10.5, 22.5, 3.8], 
                  [41, np.nan, np.nan]]) 
  
print("Given array:") 
print(n) 
  
print("\nRemove all rows containing non-numeric elements") 
print(n[~np.isnan(n).any(axis=1)]) 


# # Combining a one and a two-dimensional NumPy Array

# Sometimes we need to combine 1-D and 2-D arrays and display their elements. Numpy has a function named as numpy.nditer(), which provides this facility.

# In[47]:


#1-D array
a = np.array([1,2,3])
print('\n1-D\n',a)
print('\nDimenson\n',a.ndim)

#2-D array
b = np.arange(6).reshape(2,3)
print('\n2-D\n',b)
print('\nDimenson\n',b.ndim)

#combine 1-D and 2-D matrix

for x,y in np.nditer([a,b]):
    print('%d:%d'%(x,y))


# # How to compare two NumPy arrays?

# Here we will be focusing on the comparison done using NumPy on arrays. Comparing two NumPy arrays determines whether they are equivalent by checking if every element at each corresponding index is the same. 

# Method 1: We generally use the == operator to compare two NumPy arrays to generate a new array object. Call ndarray.all() with the new array object as ndarray to return True if the two NumPy arrays are equivalent. 

# In[56]:


#Example-1
print('\nExample-1')
a = np.array([[50,60,70],[100,200,300]])
b = np.array([[51,59,71],[99,201,299]])

print('\nMatrix a\n',a)
print('\nMatrix b\n',b)

#Comparing Two matrix 

comparison = a==b
c=comparison.all()
print('\nResult\n',c)


#Example-2
print('\nExample-2')
a = np.array([[50,60,70],[100,200,300]])
b = np.array([[50,60,70],[100,200,300]])

print('\nMatrix a\n',a)
print('\nMatrix b\n',b)

#Comparing Two matrix 

comparison = a==b
c=comparison.all()
print('\nResult\n',c)


# In[58]:


#Method 2: We can also use greater than, less than and equal to operators to compare. To understand, have a look at the code below.

#Syntax : numpy.greater(x1, x2[, out])
#Syntax : numpy.greater_equal(x1, x2[, out])
#Syntax : numpy.less(x1, x2[, out])
#Syntax : numpy.less_equal(x1, x2[, out])


# In[63]:


a = np.array([[50,60,70],[100,200,300]])
b = np.array([[51,59,71],[99,201,299]])

print('a>b')
print(np.greater(a,b))

print('a<b')
print(np.less(a,b))

print('a>=b')
print(np.greater_equal(a,b))

print('a>=b')
print(np.less_equal(a,b))


# In[64]:


#Method 3: This array_equal() function checks if two arrays have the same elements and same shape.


# In[65]:


a = np.array([[50,60,70],[100,200,300]])
b = np.array([[51,59,71],[99,201,299]])

if np.array_equal(a,b):
    print('Equal')
else:
    print('Not Equal')


# # How to get all 2D diagonals of a 3D NumPy array?

# Let’s see the program for getting all 2D diagonals of a 3D NumPy array. So, for this we are using numpy.diagonal() function of NumPy library. This function return specified diagonals from an n-dimensional array.

# In[82]:


#Example -1
# Create 3D diagonal array 
a = np.arange(2*3*4).reshape(2,3,4)
print('\n3-D Array\n',a)

# Create 2D diagonal array 
b = np.diagonal(a,axis1=1,axis2=2)
print('\n2d diagonal array:\n',b)

#Example -2
# Create 3D diagonal array
x = np.arange(10*13*8).reshape(10,13,8)
print('\n3-D Array\n',x)

# Create 2D diagonal array 
y = np.diagonal(x,axis1=1,axis2=2)
print('\n2d diagonal array:\n',y)


# In[87]:


a = np.arange(24).reshape(2,3,4)
print(a)


# # Flatten a Matrix in Python using NumPy

# Let’s discuss how to flatten a Matrix using NumPy in Python. By using ndarray.flatten() function we can flatten a matrix to one dimension in python.

# In[100]:


#Example-1
print('Example-1')
a = np.arange(24).reshape(2,3,4)
print(a)

#using array.flatten() method 
b=a.flatten()
print('\n3-D converted into 1-D by using flatten function\n',b)

#Example-2
print('\nExample-2')
# declare matrix with np 
x = np.array([[6, 9, 12], [8, 5, 2], [18, 21, 24]]) 
print('\n',x)
  
# using array.flatten() method 
y = x.flatten(order='A') 
print('\n3-D converted into 1-D by using flatten function\n',y) 


# # Counts the number of non-zero values in the array

# numpy.count_nonzero() function counts the number of non-zero values in the array arr.

# In[103]:


a = np.array([[0,1,2,3,0],[0,6,7,8,0]])
print(a)
b = np.count_nonzero(a)
print('\n Non zero count of elements\n',b)


# # Trim the leading and/or trailing zeros from a 1-D array

# numpy.trim_zeros function is used to trim the leading and/or trailing zeros from a 1-D array or sequence.

# In[123]:


a = np.array([0,0,0,0,1,2,3,4,0,0,0,6,7,8,0,0,0])
print('1-D without trim arrays\n',a)
b=np.trim_zeros(a)
c=np.trim_zeros(a,'f')
d=np.trim_zeros(a,'b')
print('\n1-D with trim arrays (from both side)\n',b)
print('\n1-D with trim arrays (from front side)\n',c)
print('\n1-D with trim arrays (fromback side)\n',d)


# In[ ]:




