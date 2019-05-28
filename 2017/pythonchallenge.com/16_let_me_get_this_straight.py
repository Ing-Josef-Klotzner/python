#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import Image
"""
16 let me get this straight
"""
# site = "http://www.pythonchallenge.com/pc/return/"
# opt = "mozart.html"

"""
find and align sequence:  195 195 195 195 195 
"""

white = 255, 255, 255
orig = Image.open("16_let_me_get_this_straight_mozart.gif")
width, height = orig.size

def find(dat):
    dat = list(dat)
    for i, d in enumerate(dat):
        if dat[i] == 195 and i < len(dat) - 5:
#            print(dat[i+1:i+5])
            if dat[i+1:i+5] == [195, 195, 195, 195]:
                return i

## rotate per pixel
#def rotate(img, amount):   # only for one line pic crops!
#    imr = Image.new('L', (width, 1), 255)
#    for x in range(width - amount):
#        imr.putpixel((x, 0), img.getpixel((x + amount, 0)))
#    for x in range(width - amount, width):
#        imr.putpixel((x, 0), img.getpixel((x - width + amount, 0)))
#    return imr

# rotate per crop
def rotate(img, amount):   # only for one line pic crops!
    pf = img.crop((0, 0, amount, 1))
    pb = img.crop((amount, 0, width, 1))
    imr = Image.new('RGB', (width, 1), white)
    imr.paste(pf,(width - amount, 0))
    imr.paste(pb,(0, 0))
    return imr

#cropped = orig.crop((0, 20, width, 21))
#data = cropped.getdata()
#for i in data:
#    print(i, end = " ")
#print(find(data))

# solution by shifting with crops by width - line found position
imn = Image.new('L', (width * 2, height), 255)
for y in range(height):
    cropped = orig.crop((0, y, width, y + 1))
    data = cropped.getdata()
    xo = find(data)
#    if xo < 320:
#        xo += 320
#    else:
#        xo -= 320
    imn.paste(cropped,(width - xo,y))

imn.show()

# other solution: rotate picture lines
imr = Image.new('RGB', (width, height), white)
for y in range(height):
    cropped = orig.crop((0, y, width, y + 1))
    data = cropped.getdata()
    xo = find(data)
    cropped = rotate(cropped, xo)    
    imr.paste(cropped, (0, y))
imr.show()

answer_to_find = "see in picture - romance"
#print("answer to find is: ", answer_to_find)
#opt = "".join(x for x in lower(answer_to_find) if x in letters)
#print(" new site: http://www.pythonchallenge.com/pc/return/" + opt + ".html")
print("answer to find:", answer_to_find)
##webbrowser.open(site + answer_to_find)


