#! /usr/bin/env python2
# walk_around.py  --  created by Ing. Josef KlotzneIr
import Image
def get_image(s):
    return Image.open(s, "r")
strip = get_image('wire.png')
spiral = Image.new(strip.mode, (100,100), 0)
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
x,y,z = 0,0,0
for i in range(100):
    for j in range(100):
        spiral.putpixel((x,y), strip.getpixel((z,0)))
        x+=1
        z+=1
    y+=1
    x=0
"""
for i in range(200):
    d = dirs[i % 4]
    for j in range(100 - (i + 1) / 2):
        x += d[0]
        y += d[1]
        spiral.putpixel((x,y), strip.getpixel((z,0)))
        z += 1
"""
spiral.show()
#spiral.save('spiral.png')
