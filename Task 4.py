#!/usr/bin/env python
# coding: utf-8

# # Import the numpy package under the name np and Print the numpy version and the configuration 

# In[1]:


import numpy as np


# In[4]:


print(np.__version__) 


# In[7]:


np.show_config()


# # Create a null vector of size 10

# In[10]:


import numpy as np
df1=np.zeros(10)
df1


# In[12]:


df1.reshape(2,5)


# # Create Simple 1-D array and check type and check data types in array

# In[15]:


a=np.array([1,2,3,4,56])
a


# In[17]:


a.dtype


# In[18]:


type(a)


# # How to find number of dimensions, bytes per element and bytes of memory used?

# In[26]:


a=np.arange(25)
b=a.reshape(5,5)
print(b)


# In[27]:


a.ndim


# In[32]:


#Memory size of numpy array in byte
a.nbytes


# In[42]:


# bytes per element
a.size


# # Create a null vector of size 10 but the fifth value which is 1

# In[46]:


a= np.zeros(10,dtype='int')
a
a[4]=1
a


# # Create a vector with values ranging from 10 to 49
# 

# In[49]:


a=np.arange(10,50)
a


# # Reverse a vector (first element becomes last)

# In[54]:


a=np.arange(10,49)
a


# In[55]:


a=a[::-1]
a


# # Create a 3x3 matrix with values ranging from 0 to 8

# In[56]:


a=np.arange(0,9)
a


# In[57]:


a.reshape(3,3)


# # Find indices of non-zero elements from [1,2,0,0,4,0]

# In[63]:


x=np.array([1,2,0,0,4,0])
x


# In[65]:


a=np.flatnonzero(x)
a


# # Create a 3x3 identity matrix

# In[68]:


x=np.identity(3)
x


# # Create a 3x3x3 array with random values

# In[71]:


import numpy as np
x=np.random.random((3,3,3))
print(x)


# # Create a 10x10 array with random values and find the minimum and maximum values

# In[73]:


import numpy as np
x=np.random.random((10,10))
x


# In[76]:


# maximum and minimum
xmin=x.min()
xmax=x.max()
print("Minimum value: ",xmin, "Maximum value is :",xmax)


# # Create a random vector of size 30 and find the mean value

# In[77]:


import numpy as np
a=np.random.random(30)
a


# In[78]:


a.mean()


# # Create a 2d array with 1 on the border and 0 inside

# In[81]:


import numpy as np
x=np.ones((5,5),dtype='int')
x


# In[84]:


x[1:-1,1:-1]=0


# In[85]:


x


# # How to add a border (filled with 0's) around an existing array? 

# In[101]:


import numpy as np
x = np.ones((3,3))
print(x)


# In[103]:


x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print(x)


# # How to Accessing/Changing specific elements, rows, columns, etc in Numpy array?
# 
# ### Example -
# #### [[ 1 2 3 4 5 6 7] [ 8 9 10 11 12 13 14]]
# 
# ### Get 13, get first row only, get 3rd column only, get [2, 4, 6], replace 13 by 20

# In[137]:


a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
a


# In[138]:


# Get 13
a[1][-2]


# In[139]:


# Get first row only
a[0]


# In[140]:


# get 3 column only
a[:,[2]]


# In[141]:


# get [2,4,6]
a[0]


# In[143]:


a[0][1::2]


# # How to Convert a 1D array to a 2D array with 2 rows

# In[151]:


a=np.arange(0,25)
a


# In[152]:


a.ndim


# In[170]:


a1=np.reshape(a,(5,5))
a1


# In[171]:


a1.ndim


# # Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
# 
# ## Input:
# 
# ### a = np.array([1,2,3])`
# 
# ##Desired Output:
# 
# ### array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
# 

# In[248]:


a=np.array([1,2,3])


# In[249]:


np.r_[np.repeat(a, 3), np.tile(a, 3)]


# # Write a program to show how Numpy taking less memory compared to Python List?

# In[173]:


import numpy as np
import sys


# In[177]:


# for list
s= range(1000)
print(sys.getsizeof(s))


# In[178]:


print(sys.getsizeof(s)*len(s))


# In[192]:


# for numpy
a= np.arange(1000)
a.itemsize


# In[193]:


a.size*a.itemsize


# # Write a program to show how Numpy taking less time compared to Python List?

# In[221]:


import numpy as np
import time


# In[246]:


#list
size = 1000000  
list1 = range(size)
list2 = range(size)
array1 = numpy.arange(size)  
array2 = numpy.arange(size)
initialTime = time.time()
resultantList = [(a * b) for a, b in zip(list1, list2)]


# In[244]:


print("Time taken by Lists to perform multiplication:", 
      (time.time() - initialTime),
      "seconds")


# In[245]:


# Numpy
initialTime = time.time()
resultantArray = array1 * array2  
print("Time taken by NumPy Arrays to perform multiplication:",
      (time.time() - initialTime),
      "seconds")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




