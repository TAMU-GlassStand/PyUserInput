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
m.click(x_pos*9, y_pos*45)
time.sleep(1)

#PDF Selection
#x=x_pos*23
#y starts at y_pos*22 and increases by x5

scale=3.65

# 3 Tabs to move to first element
k.tap_key(k.tab_key, n=3)
time.sleep(2)

x=0

for x in range(0, 5):
	k.tap_key(k.tab_key, n=2)
	x=x+1
	time.sleep(2)


y=0
for y in range(0, 5):
	k.press_key(k.shift_key)
	k.tap_key(k.tab_key)
	k.tap_key(k.tab_key)
	k.release_key(k.shift_key)
	y=y+1
	time.sleep(2)
