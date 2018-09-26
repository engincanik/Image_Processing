
# coding: utf-8

# In[8]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np



# In[3]:

img = mpimg.imread('test.jpg')


# In[4]:

imgplot = plt.imshow(img)


# In[7]:

def my_function_1(image_1):
   print(".....")
   print(image_1.ndim)
   print(image_1.shape)
   print("R icin min deger")
   print(image_1[:,:,0].min())
   print("R icin max deger")
   print(image_1[:,:,0].max() )
   
img = mpimg.imread('test.jpg')
plt.imshow(img)
plt.show()

my_function_1(img)


# In[ ]:



