#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from socket import *

import socket
import time

import sys
import select

def spedisci(norm1, norm2, norm3, norm4):
    
    try:
        bufSize = 512
        
        server1 = socket.socket()
        server2 = socket.socket()
        server3 = socket.socket()
        server4 = socket.socket()
        server5 = socket.socket()
        host = ''
        port1 = 3003
        port2 = 3013
        port3 = 3023
        port4 = 3033
        port5 = 3063
        port6 = 3073
        
        s = socket.socket(AF_INET,SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        s.bind((host, port6))
        print('server 3073 connesso')
        
        server1.connect((host,port1))
        print('server1 connected')
        server2.connect((host,port2))
        print('server2 connected')
        server3.connect((host,port3))
        print('server3 connected')
        server4.connect((host,port4))
        print('server4 connected')
        server5.connect((host,port5))
        print('server5 connected')
        
        # check if Pd is already playing something else
        while(True):
            c5=' '
            msg =server5.send(c5.encode('utf-8'))
            udpClientData, _ = s.recvfrom(bufSize)
            msg=str(udpClientData.decode('utf-16'))
            
            m=str(msg)
            print('m',m)
            if m=='Ā':
                break
            time.sleep(1)
        print('uscito dal ciclo while')
        
        # start sending data
        
        for i in range(628):
            c1=' '
            c2=' '
            c3=' '
            c4=' '
            msg =server1.send(c1.encode('utf-8'))
            msg =server2.send(c2.encode('utf-8'))
            msg =server3.send(c3.encode('utf-8'))
            msg =server4.send(c4.encode('utf-8'))
            cc1=format(norm1[i],'.4f')
            cc2=format(norm2[i],'.4f')
            cc3=format(norm3[i],'.4f')
            cc4=format(norm4[i],'.4f')
            c1=str(cc1)
            c2=str(cc2)
            c3=str(cc3)
            c4=str(cc4)

            msg =server1.send(c1.encode('utf-8'))
            msg =server2.send(c2.encode('utf-8'))
            msg =server3.send(c3.encode('utf-8'))
            msg =server4.send(c4.encode('utf-8'))
        
        server1.shutdown(socket.SHUT_RDWR)
        server2.shutdown(socket.SHUT_RDWR)
        server3.shutdown(socket.SHUT_RDWR)
        server4.shutdown(socket.SHUT_RDWR)
        server5.shutdown(socket.SHUT_RDWR)

        server1.close()
        server2.close()
        server3.close()
        server4.close()
        server5.close()

        s.close()
        

    except:
        print('spedisci: failed to connect to Pd patch')
