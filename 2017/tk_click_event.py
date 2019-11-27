#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function
"""
Created on Fri Jul 21 19:35:15 2017

@author: josef
"""
from sys import version_info
if version_info.major >= 3:
    from tkinter import Tk, Frame   # python 3.2
elif version_info.major == 2:
    from Tkinter import Tk, Frame   # python 2.7
else:
    print ("what the hell you are running, if not Python 2 or 3 ?  :D")

root = Tk()

def callback(event):
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()