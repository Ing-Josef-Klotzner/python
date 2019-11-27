#! /usr/bin/env python
#  tkColorChooser - akscolor
# -*- coding: iso-8859-15 -*-
print ("use python 2.7 under linux to run this")
from Tkinter import * # python 2.7
#from tkinter import *   # python 3.2
from tkColorChooser import askcolor
def callback():
    result = askcolor(color="#6A9662",
                      title = "Josef's Colour Chooser")
    print (result)

root = Tk()
Button(root,
       text='Choose Color',
       fg="darkgreen",
       command=callback).pack(side=LEFT, padx=10)
Button(text='Quit',
       command=root.quit,
       fg="red").pack(side=LEFT, padx=10)
mainloop()
