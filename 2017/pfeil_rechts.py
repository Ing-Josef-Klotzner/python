#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 20:37:48 2017

@author: josef
"""
from __future__ import absolute_import, division, unicode_literals, print_function
from sys import version_info
if version_info.major >= 3:
    from tkinter import Tk, Frame   # python 3.2
    from tkinter.messagebox import *
elif version_info.major == 2:
    from Tkinter import Tk, Frame   # python 2.7
    from tkMessageBox import *
else:
    print ("what the hell you are running, if not Python 2 or 3 ?  :D")

def ev_handler(event):
    print ("Taste gedrueckt", repr(event.char)) 
    showinfo ("Taste gedrueckt", repr(event.char)) 

def callback(event):
#    frame.focus_set()
    print ("clicked at", event.x, event.y)

print ("Keine Ahnung warum das auf Keyboardeingabe nicht reagiert, auf Maus aber doch")
 
root = Tk()
frame = Frame(root, width=400, height=400)
#frame.bind("<KeyPress-rightarrow>", ev_handler)
#frame.bind("<KeyPress-space>", ev_handler)
frame.bind("<KeyPress>", ev_handler)
#frame.bind("<KeyPress>", handler)
frame.bind("<Button-1>", callback)
frame.pack()
frame.focus_set()
root.mainloop()