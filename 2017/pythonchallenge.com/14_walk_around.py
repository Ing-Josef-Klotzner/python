#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import Image
"""
14 walk around
"""
# site = "http://www.pythonchallenge.com/pc/return/"
# opt = "italy.html"

"""
4...
.2.3
211.
..3.

4 3 3 2 2 1 1 = 16 = 4 * 4
"""
white = 255, 255, 255
wire_pic = Image.open("14_walk_around_wire.png")   # 10000 * 1  !!!

result = Image.new('RGB', (100, 100), white)

spiral = tuple()
counter = 100
spiral += (counter,)
counter -= 1
while counter > 0:   # create spiral tuple
    spiral += (counter, counter,)
    counter -= 1
#spiral += (counter,)
#print(spiral)
wo = 0
yr, xd, yl, xu = 0, 99, 99, 0
xro, ydo, xlo, yuo = 0, 1, -1, 0
for idx, spp in enumerate(spiral):
    if not idx % 4:
        for xr in range(spp):
            #print(xr + xro, yr)
            result.putpixel((xr + xro, yr), wire_pic.getpixel((xr + wo, 0)))
        xro +=1
        yr += 1
    if not (idx - 1) % 4:
        for yd in range(spp):
            result.putpixel((xd, yd + ydo), wire_pic.getpixel((yd + wo, 0)))
        xd -= 1
        ydo += 1
    if not (idx - 2) % 4:
        for xl in range(spp):
            #print(xl, yl, wo)
            result.putpixel((spp - xl + xlo, yl), wire_pic.getpixel((xl + wo, 0)))
        yl -= 1
        xlo += 1
    if not (idx - 3) % 4:
        for yu in range(spp):
            #print(xu, yu + yuo, yu + wo)
            result.putpixel((xu, spp - yu + yuo), wire_pic.getpixel((yu + wo, 0)))
        xu += 1
        yuo += 1
    wo += spp

##wrong:
#p = 0
#for x in range(99, -1, -1):
#    for y in range(100):
#        result.putpixel((x, y), wire_pic.getpixel((p, 0)))
#        p += 1
##wrong result -- to see in picture: bit  --> bit.html tells: "you took the wrong curve."
result.show()

# version 2:

im = Image.open('14_walk_around_wire.png')
delta = [(1,0),(0,1),(-1,0),(0,-1)]
out = Image.new('RGB', [100,100])
x,y,p = -1,0,0
d = 200 
while d/2>0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            x, y = x + v[0], y + v[1]
            out.putpixel((x, y),im.getpixel((p,0)))
            p += 1
        d -= 1
#out.show()
answer_to_find = "cat in picture - when calling cat.html -> his name is uzi -> uzi.html"
#print("answer to find is: ", answer_to_find)
#opt = "".join(x for x in lower(answer_to_find) if x in letters)
#print(" new site: http://www.pythonchallenge.com/pc/return/" + opt + ".html")
print("answer to find:", answer_to_find)
##webbrowser.open(site + answer_to_find)


