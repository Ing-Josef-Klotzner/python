#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import urllib, re, webbrowser
import pickle

"""
dont try all nothings
"""
site = "http://www.pythonchallenge.com/pc/def/"
opt = "banner.p"
answer_to_find = ""

try:
    html_string = urllib.urlopen(site + opt).read()
    #html_lines = urllib.urlopen(site + opt).readlines()
except IOError:
    print("")
    print("the server pythonchallenge can not be reached ...")

banner = pickle.loads(html_string)
for line in banner:
    for index in range(len(line)):
        print(line[index][0]*line[index][1], end="")
    print("")

print("another solution using joins: ")
print ('\n'.join(["".join([i[0]*i[1] for i in b]) for b in banner]))

print("another solution using map: ")
for line in banner:
    print ("".join(map(lambda pair: pair[0]*pair[1], line)))
    
print("another solution using Image, ImageDraw saved as '5_banner.bmp'")
import Image, ImageDraw
im = Image.new("1", (190, 48))
draw = ImageDraw.Draw(im)
line = 0
for i in banner:
    xpos = 0
    for j in i:
        if j[0] == " ":
            draw.line([(xpos,line), (xpos+j[1]*2, line)], 255)
            draw.line([(xpos,line+1), (xpos+j[1]*2, line+1)], 255)
        xpos += j[1]*2
    line += 2    
im.save("5_banner.bmp")

#answer_to_find = 'channel'    ... to see on screen

print("")
#print("The answer to find is: " + answer_to_find)
#webbrowser.open(site + answer_to_find)
