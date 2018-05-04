#!/usr/bin/python

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m=PyMouse()
k=PyKeyboard()

x_dim, y_dim=m.screen_size()
y_pos=y_dim/100
x_pos=x_dim/100

m.move(20, y_pos*15)
time.sleep(1)
m.move(20, y_pos*50)



