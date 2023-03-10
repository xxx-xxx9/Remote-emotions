#!/usr/bin/env python
# coding: utf-8

# In[5]:

import librosa
import numpy as np
from mfccs import *


def transf(MFCCs, MFCCsF):
    steps=10
    diff=abs((MFCCs-MFCCsF)/steps)
    MFCCsTOT=MFCCs
    for i in range(steps):
        MFCCs1=MFCCs+(diff*(i+1))
        MFCCsTOT=np.concatenate((MFCCsTOT,MFCCs1),axis=1)
    MFCCsTOT=np.concatenate((MFCCsTOT,MFCCsF),axis=1)

    return MFCCsTOT


