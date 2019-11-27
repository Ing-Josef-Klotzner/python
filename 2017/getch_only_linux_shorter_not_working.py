#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function
"""
Created on Tue Jul 18 15:42:02 2017

@author: josef
"""
from os import system
import sys
if sys.version_info.major < 3:
    import thread as _thread
else:
    import _thread
from time import sleep

def getch():
    global char    
    char = str(system("bash -c read -n 1"))
     
def inkey():
    import tty, termios
    global char
    fd=sys.stdin.fileno()
    remember_attributes=termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())
    char=sys.stdin.read(1) # wir lesen nur einzelne zeichen
    termios.tcsetattr(fd,termios.TCSADRAIN, remember_attributes)
    
def main():
    global char
    char = None
    _thread.start_new_thread(getch, ())

    while True:
        print ("getch: ", getch())
        if char is not None:
            try:
                print("Key pressed is " + char)
            except UnicodeDecodeError:
                print("character can not be decoded, sorry!")
                char = None
            _thread.start_new_thread(getch, ())
            if char == 'q' or char == '\x1b':  # x1b is ESC
                exit()
            char = None
        print("Program is running")
        sleep(1)

if __name__ == "__main__":
    main()
