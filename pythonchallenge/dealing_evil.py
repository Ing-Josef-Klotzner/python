#! /usr/bin/env python2
# dealing_evil.py  --  created by Ing. Josef KlotzneIr
import Image
from cStringIO import StringIO

s = open("evil2.gfx", "rb").read()
print s[0:60:5]
print s[1:60:5]
print s[2:60:5]
print s[3:60:5]
print s[4:60:5]
for i in range(5):
    piece = s[i::5]  # every fifth byte, starting at i
    im = Image.open(StringIO(piece))
    f = open("%d.%s" % (i, im.format.lower()), "wb")
    f.write(piece)
    f.close()
