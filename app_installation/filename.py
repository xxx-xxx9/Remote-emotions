#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import random
import os
import glob


def filename(k,result):
    
    i = ['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

    c = ['calm', 'angry', 'surprised', 'neutral', 'sad', 'fearful', 'happy', 'disgust']

    n = ['fearful','neutral', 'sad', 'angry', 'surprised', 'calm', 'disgust', 'happy']

    s = ['calm', 'calm', 'calm', 'calm', 'calm', 'calm', 'calm', 'calm']
    
    if k==0:
        result2=result
    elif k==1:
        result2= [c[i.index(result[0])],c[i.index(result[1])],c[i.index(result[2])],c[i.index(result[3])]]
    elif k==2:
        result2= [n[i.index(result[0])],n[i.index(result[1])],n[i.index(result[2])],n[i.index(result[3])]]
    elif k==3:
        result2= [s[i.index(result[0])],s[i.index(result[1])],s[i.index(result[2])],s[i.index(result[3])]]
    
    res = result2[random.randint(0,3)]
    
    #file=os.listdir(res+'/')
    file = glob.glob(res + '/*.wav') # avoid .DS_Store ie. from messing things up
    x=len(file)-1
    y=random.randint(1,x)
    
    fn=file[y]
    print(fn)
    
    return fn