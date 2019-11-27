#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#  tk__menu
from sys import version_info
if version_info.major == 3:
    from tkinter import *   # python 3.2
elif version_info.major == 2:
    from Tkinter import *   # python 2.7
else:
    print ("what the hell you are running?  :D")
try:
    from tkinter.filedialog import askopenfilename
except ImportError:
    from tkFileDialog   import askopenfilename


def NewFile():
    print ("New File!")
def OpenFile():
    name = askopenfilename()
    print (name)
def About():
    print ("This is a simple example of a menu")
    print("python version ",version_info.major)
    
    
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
