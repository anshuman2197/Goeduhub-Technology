#!/usr/bin/env python
# coding: utf-8

# # List is mutable?

# In[1]:


"Yes, List is mutable because we can change the value of list"

l1=[10,20,30,40,50,'Hello',5.7]


# In[2]:


l1


# In[3]:


l1[4]='Goeduhub Technology'


# In[4]:


l1


# # Does a list need to be homogeneous?

# In[6]:


"""Yes a list need to be Homogeneous because Lists and tuples are mostly identical in Python, except that lists are mutable and
tuples are immutable. Both lists and tuples can be either homogeneous or heterogeneous. 
If we want sequences with enforced homogeneity, use the array module or use NumPy.lists must be homogenous and tuples must be 
fixed-length.Tuples are used as anonymous structures. It is the same way in mathematics. Python's type system, however, 
does not allow us to make these distinctions,we can make tuples of dynamic length, and can make lists with heterogeneous data."""


# # What is the difference between a list and a tuple.

# In[7]:


""" List: 
        1) It is a collection of value that may be different and have no fixed size.
        2) It is ordered and Changeable/Mutable.
        3) It allow Duplicate member.
        4) It is Slower the tuple.
        5) It is homogeneous.
        
    Tuple:
        1) It is also a collection of item that may be different.
        2) It is ordered and Unchangeable.Immutable.
        3) It also allow duplicate value.
        4) It is faster then list.
        5) It is heterogeneous.
        """


# # How to find the number of elements in the list?

# In[13]:


""" The most straightforward way to get the number of elements in a list is to use the Python built-in function len() .
As the name function suggests, len() returns the length of the list, regardless of the types of elements in it."""

l1=[20,10,3.0,40,50,60,70.80,90]
l1


# In[14]:


len(l1)


# # How to check whether the list is empty or not?

# In[20]:


"There are many ways to find list is empty or not"
'1) Using len()'
l1=[]
if len(l1):
    print("List is not empty")
else:
    print("List is empty")


# In[21]:


'2) Comaprison operator'
l1=[]
if len(l1)==0:
    print("List is empty")
else:
    print("List is not empty")


# In[23]:


'3) Using empty list'
if l1==[]:
    print("List is empty")
else:
    print("List is not empty")


# # How to find the first and last element of the list?

# In[24]:


"There are three ways"
'1) Index'
l1=['Sun','Moon','Day','Winter','Summer']
l1


# In[27]:


l1[0] # first element


# In[28]:


l1[-1] # last element


# In[29]:


'2) Slicing'
l1


# In[31]:


l1[::len(l1)-1]


# In[32]:


'3) for loop'
l1


# In[34]:


first_last=[l1[n] for n in (0,-1)]
first_last


# # How to find the largest and lowest value in the list?

# In[39]:


'To find the largest and lowest value we use min and max function'
l1=[10,20,59,89,145,56,82]


# In[45]:


max(l1)


# In[46]:


min(l1)


# # How to access elements of the list?

# In[47]:


"To access element on a list"
'1) Index'
l1


# In[48]:


l1[3]


# In[49]:


'2) Range of Index'
l1[2:5]


# In[50]:


'3) negative index'
l1[-2]


# # Remove elements in a list before a specific index

# In[51]:


'Pop()'
l1


# In[52]:


l1.pop()


# In[53]:


l1


# In[55]:


l1.pop(3)


# In[56]:


l1


# # Remove elements in a list between 2 indixes

# In[69]:


"del"
l1=[20,30,40,50,6097,80,68]


# In[70]:


l1


# In[71]:


del l1[3:5]


# In[72]:


l1


# # Return every 2nd element in a list between 2 indices

# In[73]:


l1=[10,20,30,40,50,60,70,80,90]
l1[::2]


# # Get the first element from each nested list in a list

# In[87]:


l1=[[1,2,3],[4,5,6],[7,8,9],['x','y','z']]
l2=[i[0] for i in l1]


# In[88]:


l2


# # How to modify elements of the list?

# In[92]:


l1=["papa","ki","pari","police station", "mai","khadii"]


# In[93]:


l1


# In[94]:


l1[3]="Theke"


# In[95]:


l1


# # How to concatenate two lists?

# In[96]:


l1=[20,30,40,50,60]
l2=[10,70,80,90,100]
l3=l1+l2
l3


# # How to add two lists element-wise in python?

# In[105]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# # Difference between del and clear?

# In[114]:


""" Clear():
        function delete the all keys and values in the dictionary and leave the dictionary empty. 
    
    Delete():
        While del <dict> delete the complete dictionary when we want to find deleted dictionary then it will give error 
        that <dict> not defined"""

l1=[10,20,30,40,50]
l1.clear()


# In[115]:


l1


# In[116]:


l1=[10,20,30,40,50]
del l1


# In[117]:


l1


# # Difference between remove and pop?

# In[118]:


""" pop():
        takes an index as its argument and will remove the element at that index. If no argument is specified, pop() will 
        remove the last element. pop() also returns the element it removed.

    remove():
        takes an element as its argument and removes it if it’s in the list, otherwise an exception will be thrown."""

l1=[10,20,30,40,50,60]


# In[119]:


l1.pop()


# In[120]:


l1.remove(20)


# In[121]:


l1


# # Difference between append and extend?

# In[125]:


