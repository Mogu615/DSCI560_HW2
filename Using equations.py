#!/usr/bin/env python
# coding: utf-8

# In[3]:


file = open('random_number.txt')

with open('using_equation.txt','w') as f:
    for line in file:
        y = 3*int(line)+6
        f.write(str(y)+'\n')

