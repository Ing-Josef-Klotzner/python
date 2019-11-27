#!/usr/bin/python
# -*- coding: utf-8 -*-
# originally posted in thread http://www.daniweb.com/software-development/python/threads/298190/1282328#post1282328
# color_label needs to be defined global with todays python versions
"""
Created on Mon Jul 17 11:10:18 2017

@author: josef
"""

from __future__ import absolute_import, division, unicode_literals, print_function
from sys import version_info
if version_info.major >= 3:
    from tkinter import *   # python 3.2
elif version_info.major == 2:
    from Tkinter import *   # python 2.7
else:
    print ("what the hell you are running, if not Python 2 or 3 ?  :D")
    
def change(a=0):
    color_label.config(bg = "blue" if a & 1 else "purple")
    color_label.after(400,change, a ^ 1 )
    print ("i am in change",a)

def main():
    global color_label
    win = Tk() 
    win.geometry("500x300")
    win.title('Demonstrating after event')
    color_label = Label(win)
    color_label.pack(expand=YES, fill=BOTH)
    change()
    win.mainloop()
    
if __name__ == '__main__':
    main()