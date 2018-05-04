#!/usr/bin/python

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m=PyMouse()
k=PyKeyboard()

x_dim, y_dim=m.screen_size()
x_pos=x_dim/100
y_pos=y_dim/100

#Google Drive
m.move(x_pos*9, y_pos*55)
#m.click(x_pos*9, y_pos*55, 1)
time.sleep(10)

#PDF Selection
m.move(
