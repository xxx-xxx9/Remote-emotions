#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import shutil
import os

def salva_audio(flnm, result):
    o=os.getcwd()
    res=set(result)
    m=0
    
    for i in range(len(res)):
        lst=list(res)
        r=lst[i]
        
        src = o + '/' + flnm
        
        file=os.listdir(r+'/')

        for i in range(len(file)-1):
            filetr=file[i+1].split('.')[0]
            file[i]=int(filetr)
        file[len(file)-1]=0   
        m=max(file)
        nnm=m+1
        nflnm=str(nnm)+'.wav'
        
        dst = o + '/' + r + '/' + nflnm      
        
        shutil.copyfile(src, dst)