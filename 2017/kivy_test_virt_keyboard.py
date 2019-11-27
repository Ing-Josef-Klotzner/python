#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function
"""
Created on Thu Jul 27 00:28:28 2017

@author: josef
"""
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.vkeyboard import VKeyboard
from kivy.core.window import Window
from kivy.config import Config

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
#        vka = VKeyboard(layout='qwertz')   # alt: "azerty" "qwertz" "qwerty"
        Config.set("kivy", "keyboard_mode", "systemanddock")
        Config.write()
        self.cols = 2
        self.rows = 5
        self.username = TextInput(multiline=False)
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.username)
        self.add_widget(self.password)
        self.add_widget(Label(text='User Name'))
        self.add_widget(Label(text='Passwort'))
        self.add_widget(Label(text='Zur Eingabe in das Feld über User Name tippen'))
        self.add_widget(Label(text='Zur Eingabe in das Feld über "Passwort" tippen'))

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()