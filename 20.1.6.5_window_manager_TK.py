#  window manager wm TK
# -*- coding: iso-8859-15 -*-
from Tkinter import *
class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()


# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("Mein kleines tu nichts weiter - sei einfach ein - Fenster")
myapp.master.maxsize(1000, 400)
myapp.master.minsize(500,100)

#print dir(myapp.master)

# start the program
myapp.mainloop()