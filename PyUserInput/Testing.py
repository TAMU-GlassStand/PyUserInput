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
m.move(150, y_pos*30)
m.click(150, y_pos*30, 1)
time.sleep(10)

#Google Drive
m.move(150, y_pos*55)
m.click(150, y_pos*55, 1)
time.sleep(10)

#Removable Storage
m.move(150, y_pos*90)
m.click(150, y_pos*90, 1)
