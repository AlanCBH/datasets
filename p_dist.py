
# coding: utf-8

# In[22]:


import dendropy
import os
import numpy as np
f = open('Desktop/p_0.5.txt','r+')
line = f.readline()
line = f.readline()
total = 0
while line:
    arr = line.split()
    results = [float(arr[i+1]) for i in range(len(arr)-1)]
    total += sum(results)
    line = f.readline()
print(total/1000/999)


# In[23]:


f = open('Desktop/p_1.0.txt','r+')
line = f.readline()
line = f.readline()
total = 0
while line:
    arr = line.split()
    results = [float(arr[i+1]) for i in range(len(arr)-1)]
    total += sum(results)
    line = f.readline()
print(total/1000/999)