"""Python append():
            method adds an element to a list.
            
    extend():
    method concatenates the first list with another list (or another iterable). Whereas extend() method iterates over its 
    argument adding each element to the list, extending the list."""

l1=[20,30,50,49,50]


# In[126]:


l1.extend([4,5,6])


# In[127]:


l1


# In[128]:


l1.append([4,5,6])


# In[129]:


l1


# # Difference between indexing and Slicing?

# In[130]:


"""Indexing:
        means referring to an element of an iterable by its position within the iterable.
    
    Slicing:
        means getting a subset of elements from an iterable based on their indices.we might say my juror number was my index."""

l1


# In[132]:


l1[3]


# In[133]:


l1[2:1:-1]


# # Difference between sort and sorted?

# In[141]:


"""sort():
        basically works with the list itself. It modifies the original list in place. The return value is None.

    sorted():
        works on any iterable that may include list, dict and so on. It returns another list and doesn't modify the original 
        list.

"""
l1=[100,40,30,50,90,70,80]


# In[142]:


l1.sort()


# In[143]:


l1


# In[147]:


l2=[100,80,40,80,20,60,10,50]
l3=sorted(l2)


# In[150]:


l3


# In[151]:


l2


# # Difference between reverse and reversed?

# In[152]:


"""reverse():
        actually reverses the elements in the container. 
        
    reversed():
        doesn't actually reverse anything, it merely returns an object that can be used to iterate over the container's 
        elements in reverse order. If that's what we need, it's often faster than actually reversing the elements"""

l1


# In[153]:


l1.reverse()


# In[154]:


l1


# In[162]:


alph = ["a", "b", "c", "d"]

x= reversed(alph)
for i in x:
    print(i)


# # Difference between copy and deepcopy?

# In[166]:


""" Shallow:
         A shallow copy creates a new object which stores the reference of the original elements.So, a shallow copy doesn't
         create a copy of nested objects, instead it just copies the reference of nested objects. 
         This means, a copy process does not recurse or create copies of nested objects itself.
             
    Deep Copy:
        A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
    The deep copy creates independent copy of original object and all its nested objects.
"""

'1) Shallow Copy'
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)


# In[167]:


'2) Deep Copy'
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)


# # How to remove duplicate elements in the list?

# In[170]:


'1)'
list_1 = [1, 2, 1, 4, 6]

print(list(set(list_1)))


# In[171]:


'2)'
list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2) ))


# # How to find an index of an element in the python list?

# In[172]:


"The index() method returns the index of the specified element in the list."
l1


# In[176]:


l1.index(80)


# In[177]:


l1.index(40)


# # How to find the occurrences of an element in the python list?

# In[179]:


l2 = ["a", "b", "a","c","d","a",'x',"a"]
occurrences = l2.count("a")

print(occurrences)


# In[183]:


from collections import Counter
a_list = ["a", "b", "a","c","d","a",'x',"a"]
occurrences =Counter(a_list)
print(occurrences)


# # How to insert an item at a given position?

# In[184]:


l1


# In[185]:


l1[2]="Hello PaPas Pari "


# In[187]:


l1


# # How to check if an item is in the list?

# In[191]:


l1=[10,20,30,40,50,60,70,80,90,100]
l1


# In[194]:


n=int(input("enter number: "))
if n in l1:
    print("It is in the list")
else: 
    print("sorry")


# # How to flatten a list in python?

# In[196]:


li1 = [range(4), range(7)]
flattened_list = []

for x in li1:
    for y in x:
        flattened_list.append(y)
y


# In[197]:


regular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]
flat_list = [item for sublist in regular_list for item in sublist]
print('Original list', regular_list)
print('Transformed list', flat_list)


# In[198]:


data = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]
flat_list = []
for item in data:
    flat_list += item
print(flat_list)


# # How to convert python list to other data structures like set, tuple, dictionary?

# In[199]:


'1) List to a tuple'
def convert(list):
    return tuple(list)

list = [1, 2, 3, 4]
print(convert(list))


# In[201]:


'2 List to set'
names = ["George", "Josh", "James", "Mark", "Carlo", "James", "Andy", "Sara", "Andy"]
unique = set(names)  
print(unique)


# In[205]:


'3) List to dictionary'
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
         
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))


# In[206]:


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
         
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))


# # How to apply a function to all items in the list?

# In[213]:


'1)'
lst = [1, 2, 3]
ans = []
for x in lst:
    def res(x): return x*2
    ans.append(res(x))
print(ans)


# In[215]:


'2)'

def double(integer):
    return integer*2
integer_list = [1, 2, 3]
  
output_list = [double(i) for i in integer_list]
  
print(output_list)


# # How to filter the elements based on a function in a python list?

# In[219]:


'1)'
scores = [70, 60, 80, 90, 50]

filtered = []

for score in scores:
    if score >= 70:
        filtered.append(score)

print(filtered)


# In[220]:


'2)'
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filtered = filter(fun, sequence)
  
print('The filtered letters are:')
for s in filtered:
    print(s)


# In[221]:


'3)'
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False

filtered_vowels = filter(filter_vowels, letters)

print('The filtered vowels are:')
for vowel in filtered_vowels:
    print(vowel)


# # How python lists are stored in memory?

# In[223]:


"""Instead of storing values in the memory space reserved by the variable, Python has the variable refer to the value.
Similar to pointers in C, variables in Python refer to values (or objects) stored somewhere in memory.
Python keeps an internal counter on how many references an object has"""


# In[ ]:




