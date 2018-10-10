
# coding: utf-8

# In[20]:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('test.jpg')
plt.imshow(img)
plt.show()
get_ipython().magic('matplotlib inline')

plt.subplot(1,2,1),plt.imshow(img)
plt.subplot(1,2,2),plt.imshow(255-img)


# In[ ]:




# In[6]:

from PIL import Image
import PIL.ImageOps

image = Image.open('test.jpg')

inverted_image = PIL.ImageOps.invert(image)

inverted_image.save('new_name.jpg')


# In[9]:

image.show()


# In[13]:

inverted_image.show()


# In[77]:

def my_H(image):
    H_1 = {}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,0]) in H_1.keys():
                H_1[image[i,j,0]]=H_1[image[i,j,0]]+1
            else:
                H_1[image[i,j,0]]=1
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,1]) in H_1.keys():
                H_1[image[i,j,1]]=H_1[image[i,j,1]]+1
            else:
                H_1[image[i,j,1]]=1
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,2]) in H_1.keys():
                H_1[image[i,j,2]]=H_1[image[i,j,2]]+1
            else:
                H_1[image[i,j,2]]=1
    return H_1


# In[78]:

my_H(img)
plt.bar(my_H(img).keys(), my_H(img).values(),color='g')
plt.show()


# In[ ]:




# In[ ]:



