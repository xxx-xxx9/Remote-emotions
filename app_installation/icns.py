#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import sqlite3
import random
import numpy as np

def icns():
    
    lista= []
#     freq =[4,4,3,3] # caricare da database!!
    lista=[0,1,2,3]
    
    # richiama il database icns_db.db
    conn =sqlite3.connect('icns_db.db')
    c = conn.cursor()

    c.execute("SELECT * FROM action ORDER BY id DESC")

    conn.commit()
    tutto=c.fetchall()
    conn.close()
    
    ad = np.sum(tutto, axis = 0)
    
    freq=ad[1:5]

    n=max(freq)
    k=np.argmax(freq)
#     print(k)

    if freq[0]==freq[1]==freq[2]==freq[3]:
        k=random.choice(lista)
        print('uguali')
        
    else:
        freq[k]=freq[k]+1
        del lista[k]
        j=random.choice(lista)        
        k=j
        
    freq=[0,0,0,0]
    freq[k]=1
    
    conn =sqlite3.connect('icns_db.db')
    c = conn.cursor()
    c.execute("SELECT * FROM action ORDER BY id")
    conn.commit()

    data=[(freq[0],freq[1],freq[2],freq[3])]
    conn.executemany("INSERT INTO action (I,C,N,S) VALUES (?,?,?,?)", data)
    c.execute("SELECT * FROM action ORDER BY id DESC")
    conn.commit()
    conn.close()
            
    return k


