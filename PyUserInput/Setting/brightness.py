#!/usr/bin/python

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m=PyMouse()
k=PyKeyboard()

x_dim, y_dim=m.screen_size()
print "X Dim: ", x_dim, " Y Dim: ", y_dim
x_pos=x_dim/100
y_pos=y_dim/100

#Settings
m.move(x_pos*9, y_pos*15)
time.sleep(1)

#Brightness Plus
m.move(x_pos*30, y_pos*21.25)
time.sleep(1)

#Brightness Minus
m.move(x_pos*35.25, y_pos*21.25)
time.sleep(1)

#Apply Brightness Changes
m.move(x_pos*26, y_pos*22.5)
