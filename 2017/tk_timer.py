#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Thu Aug 17 17:57:00 2017

@author: josef
"""

''' tk_counter_down101.py
count down seconds from a given minute value
using the Tkinter GUI toolkit that comes with Python
tested with Python27 and Python33
'''
try:
    # Python2
    import Tkinter as tk

except ImportError:
    # Python3
    import tkinter as tk

import time
import os
import subprocess

def count_down():
    # counter loop - NOT precise!
    starttime=time.time()
    for t in range(counter, -100, -1):
        # format as 2 digit integers, fills with zero to the left
        # divmod() gives minutes, seconds
        hr, sc = t // 3600, t % 3600
        mn, sc = sc // 60, sc % 60
#        hr, sc = divmod(t, 3600)
#        mn, sc = divmod(sc, 60)
        sf = "{:02d}:{:02d}:{:02d}".format(hr,mn,sc)
        #print(sf)  # test
        time_str.set(sf)
        root.update()
        # delay one second
        time.sleep(1)
        print(t)
    print("realtime: "+str(time.time()-starttime))
    subprocess.call(["shutdown", "-k", "now"])
    #os.system("shutdown -k now")

def simple_count_down():
    import os
    hours = int(input("Eingabe Stunden: "))
    minutes = int(input("Eingabe Minuten: "))
    sec = int(input("Eingabe Sekunden: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    counter=hours*3600+minutes*60+sec
    mins=int(counter/60)
    hr=int(mins/60)
    while counter > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        hr, sc = divmod(counter, 3600)
        mn, sc = divmod(sc, 60)
        print ("##########################################")
        print("")
        print ("  %d Stunden, %d Minuten and %d Sekunden" % (hr, mn, sc))
        print("")
        print ("##########################################")
        counter-=1
        mins=int(counter/60)
        hr=int(mins/60)
        time.sleep(1)
    else:
        print("Times up!")

if __name__ == '__main__':
#    i=3
    #def main():
    print("run this as root being able to shutdown in grafic mode")
    simple = int(input("einfach (1) oder grafisch (2)"))
    if simple == 1:
        simple_count_down()
    hours = int(input("Eingabe Stunden: "))
    minutes = int(input("Eingabe Minuten: "))
    sec = int(input("Eingabe Sekunden: "))
    counter=hours*3600+minutes*60+sec
    # create root/main window
    root = tk.Tk()
    time_str = tk.StringVar()
    # create the time display label, give it a large font
    # label auto-adjusts to the fontcount
    label_font = ('helvetica', 40)
    tk.Label(root, textvariable=time_str, font=label_font, bg='white', 
             fg='blue', relief='raised', bd=3).pack(fill='x', padx=5, pady=5)
    # create start and stop buttons
    # pack() positions the buttons below the label
    tk.Button(root, text='Count Start', command=count_down).pack()
    # stop simply exits root window
    tk.Button(root, text='Count Stop', command=root.destroy).pack()
    # start the GUI event loop
    root.mainloop()
    print("Times up!")

"""        
if __name__ == '__main__':
    main()
"""
