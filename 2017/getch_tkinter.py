#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:00:00 2017

@author: josef
"""
from Tkinter import Tk, Frame

def keyup(event):
    key = event.keysym
    print "Key Released: %s" % key

def keydown(event):
    key = event.keysym
    print "Key Pressed: %s" % key

root = Tk()
frame = Frame(master=root, width=100, height=100)
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
frame.pack()
root.mainloop()