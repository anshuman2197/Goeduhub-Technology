#!/usr/bin/env python
# coding: utf-8

# # Question1

# In[24]:


Colors=["Yellow","White","Green","Black"]

Fruits=["Apple","Papaya","Mango","Orange"]

Animals=["Tiger","Lion","Deer","Zebra"]

n=input("Enter The Color,fruits and animals and first letter with capital letter: ")

if n in Colors:
    print(n,"Its belongs To color")
    
if n in Fruits:
    print(n,"Its belongs to Fruits")
    
if n in Animals:
    print(n,"Its belongs to Animals")


# # Question 2
#         

# In[28]:


n1=input("Enter The Color,fruits and animals and first letter with capital letter: ")
n2=input("Enter The Color,fruits and animals and first letter with capital letter: ")
if n1 in Colors and n2 in Colors:
    print(n1, n2, "Both are Color")
elif n1 in Fruits and n2 in Fruits:
    print(n1, n2, "Both are Fruits")
elif n1 in Animals and n2 in Animals:
    print(n1, n2, "Both are Animals")
else:
    print(n1, n2, "They don't belong to same category")


# # Question3

# In[38]:


a=int(input("Enter number: "))
if a>60:
    print(" it is good ")
elif a<=60 and a>=40:
    print("score is normal")
else:
    print("score is low")


# # Question 4

# In[6]:


count=0
result=["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"]
for x in result:
    if x=='Pass':
        count+=1
print("You Passed",count,"times")


# # Question 5

# In[9]:


n= int(input("Enter a Number:"))
for i in range(n):
    print("* "*(i+1))
for i in range(n-1):
    print("* "*(n-i-1))


# # Question 6

# In[18]:


a=0
for i in range(1,51):
    if i%10==0:
        n=input("You are Tired: ")
        if n=="Yes":
            print("You didn't finish the race")
            a=1
            break
        elif n=='No':
            continue
    if a==0:
        print('Congratulation You have finish the race')
        


# # Question 7

# In[30]:


for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i)


# # Question 8

# In[41]:


for i in range(10,21):
    if i%2!=0:
        print(i**2,"Odd number")
    else:
        print('Not for even number')


# # Question 9

# In[65]:


marks_list = [65, 75, 2100, 95, 83]
n=int(input("Enter The Number: "))
if n not in marks_list:
    print("It is not in List")
else:
    for x in marks_list:
        if n==x:
            print("Yes its belong to",n,"in Mark List",x)


# In[ ]:




