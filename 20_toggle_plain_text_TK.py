#  toggle plain text color TK
# -*- coding: iso-8859-15 -*-
# change the background/foreground color of a button
# askcolor() returns the selected color in two forms
# one is rgb = (red,green,blue) for blue = (0,0,255) for red = (255, 0, 0)
# the other is a hex number for blue = #0000ff for red = #ff0000
# tested with Python 24 vegaseat 05jul2005
 
from Tkinter import *
from tkColorChooser import askcolor # brings up the color dialog box
 
# the toggle flag
flag1 = True
 
def setColor():
	# flag1 has to be global, not local (the default)
	global flag1
	(rgb, hexval) = askcolor()
	if hexval:
		print rgb, hexval # testing
		# toggle between bg and fg
		if flag1:
			push1.config(bg=hexval, text='Click to set Foreground Color')
			flag1 = False
		else:
			push1.config(fg=hexval, text='Click to set Background Color')
			flag1 = True
 
 
#create the form
form1 = Tk()
# set the form's title
form1.title('Change Button Colors')
# create a button
push1 = Button(form1, text='Click to set Background Color', command=setColor)
# configure the button's text
push1.config(height=3, font=('times', 20, 'bold'))
# pack the button into the frame
push1.pack(expand=YES, fill=BOTH)
# run the event-loop/program ...
form1.mainloop()