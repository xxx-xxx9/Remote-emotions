#!/usr/bin/env python
# coding: utf-8

# In[5]:


import keras
from keras.models import load_model
import librosa
import numpy as np
from mfccs import *


def pred_audio(a,b,c,d):
    model_pre = load_model('my_model.h5')
    
    pred_a = model_pre.predict(a)
    pred_b = model_pre.predict(b)
    pred_c = model_pre.predict(c)
    pred_d = model_pre.predict(d)

    max1 = np.argmax(pred_a)
    max2 = np.argmax(pred_b)
    max3 = np.argmax(pred_c)
    max4 = np.argmax(pred_d)
    
    m = np.array(['angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'surprised'])

    result = (m[max1], m[max2], m[max3], m[max4]) 
        
    return (result)