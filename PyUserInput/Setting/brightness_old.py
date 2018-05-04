#!/usr/bin/python

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m=PyMouse()
k=PyKeyboard()

x_dim, y_dim=m.screen_size()
x_pos=x_dim/100
y_pos=y_dim/100

#Settings
m.move(150, 140)
time.sleep(2)

#Brightness Plus
m.move(480, 250)
time.sleep(2)

#Brightness Minus
m.move(565, 250)
time.sleep(1)

#Apply Brightness Changes
m.move(400, 275)


