#!/usr/bin/env python
# coding: utf-8

# In[5]:

import librosa
import numpy as np
from mfccs import *
from silence import *


def space(M, j, r1, r2, r3, r4):
    
    if j==4 or j==8:
        M=silence(M,r2)
        M=silence(M,r3)
        M=silence(M,r4)
        print('blocco in space',j)
    elif j==1 or j==22 or j==24 or j==26:
        M=silence(M,r1)
        M=silence(M,r3)
        M=silence(M,r4)
        print('blocco in space',j)
    elif j==2 or j==6 or j==15 or j==17 or j==19:
        M=silence(M,r2)
        M=silence(M,r1)
        M=silence(M,r4)
        print('blocco in space',j)
    elif j==3 or j==23 or j==25:
        M=silence(M,r2)
        M=silence(M,r3)
        M=silence(M,r1)
        print('blocco in space',j)
    elif j==9 or j==11 or j==28:
        M=silence(M,r3)
        M=silence(M,r4)
        print('blocco in space',j)
    elif j==10 or j==12 or j==29:
        M=silence(M,r2)
        M=silence(M,r1) 
        print('blocco in space',j)
    elif j==16 or j==18:
        M=silence(M,r3)
        print('blocco in space',j)
    elif j==5:
        M=silence(M,r3)
        M=silence(M,r1)
        print('blocco in space',j)
    elif j==7 or j==27:
        M=silence(M,r3)
        M=silence(M,r2)
        print('blocco in space',j)
    elif j==0 or j==13 or j==14 or j==20 or j==21 or j==30 or j==31:
        M=M
        print('blocco in space',j)
        
    return M


