#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import librosa

def mfccs(filename):
    
    count= 0
    for i in range(4):  
        signal, sr = librosa.load(filename, 44100)
        signal = signal[count:count+40000]
        count+=40000
        MFCCs = librosa.feature.mfcc(signal, n_mfcc=39, hop_length=256, n_fft=2048)
        if i==0:
            a=MFCCs
            aa = a.T.tolist()
            aaa = np.array(aa)
            aaaa = aaa[..., np.newaxis]
            aaaaa =aaaa[np.newaxis, ...]
            
        if i==1:
            b=MFCCs
            bb = b.T.tolist()
            bbb = np.array(bb)
            bbbb = bbb[..., np.newaxis]
            bbbbb =bbbb[np.newaxis, ...]
            
        if i==2:
            c=MFCCs
            cc = c.T.tolist()
            ccc = np.array(cc)
            cccc = ccc[..., np.newaxis]
            ccccc =cccc[np.newaxis, ...]
            
        if i==3:
            d=MFCCs
            dd = d.T.tolist()
            ddd = np.array(dd)
            dddd = ddd[..., np.newaxis]
            ddddd =dddd[np.newaxis, ...]
            
            
    MFCCs=np.concatenate((a,b,c,d),axis=1)
            
    return aaaaa, bbbbb, ccccc, ddddd, MFCCs


