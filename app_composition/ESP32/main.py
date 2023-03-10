import socket
import time
import machine
#import network
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.bind (('192.168.1.151', 1239))
s.listen(5)
print('listening...')
confirm='end'
p2 = machine.Pin(2)
pwm2 = machine.PWM(p2)
pwm2.freq(500)
while True:
   client, address = s.accept()
   print('got address')
   client.send(str.encode(confirm))
   print('confirmation sent')
   msg = client.recv(32)
   full_msg=msg.decode('utf-8')
   z=0
   while len(msg)>0:
      z=z+1
      print('in the while loop')
#       client.send(str.encode(confirm))
#       print('confirmation2 sent')
      msg = client.recv(32)
      full_msg=full_msg+msg.decode('utf-8')
   print(z)
   a=full_msg.split(' ')
   print(a)
   for i in a:
      print('in the for loop')
      if i!='':
         b=int(i)
         pwm2.duty(b)
         print(b)
         time.sleep(0.007)
      else:
         break
   b=100
   pwm2.duty(b)
   print(b)
   client.send(str.encode(confirm))
   client.close()
