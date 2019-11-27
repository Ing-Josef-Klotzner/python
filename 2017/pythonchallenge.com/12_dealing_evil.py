#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from string import digits, printable, letters
import re, Image, colorsys

"""
12 dealing evil
hint2:
evil2.jpg --- not jpg - - .gfx
download evil2.gfx
"""
# site = "http://www.pythonchallenge.com/pc/return/"
# opt = "evil.html"

data = open("12_dealing_evil2.gfx", "rb").read()
print(len(data))
extension = ('.jpg', '.png', '.gif', '.png', '.jpg')
for i in range(5):
    open(('12_dealing_evil_s%d' + extension[i]) % i ,'wb').write(data[i::5])
    
#white = 255, 255, 255
#black = 0, 0, 0
#pic = Image.open("12_dealing_evil1.jpg")
#v_offs = 32

## how
#width, height = pic.size
#for yo in range(80):
#    if not yo % 6:
#        print("")
#    cp = pic.getpixel((220, v_offs + yo))
#    print(yo + v_offs, end = " ")
#    for xo in range(6):
#        bp = pic.getpixel((214 + xo, v_offs + yo))
#        print(bp, end = " ")
#    print(cp, end = "  Y: ")
#    ra = cp[0] * .3
#    ga = cp[1] * .59
#    ba = cp[2] * .11
#    y = ra + ga + ba
#    hsv = list(colorsys.rgb_to_hsv(cp[0]/255, cp[1]/255, cp[2]/255))
#    hsv[0] = hsv[0] * 360
#    for i in range(1, 3):
#        hsv[i] = hsv[i] * 255
#    print(y, " HSV: {:.2f} {:.2f} {:.2f}".format(*hsv))
## analyze first lines of pic
#testpic_data = []
#cropped = pic.crop((0, v_offs, width, v_offs + 48))
#data = cropped.getdata()
#datalist = list(data)
#data_part = datalist[0:width]
#data_gen = (x for x in data_part)
#for i in data_gen:
#    print(i, end = "")
## fill whole picture with one line from datalist for testing result
#testpic_data += datalist
#for i in range(48):
#    for j in range(height//128):
#        testpic_data += datalist[i * width:(i + 1) * width]
##pic.putdata(testpic_data)
#pic.putpixel((220, v_offs), white)
##picn = pic.transform(pic.size, Image.AFFINE, data = (1, 5, 0, 1, 1, 0), resample = Image.NEAREST)
#pic.show()

##little_cropped = pic.crop((20, 360, 21, 366))
##sm = little_cropped.getdata()
###drg, dbg = 1.38617100531, 0.647512973008

##for i in sm:
###    print(i[0]/i[1], i[2]/i[1], "Korrekturfaktoren: ", drg / (i[0]/i[1]), dbg / (i[2]/i[1]) )
###    print(drg / (i[0]/i[1]), dbg / (i[2]/i[1]) )
##    print(1 / ((i[0] * .3 + i[1] * .59 + i[2] * .11) / 80.31))

###little_cropped.show()

#"""
#Korrekturfaktoren zur Eliminierung zeilenweiser farbverfälschung:
#0.901684051998 1.00891556259    R/G  B/G
#0.92411400354 1.18075895078
#1.16497350446 1.02307049735
#1.1971476864 0.946365114396
#1.02363397315 0.971269459512
#0.878559087873 0.910565118292

#r/g             b/g
#1.43023255814 0.686046511628
#1.5 0.548387096774
#1.18987341772 0.632911392405
#1.15789473684 0.684210526316
#1.26582278481 0.759493670886
#1.30337078652 0.808988764045

#rgk             bgk
#0.914442694348 1.00091317722
#0.871910476007 1.25216840023
#1.09916373837 1.08494333001
#1.12952038937 1.00359899076
#1.03321391407 0.904119441673
#1.00344869437 0.848804117183

