#!/usr/bin/env python
# coding: utf-8

# In[2]:


def square_num(n):
    return n*n
sample_list = [4, 5, 2, 9]
print("Original List: ",sample_list)
result = list(map(square_num, sample_list))
print("Square the elements of the list:",result)


# In[ ]:




