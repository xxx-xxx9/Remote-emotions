#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# fornisce una coppia di numeri: lo strumento e la diffusione

import socket
# import time
import random
import numpy as np

def instr(r1,r2,r3,r4):
    
    try:
        server1 = socket.socket()
        server2 = socket.socket()
        host = '127.0.0.1'
        port1 = 3043
        port2 = 3053
        
        server1.connect((host,port1))
        print('server1 connected')
        server2.connect((host,port2))
        print('server2 connected')
        
        c=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        se1=[1,0,0,0,0,0]
        se2=[0,1,0,0,0,0]
        se3=[0,0,1,0,0,0]
        se4=[0,0,0,1,0,0]
        se5=[0,0,0,0,1,0]
        se6=[0,0,0,0,1,0]

        se7=[1,0,1,0,0,0]
        se8=[1,0,0,1,0,0]
        se9=[1,0,0,0,1,0]
        se10=[1,0,0,0,1,0]

        se11=[0,1,1,0,0,0]
        se12=[0,1,0,1,0,0]
        se13=[0,1,0,0,1,0]
        se14=[0,1,0,0,1,0]

        se15=[0,0,1,0,1,0]
        se16=[0,0,1,0,1,0]
        se17=[0,0,0,1,1,0]
        se18=[0,0,0,1,1,0]

        se19=[1,1,0,0,0,0]
        se20=[0,0,1,1,0,0]
        se21=[0,0,0,0,1,0]

        se22=[1,0,1,0,1,0]
        se23=[1,0,1,0,1,0]
        se24=[1,0,0,1,1,0]
        se25=[1,0,0,1,1,0]
        se26=[0,1,1,0,1,0]
        se27=[0,1,1,0,1,0]
        se28=[0,1,0,1,1,0]
        se29=[0,1,0,1,1,0]
        
        ce1=[1,0,0]
        ce2=[0,1,0]
        ce3=[0,0,1]
        
        ce4=[1,1,0]
        ce5=[1,0,1]
        
        ce=[0,0,0]

        se=np.matrix([se1,se2,se3,se4,se5,se6,se7,se8,se9,se10,se11,se12,se13,se14,se15,se16,se17,se18,se19,se20,se21,se22,se23,se24,se25,se26,se27,se28,se29])
        
        
        st=random.randint(0,4)
        
    # st=0 -> altoparlanti (2 o 4)
    # st=1 -> fd
    # st=2 ->
    # st=3 -> ffd + altoparlanti (2)
    # st=4 -> fd + altoparlanti (2)

        if st==0:
            ce=ce1
    #         diff=random.randint(0,1)
            alt=random.randint(0,1)
            if alt==0:
                c[3]=c[4]=1 # altoparlanti 1 e 2
            else:
                c[3]=c[4]=c[5]=c[6]=1 # tutti gli altoparlanti
        elif st==3:
            ce=ce3
            c[3]=c[4]=1
            diff=random.randint(0,28)
            for i in range (6):
                c[i+7]=se.item((diff,i)) 
        elif st==4:
            ce=ce4
            c[3]=c[4]=1
            diff=random.randint(0,28)
            for i in range (6):
                c[i+7]=se.item((diff,i)) 
            
        elif st==1:
            ce=ce2
            diff=random.randint(0,28)
    #         print(diff)
            for i in range (6):
                c[i+7]=se.item((diff,i))
        else: 
            ce=ce3
            diff=random.randint(0,28)
    #         print(diff)
            for i in range (6):
                c[i+7]=se.item((diff,i))
    #         print(se[diff])
        c[0]=ce[0]
        c[1]=ce[1]
        c[2]=ce[2]
        
    # aggiungiamo lunghezze random dei suoni per rs, fd e ffd
        l1=random.randint(0,2)
        l2=random.randint(0,2)
        l3=random.randint(0,2)
    #     print('lunghezze suoni', l1, l2, l3)
            
    #     c[st]=1
        
        s=' '
        s=str(c[0])+str(c[1])+str(c[2])+str(c[3])+str(c[4])+str(c[5])+str(c[6])+str(c[7])+str(c[8])+str(c[9])+str(c[10])+str(c[11])+str(c[12])+str(l1)+str(l2)+str(l3)

    #     s='1110000000001'
    #     s='0100000100000'
        
        msg=str(s)
        msg=server1.send(s.encode('utf-8'))
        
    # frequenze in base alle r1, r2, r3 ed r4

        c1=str(r1+10)+' '+str(r2+10)+' '+str(r3+10)+' '+str(r4+10)+' '
        msg=server2.send(c1.encode('utf-8'))

    #     c1=' '
    #     cc1=str(r1+10)
    #     c2=' '
    #     cc2=str(r2+10)
    #     c3=' '
    #     cc3=str(r3+10)
    #     c4=' '
    #     cc4=str(r4+10)
    #     msg=server2.send(c1.encode('utf-8'))
    #     msg=server2.send(cc1.encode('utf-8'))
    #     msg=server2.send(c2.encode('utf-8'))
    #     msg=server2.send(cc2.encode('utf-8'))
    #     msg=server2.send(c3.encode('utf-8'))
    #     msg=server2.send(cc3.encode('utf-8'))
    #     msg=server2.send(c4.encode('utf-8'))
    #     msg=server2.send(cc4.encode('utf-8'))
        print(c1)
        
        print(s)
    #     time.sleep(0.01)
        
        server1.shutdown(socket.SHUT_RDWR)
        server2.shutdown(socket.SHUT_RDWR)

        server1.close()
        server2.close()
        
        return s

    except:
        print('instr: failed to connect to Pd patch')
        return ' '
