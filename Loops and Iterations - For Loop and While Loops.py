#!/usr/bin/env python
# coding: utf-8

# In[6]:


nums = [1,2,3,4,5,6,7,8,9]

for num in nums:
    print(num)


# In[2]:


# When it comes to FOR loop Break and Continue palys am important role

nums = [1,2,3,4,5,6,7,8,9]

for num in nums:
   
    if num==3:
        print('Found!')
        break
    print(num)


# In[15]:


nums = [1,2,3,4,5,6,7,8,9]

for num in nums:
    if num==3:
        print('Found!')
        continue
    print(num)


# In[48]:


#Loop within the loop

nums = [1,2,3,4,5,6,7,8,9]

for num in nums:
    for latter in 'abc':
        for ab in [12,23]:
            print(latter,num,ab)
            break
            
           
            
        


# In[ ]:




