#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import keyword 
import operator
from datetime import datetime 
import os


# In[2]:


x = "i love coding"
print(x.capitalize())
print(x.title())


# # Keywords 
# 
# Keywords are the reserved words in Python and cant be used as an identifier

# In[2]:


print(keyword.kwlist)   #list all python Keywords 


# In[3]:


len(keyword.kwlist)


# # Identifiers
# 
# An identifier is a name given to entities like class, functions, variables, etc. It helps to differentiate one entity from another.

# In[4]:


1var = 10 # Identifier can't start with a digit


# In[5]:


val2@ = 35 # Identifier can't use special symbols


# In[6]:


import = 125 # Keywords can't be used as identifiers


# In[7]:


"""
Correct way of defining an identifier 
(Identifiers can be a combination of letters in lowercase (a to z) or uppercase (
"""
val2 = 10


# In[8]:


val_2 = 99


# # Statements
# Instructions that a Python interpreter can execute.

# In[9]:


# Single line statement
p1 = 10 + 20
p1


# In[10]:


# Single line statement
p2 =['a', 'b', 'c', 'd']
p2


# In[11]:


# Multiple line statement
p1 = 20 + 30+ 40 + 50 ++ 70 + 80
p1


# In[12]:


# Multiple line statement
p2 =['a', 
'b', 
'c', 
'd'
]
p2


# # Indentation
# Indentation refers to the spaces at the beginning of a code line. It is very important as Python uses indentation to indicate a block of code.If the indentation is not correct we will endup with IndentationErrorerror .

# In[14]:


p = 10
if p == 10:
    print('P is equal to 10') # correct indentation


# In[15]:


for i in range (0,5):
    print (i)


# In[16]:


j = 20 
for i in range (0,5):
    print(i)
print(j)


# # Docstrings
# 1) Docstrings provide a convenient way of associating documentation with functions, classes, methods or modules.\
# 2) They appear right after the definition of a function, method, class, or module.

# In[21]:


def square(num):
    '''Square function:- This function will return the square of a number'''
    return num**2


# In[22]:


square(2)


# In[23]:


square(5)


# In[24]:


square.__doc__


# In[26]:


def evenodd(num):
    if num % 2 ==0:
        print("Even Number")
    else:
        print("Odd Number")


# In[27]:


evenodd(3)


# In[28]:


evenodd(0)


# # Variables
# A Python variable is a reserved memory location to store values.A variable is created the moment you first assign a value to it.

# In[29]:


p = 30 


# In[30]:


id(p)


# In[31]:


hex(id(p))


# In[32]:


intvar = 10 # Integer variable
floatvar = 2.57 # Float Variable
strvar = "Python Language" # String variable
print(intvar)
print(floatvar)
print(strvar)


# In[34]:


a , b , c = 10, 20 ,30
print(a)
print(b)
print(c)


# In[35]:


a = b = c= d= 44 #all variables pointing to same value 


# In[36]:


print (a,b,c,d)


# # DATA TYPES 
# 
# ## Numeric 

# In[37]:


val1= 10 #integer data type
print(val1)
print(type(val1))
print(sys.getsizeof(val1))
print(val1, "id Integer?", isinstance(val1,int))


# In[38]:


val2 = 92.78 # Float data type
print(val2)
print(type(val2)) # type of object
print(sys.getsizeof(val2)) # size of float object in bytes
print(val2, " is float?", isinstance(val2, float)) # Val2 is an instance of floa


# In[39]:


val3 = 25 + 10j # Complex data type
print(val3)
print(type(val3)) # type of object
print(sys.getsizeof(val3)) # size of float object in bytes
print(val3, " is complex?", isinstance(val3, complex)) # val3 is an instance 


# In[40]:


sys.getsizeof(int()) # size of integer object in bytes 


# In[41]:


sys.getsizeof(float())  # size of float object in bytes


# In[42]:


sys.getsizeof(complex()) # size of complex object in bytes


# ## Boolen 
# 
# Boolean data type can have only two possible values true or false

# In[44]:


bool1 = True


# In[45]:


bool2 = False


# In[47]:


print(type(bool1))


# In[48]:


print(type(bool2))


# In[49]:


isinstance(bool1,bool)


# In[50]:


bool(0)


# In[51]:


bool(1)


# In[52]:


bool(None)


# In[53]:


bool (False)


# ## Strings creation 

# In[54]:


str1 = "Hello Python"


# In[55]:


str1


# In[56]:


mystr = "Hello World"
mystr


# In[59]:


mystr = '''Hello World'''
mystr


# In[1]:


len(mystr)


# ## String Indexing 

# In[61]:


str1


# In[62]:


str1[0]


# In[64]:


str1[len(str1)-1]


# In[65]:


str1[-2]


# In[67]:


str1[0:5]


# In[71]:


str1[6:12]


# In[74]:


str1[0:]


# ## Update & Delete String 

# In[75]:


str1


# In[79]:


str1[0:5] = 'Hillo'   #strings are immutable which means elements of a string cannot be changed


# In[80]:


del str1 #delete a string
print(str1)


# ## String Concatenation

# In[84]:


s1 = "Hello"
s2 = 'Anand'
s3 = s1 + " " + s2
print(s3)


# In[85]:


for i in s3:
    print(i)


# In[87]:


for i in enumerate(s3):
    print(i)


# In[88]:


list(enumerate(s3))


# ## String Partitioning

# In[89]:


"""
The partition() method searches for a specified string and splits the string into
- The first element contains the part before the argument string.
- The second element contains the argument string.
- The third element contains the part after the argument string.
"""
str5 = "Natural language processing with Python and R and Java"
L = str5.partition("and") 
print(L)


# In[90]:


## Strings Functions

s5 = "    Hello Everyone    "
s5


# In[91]:


s5.strip()   #remove white spaces from both end 


# In[93]:


s5.rstrip()


# In[94]:


s5.lstrip()


# In[96]:


s6 = "************Hello Everyone***********All the Best**********"
s6


# In[1]:


(5 > 4) or (3 == 5)


# In[2]:


not ((5 > 4) or (3 == 5))		


# In[3]:


(True and True) and (True == False)


# In[4]:


(not False) or (not True)


# In[ ]:




