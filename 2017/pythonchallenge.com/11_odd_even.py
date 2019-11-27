#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from string import digits, printable, letters
import re, Image

"""
11 odd even
"""
# site = "http://www.pythonchallenge.com/pc/return/"
# opt = "5808.html"

white = 255, 255, 255
black = 0, 0, 0
pic = Image.open("11_odd_even.jpg")

# found data looking like characters in odd lines of picture in red and green channel
# closer look: data in even lines with odd x-Position and in odd lines with even x-Position
# get all those pixel data and create new picture of it
width, height = pic.size
#result = Image.new('RGB', (width//2, height//2), white)
#even_pic = Image.new('RGB', (width//2, height//2), white)

# odd_pic is nearly same as even, slightly better to see
odd_pic = Image.new('RGB', (width//2, height//2), white)
#diff_pic = Image.new('RGB', (width//2, height//2), black)
# second solution:
write_over_pic = Image.new('RGB', (width, height), white)

#for y in range(0,height,1):
#    cropped = pic.crop((0,y,width,y + 1))
##    cropped_all += cropped
#    data = cropped.getdata()
#    idx = 0
#    for pixel in data:
##        print(pixel, end="")
#        if y % 2 and idx % 2 or (y + 1) % 2 and (idx + 1) % 2:
##         even numbers in even lines of pixels hold s.char data
##         odd numbers in odd lines of pixels hold s.char data        
##        if y % 2 and (idx + 1) % 2 or (y + 1) % 2 and idx % 2:   
##         odd numbers in even lines of pixels hold char data
##         even numbers in odd lines of pixels hold char data
##            print(pixel, end="")
#            result.putpixel((idx//2, y//2), pic.getpixel((idx,y))[1] )
##               investigation of printable characters   --- >>>  no result
##            if chr(pixel[1]) in letters + "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~":
###                print(pixel[1], end=" ")
##                print(chr(pixel[1]), end="")
###                red_odd.putpixel((idx//2, y//2), pic.getpixel((idx,y))[1] )
##            else:
##                pass
##                print(" ", end = "")
#        idx += 1
#    print("")

# shorter after above investigation:
## create even pixels pic
#for y in range(0, height, 2):
#    for x in range(0, width, 2):
#        even_pic.putpixel( (x // 2, y // 2), pic.getpixel((x, y)) )
#overwritten = 0
# alernating dark pixel (d) and picture pixel (p) information
# dpd
# pdp
print(pic.getpixel((0,0)), pic.getpixel((1,0)), pic.getpixel((2,0)))
print(pic.getpixel((0,1)), pic.getpixel((1,1)), pic.getpixel((2,1)))
# create odd pixels pic
for y in range(1, height, 2):
    for x in range(1, width, 2):
#               odd and even pictures are slightly different, but nothing special to see  :)
#        if pic.getpixel((x, y)) != pic.getpixel((x - 1, y - 1)):
#            diff_pix = tuple()
#            diff_pix += (abs(pic.getpixel((x, y))[0] - pic.getpixel((x - 1, y - 1))[0]),)
#            diff_pix += (abs(pic.getpixel((x, y))[1] - pic.getpixel((x - 1, y - 1))[1]),)
#            diff_pix += (abs(pic.getpixel((x, y))[2] - pic.getpixel((x - 1, y - 1))[2]),)
##            print(diff_pix)
#            diff_pic.putpixel( (x // 2, y // 2), diff_pix )
#            print(pic.getpixel((x - 1, y - 1)), "overwritten with", pic.getpixel((x, y)))
#            overwritten += 1
        odd_pic.putpixel( (x // 2, y // 2), pic.getpixel((x, y)) )

#even = Image.new('L', pic.size, white)
## RED
#for i in range( pic.size[0] ):
#    for j in range(0,pic.size[1],2):
#        even.putpixel((i, j), pic.getpixel((i,j))[1] )

#print("pixels total:", height * width, "pixels overwritten: ", overwritten)
#even_pic.show()
# odd pic is enough for result - better to see than even

#   odd_pic.show()

#diff_pic.show()
#result.show()
#pic.show()

# other solution: overwrite picture pixels with dark pixel information
for y in range(0, height, 2):
    for x in range(0, width, 2):
        write_over_pic.putpixel((x + 1, y), pic.getpixel((x, y)) )
        write_over_pic.putpixel((x, y), pic.getpixel((x, y)) )
for y in range(1, height, 2):
    for x in range(1, width, 2):
        write_over_pic.putpixel((x - 1, y), pic.getpixel((x, y)) )
        write_over_pic.putpixel((x, y), pic.getpixel((x, y)) )

write_over_pic.show()

# faster solution:
all = []
full=list(pic.getdata())
even = full[0::2]
odd = full[1::2]
all = even + odd
pic.putdata(all) 
pic.show()

answer_to_find = "look to the picture - there is to read: 'evil'"
print("answer to find is: ", answer_to_find)

#webbrowser.open(site + answer_to_find)
