#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import numpy as np

x = np.loadtxt('random_number.txt')
y = np.loadtxt('using_equation.txt')

plt.title('Visualization')
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('Visualization.jpg')


# In[ ]:




