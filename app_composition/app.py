from flask import Flask, render_template, request, url_for, redirect
from record import *
from pred_audio import *
from transf import *
from mfccs import *
from coefficients import *
from space import *
from repeat import *
from record_mult import *
from save_wav_channel import *
import numpy as np
import time
import math
import requests
import random
import socket
import os
import copy
from _thread import *


app = Flask(__name__)

# for the audio interface and microphone set up
recording_device=5
mic_installation=1

c1 = '100'
c2 = '100'
c3 = '100'
c4 = '100'
global host1, host2, host3, host4, port, SS
port=1239

host1='192.168.43.192'
host2='192.168.43.236'
host3='192.168.43.138'
host4='192.168.43.126'




SS=0

@app.route('/', methods=['GET', 'POST'])
def menu():
    if request.method == 'GET':
        return(render_template('index.html'))

    if request.method == 'POST':
        
# ------------------------------ RECORD -----------------------------------

        if request.form.get("submit_a"):
            
            ClientMultiSocket = socket.socket()
            CMS2 = socket.socket()
            CMS3 = socket.socket()
            CMS4 = socket.socket()
            
            print('waiting for connection...')
            try:
                ClientMultiSocket.connect((host1, port))
                print('host1 connesso', host1)
                CMS2.connect((host2, port))
                print('host2 connesso', host2)
                CMS3.connect((host3, port))
                print('host3 connesso', host3)
                CMS4.connect((host4, port))
                print('host4 connesso', host4)
            except socket.error as e:
                print(str(e))


            record_mult('f0.wav', recording_device)
            wav = wave.open('f0.wav')
            save_wav_channel('recorded.wav', wav, mic_installation - 1)
            
            a, b, c, d, MFCCs = mfccs('recorded.wav')
            result = pred_audio(a, b, c, d)
            r1 = random.randint(0,16)
            r2 = random.randint(8,24)
            r3 = random.randint(16,32)
            r4 = random.randint(24,38)
            k=0
            for i in range(628):
                c1, c2, c3, c4 = coefficients(MFCCs, r1, r2, r3, r4, i, k)
                print(c1)
                print(c2)

                ClientMultiSocket.send(str.encode(c1))
                print('c2')
                CMS2.send(str.encode(c2))
                CMS3.send(str.encode(c3))
                CMS4.send(str.encode(c4))
            ClientMultiSocket.send(str.encode('a'))
            CMS2.send(str.encode('a'))
            CMS3.send(str.encode('a'))
            CMS4.send(str.encode('a'))

            ClientMultiSocket.close()
            CMS2.close()
            CMS3.close()
            CMS4.close()

#       ---------------- TRANSFORM -------------------
           
        elif request.form.get("submit_b"):           

            a, b, c, d, MFCCs = mfccs('recorded.wav')
            e, f, g, h, MFCCsF = mfccs('target.wav')
            MFCCs = transf(MFCCs, MFCCsF)
            result = pred_audio(a, b, c, d)

            r1 = random.randint(0,16)
            r2 = random.randint(8,24)
            r3 = random.randint(16,32)
            r4 = random.randint(24,38)
            
            for j in range(10):
                k = j*628
                
                ClientMultiSocket = socket.socket()
                CMS2 = socket.socket()
                CMS3 = socket.socket()
                CMS4 = socket.socket()   

                print('waiting for connection...')
                try:
                    ClientMultiSocket.connect((host1, port))
                    CMS2.connect((host2, port))
                    CMS3.connect((host3, port))
                    CMS4.connect((host4, port))
                except socket.error as e:
                    print(str(e))
                
                for i in range(628):
                    c1, c2, c3, c4 = coefficients(MFCCs, r1, r2, r3, r4, i, k)
                    ClientMultiSocket.send(str.encode(c1))
                    CMS2.send(str.encode(c2))
                    CMS3.send(str.encode(c3))
                    CMS4.send(str.encode(c4))
                    
                ClientMultiSocket.send(str.encode('a'))
                CMS2.send(str.encode('a'))
                CMS3.send(str.encode('a'))
                CMS4.send(str.encode('a'))
                
                e=[0,0,0,0]

                while True:
                    print('nel ciclo while')
                    msg1=ClientMultiSocket.recv(32)
                    msg2=CMS2.recv(32)
                    msg3=CMS3.recv(32)
                    msg4=CMS4.recv(32)
                    f_msg1=msg1.decode('utf-8')
                    f_msg2=msg2.decode('utf-8')
                    f_msg3=msg3.decode('utf-8')
                    f_msg4=msg4.decode('utf-8')
                    print(f_msg1)
                    print(f_msg2)
                    print(f_msg3)
                    print(f_msg4)
                    if f_msg1=='end' and e[0]==0:
                        e[0]=1
                    if f_msg2=='end' and e[1]==0:
                        e[1]=1  
                    if f_msg3=='end' and e[2]==0:
                        e[2]=1 
                    if f_msg4=='end' and e[3]==0:
                        e[3]=1 
                    if e[0]==1 and e[1]==1 and e[2]==1 and e[3]==1:                       
                        break
                        
                print('blocco')
                print(j)

                
                ClientMultiSocket.close()
                CMS2.close()
                CMS3.close()
                CMS4.close()

            
#       -------------- RECORD TARGET ----------------------------- 
      
        elif request.form.get("submit_c"):
            coeff1=0

            record_mult('f0.wav', recording_device)
            wav = wave.open('f0.wav')
            save_wav_channel('target.wav', wav, mic_installation - 1)

            a, b, c, d, MFCCs = mfccs('target.wav')
            result = pred_audio(a, b, c, d)
            
# -------------------------------- BORDONE 1 --------------------------------------------

        elif request.form.get("submit_d"):
            a, b, c, d, MFCCs = mfccs('target.wav')
            result = pred_audio(a, b, c, d)
            
            for j in range(32):
                k=0
                r1 = random.randint(0,16)
                r2 = random.randint(8,24)
                r3 = random.randint(16,32)
                r4 = random.randint(24,38)
                
                ClientMultiSocket = socket.socket()
                CMS2 = socket.socket()
                CMS3 = socket.socket()
                CMS4 = socket.socket()

                print('waiting for connection...')
                try:
                    ClientMultiSocket.connect((host1, port))
                    CMS2.connect((host2, port))
                    CMS3.connect((host3, port))
                    CMS4.connect((host4, port))
                except socket.error as e:
                    print(str(e))
                
                print('blocco')
                print(j)
                
                M=copy.deepcopy(MFCCs)
                M=space(M, j, r1, r2, r3, r4)
                
                for i in range(628):
                    c1, c2, c3, c4 = coefficients(M, r1, r2, r3, r4, i, k)
                
                    ClientMultiSocket.send(str.encode(c1))
                    CMS2.send(str.encode(c2))
                    CMS3.send(str.encode(c3))
                    CMS4.send(str.encode(c4))


                ClientMultiSocket.send(str.encode('a'))
                CMS2.send(str.encode('a'))
                CMS3.send(str.encode('a'))
                CMS4.send(str.encode('a'))

                
                e=[0,0,0,0]
        

                while True:
                    print('nel ciclo while')
                    msg1=ClientMultiSocket.recv(32)
                    print('nel ciclo while 1')
                    msg2=CMS2.recv(32)
                    print('nel ciclo while 2')
                    msg3=CMS3.recv(32)
                    print('nel ciclo while 3')
                    msg4=CMS4.recv(32)
                    print('nel ciclo while 4')
                    f_msg1=msg1.decode('utf-8')
                    f_msg2=msg2.decode('utf-8')
                    f_msg3=msg3.decode('utf-8')
                    f_msg4=msg4.decode('utf-8')
                    print(f_msg1)
                    print(f_msg2)
                    print(f_msg3)
                    print(f_msg4)
                    if f_msg1=='end' and e[0]==0:
                        e[0]=1
                    if f_msg2=='end' and e[1]==0:
                        e[1]=1  
                    if f_msg3=='end' and e[2]==0:
                        e[2]=1 
                    if f_msg4=='end' and e[3]==0:
                        e[3]=1
                    if e[0]==1 and e[1]==1 and e[2]==1 and e[3]==1:
                        break
                
                ClientMultiSocket.close()
                CMS2.close()
                CMS3.close()
                CMS4.close()


