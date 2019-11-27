#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import string, re, urllib, pyglet



"""
7 smarty
"""
site = "http://www.pythonchallenge.com/pc/def/"
opt = "oxygen.png"
answer_to_find = ""

# decode png
pic = pyglet.image.load('7_smarty.png')
raw_image = pic.get_image_data()
format = 'RGBA'
pitch = raw_image.width * len(format)
pixels = raw_image.get_data(format, pitch)
width = (pitch)                 # 2516
height = (len(pixels)/pitch)    # 95
all_pixel_count = (len(pixels)) # 239020   (mid of picture 119510)
lti = 47   # line_to_inspect
for pix_in_mid in range(width * lti, width * lti + width):
    print(pixels[pix_in_mid], end="")
pix_line_in_mid = pixels[width * lti : width * lti + width]
#print("alpha channel value: " + str(ord(pix_line_in_mid[3])))
answer_string = "".join(re.findall('([a-z0-9 ,])[a-z0-9 ,]+.[a-z0-9 ,]+.[a-z0-9 ,]+.[a-z0-9 ,]+.[a-z0-9 ,]+.[a-z0-9 ,]+.[a-z0-9 ,]+.', pix_line_in_mid))
# answer_string is "smart guy, you made it the next level is 105, 110, 116, 101, 103, 114, 105, 116, 121"
# -> convert last numbers from ascii to characters being able to read:
number_pos = answer_string.find("1")
print("\n")
print(answer_string)
answer_to_find = answer_string[:number_pos]
number_str = answer_string[number_pos:]
for pos in range(number_pos, len(answer_string), 5):
    num_str = ""
    for n in range(3):
        num_str += answer_string[pos + n]
    print(num_str)
    char = chr(int(num_str))
    answer_to_find += char
print("convert ascii numbers to characters")
print("answer to find is: " + answer_to_find)
#webbrowser.open(site + answer_to_find)
