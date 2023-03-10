#!/usr/bin/env python
# coding: utf-8

# In[5]:

import librosa
import numpy as np
from mfccs import *
from silence import *


def repeat(j):
    
    if j==0:
        l=3
        z=26
        print('blocco in space',j)
    elif j==1:
        l=1
        z=21
        print('blocco in space',j)
    elif j==2:
        l=1
        z=8
        print('blocco in space',j)
    elif j==3:
        l=3
        z=8
        print('blocco in space',j)
    elif j==4:
        l=2
        z=7
        print('blocco in space',j)
    elif j==5:
        l=3
        print('blocco in space',j)
        z=1
        
    return l, z