#"""
#gk = (
#1.026015625,
#1.16221238938,
#0.938071428571,
#0.918391608392,
#1.05064,
#0.972814814815
#)
#gk = (1,1,1,1,1,1)
#rgk = (
#0.914442694348,
#0.871910476007,
#1.09916373837,
#1.12952038937,
#1.03321391407,
#1.00344869437
#)
#bgk = (
#1.00091317722,
#1.25216840023,
#1.08494333001,
#1.00359899076,
#0.904119441673,
#0.848804117183
#)

#gmk = (
#1.02192982456, 0.91015625, 
#1.03097345133, 1.25268817204, 
#0.832142857143, 1.17676767677, 
#0.814685314685, 0.917322834646, 
#1.23936170213, 0.932,
#1.33908045977, 0.862962962963,
#)
##gmk = (1,1,1,1,1,1)
## print(map(lambda x : x[0] * x[1], zip(gk, bgk)))
#print(sum(bgk) / 6)

##data = pic.getdata()
#imn = Image.new('RGB', (width, height), white)
#for y in range(0, height,1):
#    if not y % 6:
#        o = 0
#    for x in range(0, width - 2, 1):
#        if not x % 2:
#            xo = 0
##        print(o)
#        pix = pic.getpixel((x, y))
##        pixx = pic.getpixel((x + 1, y))
##        if pixx[1] < pix[1]:
##            pix = pixx
#        pik = ()
#        pik += (int(pix[0] * rgk[o] * gmk[o * 2 + xo]),)
#        pik += (int(pix[1] * gmk[o * 2 + xo]),)
#        pik += (int(pix[2] * bgk[o] * gmk[o * 2 + xo]),)
##        pik += (int(pix[0] * rgk[o] * gk[o]),)
##        pik += (int(pix[1] * gk[o]),)
##        pik += (int(pix[2] * bgk[o] * gk[o]),)
##        pik += (int(pix[0]),)
##        pik += (int(pix[1]),)
##        pik += (int(pix[2]),)
#        imn.putpixel((x, y), pik)
##        imn.putpixel((x + 1, y), pik)
#        xo += 1
#    o += 1

#"""
#114 128 
#113 93 
#140 99 
#143 127 
#94 125 
#87 135

#116 116 
#102 95 
#144 124 
#179 105 
#78 147 
#102 109
#"""
#little_cropped = imn.crop((124, 360, 126, 366))
#sm = little_cropped.getdata()
#imn.putpixel((124,360), white)
#imn.putpixel((125,360), white)
#imn.putpixel((125,366), white)

##drg, dbg = 1.38617100531, 0.647512973008
##drg, dbg = 1.30786571401, 0.686672993676
#dg = 116.5
#n = 0
#for i in sm:
#    if not n % 2:
#        print("")
#    print(i[1], end = " ")
##    dg += i[1]
#    n += 1
##print (dg/12)
##    print(i[0]/i[1], i[2]/i[1], "Korrekturfaktoren: ", drg / (i[0]/i[1]), dbg / (i[2]/i[1]) )
##    print(drg / (i[0]/i[1]), dbg / (i[2]/i[1]) )
##    rg = i[0] / i[1]
##    bg = i[2] / i[1]
##    g = i[1]
##    dg += g
##    print(drg / rg, dbg / bg)
##    print(rg, bg)
##    print(dg/g)
##print(dg/6)

##for y in range(5, height - 6, 6):
##    for x in range(0, width, 2):
##        diff_pix = ()
##        diff_pix += (abs(pic.getpixel((x + 1, y))[0] - pic.getpixel((x, y))[0]),)
##        diff_pix += (abs(pic.getpixel((x + 1, y))[1] - pic.getpixel((x, y))[1]),)
##        diff_pix += (abs(pic.getpixel((x + 1, y))[2] - pic.getpixel((x, y))[2]),)
##        for o in range(6):
##            imn.putpixel( (x, y + o), diff_pix )
##            imn.putpixel( (x + 1, y + o), diff_pix )
##        l = chr(diff_pix[1])
##        if l in letters + "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~":
##            print(l, end = "")
##        else:
##            print(" ", end = "")
##    print("")
#imn.show()
answer_to_find = "look to the 5 pictures - there is to read: dis - pro - port - ional"
print("answer to find is: ", answer_to_find)

##webbrowser.open(site + answer_to_find)
