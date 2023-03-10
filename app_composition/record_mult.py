#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyaudio
import wave
import numpy as np
import math

def record_mult(flnm, device):

    # the file name output you want to record into
    filename = flnm
    # from which device to record (see sounddevice.query_devices() to know which number)
    input_device_index = device
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    FORMAT = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 5
    # 44100 samples per second
    #sample_rate = 44100
    sample_rate = 16000
    record_seconds = 4
    # initialize PyAudio object
    p = pyaudio.PyAudio()
    p.get_default_input_device_info()
    
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    input_device_index=input_device_index,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(math.ceil(sample_rate * record_seconds / chunk))):
        data = stream.read(chunk)
        frames.append(data)
    print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()
    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(sample_rate)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()
