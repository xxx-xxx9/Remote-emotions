#!/usr/bin/env python
# coding: utf-8

# In[ ]:

def match(result, result3):
    
    find = [False,False,False,False]
    m = 0

    for i in range(4):
#         print(i)
        for j in range (4):          
            if result3[i]==result[j]:
                find[i] = True
                m = m+1
    
    return m


