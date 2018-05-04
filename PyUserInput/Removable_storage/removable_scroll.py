#!/usr/bin/python

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m=PyMouse()
k=PyKeyboard()

x_dim, y_dim=m.screen_size()
x_pos=x_dim/100
y_pos=y_dim/100


#Removable Storage
base=10
x_usb=x_pos*25

m.move(x_pos*9, y_pos*80)
#m.click(x_pos*9, y_pos*80, 1)
time.sleep(1)
m.move(x_pos*25, y_pos*10)
#m.click(x_pos*25, y_pos*10, 1)
time.sleep(1)


#Removeable Storage Selection

scale=3.35/2

m.move(x_usb, y_pos*base)
time.sleep(1)
m.move(x_usb, y_pos*(base+1*scale))
time.sleep(1)
m.move(x_usb, y_pos*(base+2*scale))
time.sleep(1)
m.move(x_usb, y_pos*(base+3*scale))
time.sleep(1)
m.move(x_usb, y_pos*(base+4*scale))
time.sleep(1)
m.move(x_usb, y_pos*(base+5*scale))
time.sleep(1)
m.move(x_usb, y_pos*(base+6*scale))
time.sleep(1)
m.move(x_usb, y_pos*(base+7*scale))
time.sleep(1)
m.move(x_usb, y_pos*(base+8*scale))
time.sleep(1)
m.move(x_usb, y_pos*(base+9*scale))
time.sleep(1)
m.move(x_usb, y_pos*(base+10*scale))
time.sleep(1)
