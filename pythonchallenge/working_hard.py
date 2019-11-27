#! /usr/bin/env python2
# working_hard.py  --  created by Ing. Josef Klotzner
import bz2
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print "user: ",bz2.BZ2Decompressor().decompress(un)
print "password: ",bz2.BZ2Decompressor().decompress(pw)
"""
import Image
import urllib
coords=(179,284,214,311,255,320,281,226,319,224,363,309,339,222,371,225,411,229,404,242,415,252,428,233,428,214,394,207,383,205,390,195,423,192,439,193,442,209,440,215,450,221,457,226,469,202,475,187,494,188,494,169,498,147,491,121,477,136,481,96,471,94,458,98,444,91,420,87,405,92,391,88,376,82,350,79,330,82,314,85,305,90,299,96,290,103,276,110,262,114,225,123,212,125,185,133,138,144,118,160,97,168,87,176,110,180,145,176,153,176,150,182,137,190,126,194,121,198,126,203,151,205,160,195,168,217,169,234,170,260,174,282)
def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]
coordinates=zip(*[iter(coords)]*2)
print coordinates
def get_image(s):
    return Image.open(s, "r")
im = get_image('integrity.jpg')
w,h = im.size
for x,y in coordinates:
    #print x,y
    print ''.join(chr(im.getpixel((x,y))[0]))
print "Bildbreite in Pixel",w
print "Bildhoehe in Pixel",h
"""
#print """ print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))  """
#print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
