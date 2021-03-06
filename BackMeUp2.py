#! /usr/bin/env python
# BackMeUp.py  --  created by Ing. Josef Klotzner
# -*- coding: iso-8859-15 -*-
from sys import version_info
if version_info.major == 3:
    from tkinter import *   # python 3.2
elif version_info.major == 2:
    from Tkinter import *   # python 2.7
else:
    print ("what the hell you are running?  :D")
try:
    from tkinter.filedialog import askopenfilename
except ImportError:
    from tkFileDialog   import askopenfilename
try:
    from tkinter.messagebox import *
except ImportError:
    from tkMessageBox import *

class ToolTip:
    def __init__(self, master, text='Your text here', delay=0, **opts):
        self.master = master
        self._opts = {'anchor':'center', 'bd':1, 'bg':'lightyellow', 'delay':delay, 'fg':'black',\
                    'follow_mouse':0, 'font':None, 'justify':'left', 'padx':4, 'pady':2,\
                    'relief':'solid', 'state':'normal', 'text':text, 'textvariable':None,\
                        'width':0, 'wraplength':150}
        self.configure(**opts)
        self._tipwindow = None
        self._id = None
        self._id1 = self.master.bind("<Enter>", self.enter, '+')
        self._id2 = self.master.bind("<Leave>", self.leave, '+')
        self._id3 = self.master.bind("<ButtonPress>", self.leave, '+')
        self._follow_mouse = 0
        if self._opts['follow_mouse']:
            self._id4 = self.master.bind("<Motion>", self.motion, '+')
            self._follow_mouse = 1
      
    def configure(self, **opts):
        for key in opts:
            if self._opts.has_key(key):
                self._opts[key] = opts[key]
            else:
                KeyError = 'KeyError: Unknown option: "%s"' %key
                raise KeyError
      
      ##----these methods handle the callbacks on "<Enter>", "<Leave>" and "<Motion>"---------------##
      ##----events on the parent widget; override them if you want to change the widget's behavior--##
      
    def enter(self, event=None):
        self._schedule()
          
    def leave(self, event=None):
        self._unschedule()
        self._hide()
      
    def motion(self, event=None):
        if self._tipwindow and self._follow_mouse:
            x, y = self.coords()
            self._tipwindow.wm_geometry("+%d+%d" % (x, y))
      
      ##------the methods that do the work:---------------------------------------------------------##
      
    def _schedule(self):
        self._unschedule()
        if self._opts['state'] == 'disabled':
            return
        self._id = self.master.after(self._opts['delay'], self._show)
  
    def _unschedule(self):
        id = self._id
        self._id = None
        if id:
            self.master.after_cancel(id)
  
    def _show(self):
        if self._opts['state'] == 'disabled':
            self._unschedule()
            return
        if not self._tipwindow:
            self._tipwindow = tw = Toplevel(self.master)
            # hide the window until we know the geometry
            tw.withdraw()
            tw.wm_overrideredirect(1)
  
            if tw.tk.call("tk", "windowingsystem") == 'aqua':
                tw.tk.call("::tk::unsupported::MacWindowStyle", "style", tw._w, "help", "none")
  
            self.create_contents()
            tw.update_idletasks()
            x, y = self.coords()
            tw.wm_geometry("+%d+%d" % (x, y))
            tw.deiconify()
      
    def _hide(self):
        tw = self._tipwindow
        self._tipwindow = None
        if tw:
            tw.destroy()
                  
      ##----these methods might be overridden in derived classes:----------------------------------##
      
    def coords(self):
        # The tip window must be completely outside the master widget;
        # otherwise when the mouse enters the tip window we get
        # a leave event and it disappears, and then we get an enter
        # event and it reappears, and so on forever :-(
        # or we take care that the mouse pointer is always outside the tipwindow :-)
        tw = self._tipwindow
        twx, twy = tw.winfo_reqwidth(), tw.winfo_reqheight()
        w, h = tw.winfo_screenwidth(), tw.winfo_screenheight()
        # calculate the y coordinate:
        if self._follow_mouse:
            y = tw.winfo_pointery() + 20
            # make sure the tipwindow is never outside the screen:
            if y + twy > h:
                y = y - twy - 30
        else:
            y = self.master.winfo_rooty() + self.master.winfo_height() + 3
            if y + twy > h:
                y = self.master.winfo_rooty() - twy - 3
        # we can use the same x coord in both cases:
        x = tw.winfo_pointerx() - twx / 2
        if x < 0:
            x = 0
        elif x + twx > w:
            x = w - twx
        return x, y
  
    def create_contents(self):
        opts = self._opts.copy()
        for opt in ('delay', 'follow_mouse', 'state'):
            del opts[opt]
        label = Label(self._tipwindow, **opts)
        label.pack()

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)    
def Backup():
    print ("Backup Window here")
def Restore():
    print ("Restore Window here")
    name = askopenfilename()
    print (name)
def Settings():
    print ("settings currently in main window")
def About():
    showinfo("BackMeUp Help",
    "This is a Backup App to save Your computer partitions\n"+
    "Author: Ing. Josef Klotzner \n"+
    "running python version "+ str(version_info.major))
    
root = Tk()
menu = Menu(root)
root.config(menu=menu)
root.title('BackMeUp')
filemenu = Menu(menu)
menu.add_cascade(label="Partition", menu=filemenu)
filemenu.add_command(label="Backup", command=Backup)
filemenu.add_command(label="Restore", command=Restore)
filemenu.add_command(label="Settings", command=Settings)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
bak = Checkbar(root, ['--allow-rw-mounted', '--verbose', '--allow-no-acl-xattr'])
rest = Checkbar(root, ['English','German'])
bak.pack(side=TOP,  fill=X)
rest.pack(side=LEFT)
bak.config(relief=GROOVE, bd=2)
t1 = ToolTip(bak, follow_mouse=1, text="I'm a tooltip with follow_mouse set to 1, so I won't be placed outside my parent",delay=100)
mainloop()