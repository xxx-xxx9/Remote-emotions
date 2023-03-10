# Complete project details at https://RandomNerdTutorials.com
try:
    import usocket as socket
except:
    import usocket as socket

from machine import Pin

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid='Linkem_FFF533'
password='ct6esaqf'

station=network.WLAN(network.STA_IF)
station.active(True)
# station.ifconfig((‘192.168.1.69', '255.255.255.0', '192.168.1.1', '192.168.1.1’))
station.connect(ssid,password)

while station.isconnected()==False:
    pass

print('network config:', station.ifconfig())

led=Pin(2, Pin.OUT)

import webrepl
webrepl.start()
