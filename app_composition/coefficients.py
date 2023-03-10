#!/usr/bin/env python
# coding: utf-8

# In[5]:

import librosa
import numpy as np
from mfccs import *


def coefficients(MFCCs, r1, r2, r3, r4, i, k):
    coeff1=MFCCs[r1][i+k]
    coeff2=MFCCs[r2][i+k]
    coeff3=MFCCs[r3][i+k]
    coeff4=MFCCs[r4][i+k]

    coeff1=int((coeff1*20)+800)
    coeff2=int((coeff2*20)+800)
    coeff3=int((coeff3*20)+800)
    coeff4=int((coeff4*20)+800)
    
    if coeff1<=0:
        coeff1=100
    elif coeff1>1000:
        coeff1=1000
    else:      
        coeff1=coeff1

    if coeff2<=0:
        coeff2=100
    elif coeff2>1000:
        coeff2=1000
    else:      
        coeff2=coeff2
        
    if coeff3<=0:
        coeff3=100
    elif coeff3>1000:
        coeff3=1000
    else:      
        coeff3=coeff3
        
    if coeff4<=0:
        coeff4=100
    elif coeff4>1000:
        coeff4=1000
    else:      
        coeff4=coeff4

    c1 = str(coeff1)
    c2 = str(coeff2)
    c3 = str(coeff3)
    c4 = str(coeff4)

    print(c3)
    c1=c1+' '
    c2=c2+' '
    c3=c3+' '
    c4=c4+' '
    return c1, c2, c3, c4


