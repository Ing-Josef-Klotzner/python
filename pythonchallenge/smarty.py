#! /usr/bin/env python2
# smarty.py  --  created by Ing. Josef Klotzner
import Image
import urllib
def get_challenge(s):
    return urllib.urlopen('http://www.pythonchallenge.com/pc/' + s).read()
def get_image(s):
    return Image.open(s, "r")
im = get_image('oxygen.png')
w,h = im.size
print ''.join([chr(im.getpixel((i, h/2))[0]) for i in range(0,w,7)])
print "Bildbreite in Pixel",w
print "Bildhoehe in Pixel",h
print """ print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))  """
print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
