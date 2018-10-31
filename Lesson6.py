#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt
import numpy as np
import random as random

def matris_c():
    matris = np.random.randint(0,2,(28,28))
    return matris
print(matris_c())


# In[21]:


def mbr_create(matris):
    m=matris.shape[0]
    n=matris.shape[1]
    x_min=m
    x_max=0
    y_min=n
    y_max=0
    
    for i in range(m):
        for j in range(n):
            if(matris[i,j]==1 and x_min>i):
                x_min=i
            if(matris[i,j]==1 and x_max<i):
                x_max=i
            if(matris[i,j]==1 and y_min>j):
                y_min=i
            if(matris[i,j]==1 and y_max<j):
                y_max=i
    return (x_min,x_max,y_min,y_max)
print(mbr_create(matris_c()))


# In[22]:


def get_similarity(character_a,character_b):
    m=character_a.shape[0]
    n=character_a.shape[1]
    
    my_similarity=0
    
    for i in range(m):
        for j in range(n):
            my_similarity=my_similarity+character_a[i,j]*character_b[i,j]
    return my_similarity


# In[25]:


print(get_similarity(matris_c(),matris_c()))


# In[37]:


a = matris_c()
plt.imshow(a,cmap="gray")
plt.show()

max = 0
for i in range(100):
    b= matris_c()
    if(get_similarity(a,b)>max):
        max = get_similarity(a,b)
        c = b
plt.imshow(c,cmap="gray")
print("En yuksek benzerlik =",max)      


# In[40]:


print(get_similarity(a,a))


# In[ ]:




