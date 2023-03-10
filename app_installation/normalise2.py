#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import copy

# import librosa

def normalise2(MFCCs):

    c=copy.deepcopy(MFCCs)

    for i in range(39):
        for j in range(628):          
            c[i,j]=(c[i,j]*20)+800
            if c[i,j]<=0:
                c[i,j]=0
            elif c[i,j]>=1000:
                c[i,j]=1000
            else:
                c[i,j]=c[i,j]/900
            
    nMFCCs=c
            
    return nMFCCs


