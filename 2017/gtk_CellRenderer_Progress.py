#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Thu Sep 14 15:21:09 2017

@author: josef
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class CellRendererProgressWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="CellRendererProgress Example")
        
        self.set_default_size(200, 200)
        
        self.liststore = Gtk.ListStore(str, int, bool)
        self.current_iter = self.liststore.append(["Sabayon", 0, False])
        self.liststore.append(["Zenwalk", 0, False])
        self.liststore.append(["SimplyMepis", 0, False])
        
        treeview = Gtk.TreeView(model=self.liststore)
        
        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
        treeview.append_column(column_text)
        
        renderer_progress = Gtk.CellRendererProgress()
        column_progress = Gtk.TreeViewColumn("Progress", renderer_progress, value=1, inverted=2)
        treeview.append_column(column_progress)
        
        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_inverted_toggled)
        column_toggle = Gtk.TreeViewColumn("Inverted", renderer_toggle, active=2)
        treeview.append_column(column_toggle)
        self.add(treeview)
        
        self.timeout_id = GObject.timeout_add(100, self.on_timeout, None)   # 100 = 10 sec
    
    def on_inverted_toggled(self, widget, path):
        self.liststore[path][2] = not self.liststore[path][2]

    
    def on_timeout(self, user_data):
        new_value = self.liststore[self.current_iter][1] + 1
        if new_value > 100:
            self.current_iter = self.liststore.iter_next(self.current_iter)
            if self.current_iter == None:
                self.reset_model()
            new_value = self.liststore[self.current_iter][1] + 1
        
        self.liststore[self.current_iter][1] = new_value
        return True
    
    def reset_model(self):
        for row in self.liststore:
            row[1] = 0
        self.current_iter = self.liststore.get_iter_first()

win = CellRendererProgressWindow()
win.connect("delete-event", Gtk.main_quit)
print("Position Hauptfenster", win.get_position())
win.set_position(Gtk.WindowPosition.MOUSE)
win.set_keep_above(True)
#win.fullscreen()
print("Position Hauptfenster", win.get_position())
win.show_all()
Gtk.main()