# -------------------------------- BORDONE 2 --------------------------------------------


        elif request.form.get("submit_e"):
        
            for j in range(6):
                
                record_mult('f0.wav', recording_device)
                wav = wave.open('f0.wav')
                save_wav_channel('recorded.wav', wav, mic_installation - 1)
                
                a, b, c, d, MFCCs = mfccs('recorded.wav')
                result = pred_audio(a, b, c, d)
                
                k=0
                r1 = random.randint(0,16)
                r2 = random.randint(8,24)
                r3 = random.randint(16,32)
                r4 = random.randint(24,38)
                
                ind=[r1,r2,r3,r4]
                
                l, z =repeat(j)
                for ii in range(l):
                    M=copy.deepcopy(MFCCs)
                    
                    for jj in range(ii+1):
                        M=silence(M,ind[3-jj])
                    
                    ClientMultiSocket = socket.socket()
                    CMS2 = socket.socket()
                    CMS3 = socket.socket()
                    CMS4 = socket.socket()

                    print('waiting for connection...')
                    try:
                        ClientMultiSocket.connect((host1, port))
                        CMS2.connect((host2, port))
                        CMS3.connect((host3, port))
                        CMS4.connect((host4, port))
                    except socket.error as e:
                        print(str(e))

                    print('blocco')
                    print(j)
                    
                    for i in range(628):
                        c1, c2, c3, c4 = coefficients(M, r1, r2, r3, r4, i, k)

                        ClientMultiSocket.send(str.encode(c1))
                        CMS2.send(str.encode(c2))
                        CMS3.send(str.encode(c3))
                        CMS4.send(str.encode(c4))
                
    
                    ClientMultiSocket.send(str.encode('a'))
                    CMS2.send(str.encode('a'))
                    CMS3.send(str.encode('a'))
                    CMS4.send(str.encode('a'))
    
                    e=[0,0,0,0]

                    while True:
                        print('nel ciclo while')
                        msg1=ClientMultiSocket.recv(32)
                        print('nel ciclo while 1')
                        msg2=CMS2.recv(32)
                        print('nel ciclo while 2')
                        msg3=CMS3.recv(32)
                        print('nel ciclo while 3')
                        msg4=CMS4.recv(32)
                        print('nel ciclo while 4')
                        f_msg1=msg1.decode('utf-8')
                        f_msg2=msg2.decode('utf-8')
                        f_msg3=msg3.decode('utf-8')
                        f_msg4=msg4.decode('utf-8')
                        print(f_msg1)
                        print(f_msg2)
                        print(f_msg3)
                        print(f_msg4)
                        if f_msg1=='end' and e[0]==0:
                            e[0]=1
                        if f_msg2=='end' and e[1]==0:
                            e[1]=1  
                        if f_msg3=='end' and e[2]==0:
                            e[2]=1
                        if f_msg4=='end' and e[3]==0:
                            e[3]=1
                        if e[0]==1 and e[1]==1 and e[2]==1 and e[3]==1:
                            break

                    ClientMultiSocket.close()
                    CMS2.close()
                    CMS3.close()
                    CMS4.close()
            
                for jj in range(z):
                    SS=z-jj
                    print(SS)
                    time.sleep(1)
            
    return render_template('index.html', result= result, MFCCs=MFCCs) 

    
if __name__ == '__main__':
    app.run(debug= True)
