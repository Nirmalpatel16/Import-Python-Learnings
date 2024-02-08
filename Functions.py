#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
In Python a function is defined using the 'def' keyword

You can pass data, known as parameters, into a function or you can pass empty functio as well

To call a function, use the function name followed by parenthesis

Information can be passed into functions as arguments.

Saves time beacuse single function can be used at mamy locations and if some changes need to be made then only change in single location that will change throughout

'''


# In[4]:


def hello_func():
    pass
print(hello_func())


# In[24]:


def my_function():
    print('hello python')
my_function()


# In[21]:


#Arguments are specified after the function name, inside the parentheses.
#You can add as many arguments as you want, just separate them with a comma.

def my_function(studentname, studentID):
  print("name: "+studentname   + " ,ID: "+ studentID )

my_function("Emil",'1')
my_function("Tobias",'2')
my_function("Linus",'3')


# In[5]:


'''
*args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly

**kwargs:
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:'''

def Student_info(*args,**Kwargs):
    print(args)
    print(Kwargs)
    
Student_info('Math','Art',name = 'Joy', age = 22)
Student_info('Math','Art','Biology',name = 'Joy', age = 22)


# In[1]:


def myfunc(x):
    return x+10
myfunc(5)


# In[ ]:




