#! /usr/bin/env python
# zip_.py  --  created by Ing. Josef Klotzner
import urllib, zipfile, re, collections

o, n, f = [], "90052", "%s.txt"
nnr = "Next nothing is (\d+)"

# Download the ZIP file from http://www.pythonchallenge.com/pc/def/channel.zip

file = zipfile.ZipFile("channel.zip")

while True:
    try:
        n = re.search(nnr, file.read(f % n)).group(1)
    except:
        print file.read(f % n)
        break

    o.append(file.getinfo(f % n).comment)
print "".join(o)

"""
result:
Collect the comments.
***************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************

"""
