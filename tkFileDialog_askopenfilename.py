#  tkFileDialog - askopenfilename
# -*- coding: utf-8 -*-
print ("use python 2.7 for this")
from Tkinter import *   # python 2.7
from tkFileDialog   import askopenfilename
def callback():
    name= askopenfilename()
    print (name)

errmsg = 'ups Fehler!'
Button(text='öffne Datei bla bla bla', command=callback).pack(fill=X)
mainloop()
