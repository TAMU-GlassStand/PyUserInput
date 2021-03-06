#!/usr/bin/python

from smbus2 import SMBus
from smbus2 import SMBusWrapper
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

#PyUserInput

m=PyMouse()
k=PyKeyboard()
x_dim, y_dim=m.screen_size()
y_pos=y_dim/100
x_pos=x_dim/100


#SMBus

busnum=1
address=0x0a
offset=0x00
data0=[0, 0, 0, 0, 0, 0]
bus=SMBus(busnum)
b=bus.read_byte_data(address,offset)
print b


prev = -1
touch = -1
while 1:
	
	bus.write_i2c_block_data(0x0a, 0x00, data0) #Write which sensor element looking for (buttons)
	read=bus.read_i2c_block_data(address, 0, 6)
	read1=read[0] #Byte 1
	read2=read[1] #Byte 2
	read3=read[2] #Byte 3 (Changes based on button being pressed)
	read4=read[3] #Byte 4
	read5=read[4] #Byte 5
	read6=read[5] #Byte 6 (Changes when touch/proximity is detected)

	touchbit=read6 & 0x01

	#if read6>=1 and read6!=12 and read3!=prev and touch==-1:
	if touchbit==1 and read3!=prev:
		prev=read3
		touchbit=-1
		if read3==0:
			print"Button 1 was pressed"
			m.move(20, y_pos*25)
		elif read3==1:
			print"Button 2 was pressed"
			m.move(20, y_pos*50)
		elif read3==2:
			print"Button 3 was pressed"
			m.move(20, y_pos*75)
		elif read3==3:
			print"Button 4 was pressed"
			m.move(x_pos*50, y_pos*25)
		elif read3==4:
			print"Button 5 was pressed"
			m.move(x_pos*50, y_pos*50)
		elif read3==5:
			print"Button 6 was pressed"
			m.move(x_pos*50, y_pos*75)
		elif read3==6:
			print"Button 7 was pressed"
			m.move(x_pos*80, y_pos*25)
		elif read3==7:
			print"Button 8 was pressed"
			m.move(x_pos*80, y_pos*50)
		elif read3==8:
			print"Button 9 was pressed"
			m.move(x_pos*80, y_pos*75)

	if read6==0:
		touch=-1
		prev=-1
		read3=-1