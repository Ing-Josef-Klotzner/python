#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function
"""
Created on Mon Jul 24 23:16:54 2017

@author: josef
"""

import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
    MyApp().run()