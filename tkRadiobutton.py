#!/usr/bin/python
#  tkRadiobutton
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
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def ShowChoice():
    print (v.get())
ShowChoice()
Label(root,
      text="""Waehlen Sie Ihre Programmiersprache:""",
#      orient = HORIZONTAL,  # orient not supported
      justify = CENTER,
      padx = 20).pack()

for txt, val in languages:
    Radiobutton(root,
                text=txt,
                indicatoron = 0,
                width = 30,
#                height =2,
                padx = 20,
                variable=v,
                command=ShowChoice,
                value=val).pack(anchor=W)

mainloop()
