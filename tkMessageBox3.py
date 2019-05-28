#!/usr/bin/python
#  tkMessageBox2
# -*- coding: iso-8859-15 -*-
print ("use Python 2.7 to get it work")
from sys import version_info
if version_info.major == 3:
    from tkinter import *   # python 3.2
elif version_info.major == 2:
    from Tkinter import *   # python 2.7
else:
    print ("what the hell you are running?  :D")
from tkMessageBox import *
top = Tk()
def hello():
   showinfo("Say Hello", "why should i say hello, if you buster only want me to say that, because you think you are the Boss?")

B1 = Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
