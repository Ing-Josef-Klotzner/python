#! /usr/bin/env python2
# odd_even.py  --  created by Ing. Josef Klotzner
import Image

def get_image(s):
    return Image.open(s, "r")

im = get_image('cave.jpg')
w,h =im.size

for i in range(w):
    for j in range(h):
        if (i + j) % 2 == 1:
            im.putpixel((i,j), 0)
im.show()
