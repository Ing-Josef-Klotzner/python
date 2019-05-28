#!/usr/bin/python
#  tkCanvas_scrollbar
# -*- coding: utf-8 -*-
from sys import version_info
if version_info.major == 3:
    from tkinter import *   # python 3.2
elif version_info.major == 2:
    from Tkinter import *   # python 2.7
else:
    print ("what the hell you are running?  :D")

root = Tk()
S = Scrollbar(root)
T = Text(root, height=4, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(END, quote)
mainloop(  )
