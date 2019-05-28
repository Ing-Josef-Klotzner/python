#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import string, re, bz2
"""
8 working hard
"""
site = "http://www.pythonchallenge.com/pc/def/"
opt = "oxygen.png"
answer_to_find = ""
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

answer_to_find = ""
print("answer to find is: " + answer_to_find)
print("username: " + bz2.decompress(un))
print("password: " + bz2.decompress(pw))

#webbrowser.open(site + answer_to_find)
