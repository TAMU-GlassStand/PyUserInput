#!/usr/bin/python

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m=PyMouse()
k=PyKeyboard()

x_dim, y_dim=m.screen_size()
print"X dim: ", x_dim, "Y dim: ", y_dim
x_pos=x_dim/100
y_pos=y_dim/100

x_pdf=x_pos*26
y_pdf=y_pos*6
base=6

#Google Drive
m.move(x_pos*9, y_pos*45)
time.sleep(1)

#PDF Selection
#x=x_pos*23
#y starts at y_pos*22 and increases by x5

scale=3.65

m.move(x_pdf, y_pdf)
time.sleep(1)
m.move(x_pdf, y_pos*(base+1*scale))
time.sleep(1)
m.move(x_pdf, y_pos*(base+2*scale))
time.sleep(1)
m.move(x_pdf, y_pos*(base+3*scale))
time.sleep(1)
m.move(x_pdf, y_pos*(base+4*scale))
time.sleep(1)
m.move(x_pdf, y_pos*(base+5*scale))
time.sleep(1)
m.move(x_pdf, y_pos*(base+6*scale))
time.sleep(1)
m.move(x_pdf, y_pos*(base+7*scale))
time.sleep(1)
m.move(x_pdf, y_pos*(base+8*scale))
time.sleep(1)
m.move(x_pdf, y_pos*(base+9*scale))
time.sleep(1)
m.move(x_pdf, y_pos*(base+10*scale))
time.sleep(1)
