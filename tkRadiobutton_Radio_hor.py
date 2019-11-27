#!/usr/bin/python
#  tkRadiobutton - Radio - horizontale Tasten
# -*- coding: iso-8859-15 -*-
from sys import version_info
if version_info.major == 3:
    from tkinter import *   # python 3.2
elif version_info.major == 2:
    from Tkinter import *   # python 2.7
else:
    print ("what the hell you are running?  :D")

root = Tk()

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("UKW",1),
    ("KW",2),
    ("MW",3),
    ("LW",4),
    ("AUS",5)
]

def ShowChoice():
    print (v.get())
ShowChoice()
Label(root,
      text="""Wählen Sie Ihren Senderbereich:""",
#      orient = HORIZONTAL,  # orient not supported
      justify = CENTER,
      padx = 20).pack()

for txt, val in languages:
    Radiobutton(root,
                text=txt,
                indicatoron = 0,
                width = 30,
                height =2,
                padx = 20,
                variable=v,
                command=ShowChoice,
                value=val).pack(side=LEFT, anchor=W)

mainloop()
