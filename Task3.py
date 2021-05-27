#!/usr/bin/env python
# coding: utf-8

# # Write a Python Program to sort (ascending and descending) a dictionary by value. 

# In[3]:


d={1:'Anil',2:'suraj',3:'Vasu',4:'Subhramaniyam',5:'Sheetal'}
d


# In[13]:


# Accending
d1=sorted(d.items())
d1


# In[8]:


d2=sorted(d.keys())
d2


# In[10]:


d3=sorted(d.values())
d3


# In[19]:


# decending
d4=sorted(d.items(),reverse=True)
d4


# # Write a Python Program to add a key to a dictionary. 

# In[24]:


d={0: 10, 1: 20}
d.update({2:30})
d


# # Write a  program asks for City name and Temperature and builds a dictionary using that Later on you can input City name and it will tell you the Temperature of that City.

# In[83]:


City = input("Enter City Name: ")
Temp = input("Enter Temperature: ")
dict1 = {}
dict1[City] = Temp
print(dict1)


# # or

# In[77]:


l1 = dict() 
data = input('Enter City name & Temperature separated by ":" ') 
temp = data.split(':') 
l1[temp[0]] = int(temp[1]) 
 
for key, value in l1.items(): 
    print('City: {}, Temperature: {}'.format(key, value)) 


# # Write a Python program to convert list to list of dictionaries.
# 
# 

# In[42]:


l1=["Black", "Red", "Maroon", "Yellow"]
l2=["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'l1':f,'l2':c} for f,c in zip(l1,l2)])


# #  We have following information on Employees and their Salary (Salary is in lakhs),

# In[46]:


# Using above create a dictionary of Employees and their Salary
emp=['John','Smith','Alice','Daneil']
sal=[14,13,32,21]
total=[{'emp':a,'sal':b} for a,b in zip(emp,sal)]
print(total)


# In[55]:


# Write a program that asks user for three type of inputs
emp1=dict.fromkeys(emp)
sal1=dict.
# num1=input("enter Employee name, Salary or print: ")
# if num1==emp.keys():
#     print(num1)


# In[ ]:





# #  What is the difference between a set and a frozenset? Create any set and try to use frozenset(setname).

# In[56]:


"""Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, 
elements of the frozen set remain the same after creation. Due to this, frozen sets can be used as keys in Dictionary or as 
elements of another set.
"""


# In[61]:


# set
l1=[10,20,30,40,50,60,70,80,48,59,60,50,20,10]
print(l1)


# In[64]:


set1=set(l1)
set1


# In[67]:


frz=frozenset(set1)
frz


# #  Find the elements in a given set that are not in another set

# In[68]:


set1 = {10,20,30,40,50}
set2 = {40,50,60,70,80}
print(set1.difference(set2))

