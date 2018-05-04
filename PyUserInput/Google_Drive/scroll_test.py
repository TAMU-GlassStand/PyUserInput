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

#Google Drive
m.move(x_pos*9, y_pos*50)
time.sleep(1)

#PDF Selection
#x=x_pos*23
#y starts at y_pos*22 and increases by x5

scale=4

m.move(x_pdf, y_pdf)
time.sleep(1)
m.move(x_pdf, y_pdf+1*scale)
time.sleep(1)
m.move(x_pdf, y_pdf+2*scale)
time.sleep(1)
m.move(x_pdf, y_pdf+3*scale)
time.sleep(1)
m.move(x_pdf, y_pdf+4*scale)
time.sleep(1)
m.move(x_pdf, y_pdf+5*scale)
time.sleep(1)
m.move(x_pdf, y_pdf+6*scale)
time.sleep(1)
m.move(x_pdf, y_pdf+7*scale)
time.sleep(1)
m.move(x_pdf, y_pdf+8*scale)
time.sleep(1)
m.move(x_pdf, y_pdf+9*scale)
time.sleep(1)
m.move(x_pdf, y_pdf+10*scale)
time.sleep(1)