#! /usr/bin/env python2
# attached_india2.py  --  created by Ing. Josef Klotzner
import urllib2, urllib, cookielib, re, bz2
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('inflate', 'www.pythonchallenge.com', 'huge', 'file')
jar = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(jar)
opener = urllib2.build_opener(auth_handler, cookie_handler)
#print opener.open('http://www.pythonchallenge.com/pc/return/romance.html').read()

print opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=44827').read()
#print list(jar)
list(jar)[0].value = 'sorry'
print opener.open('http://www.pythonchallenge.com/pc/stuff/violin.php').read()

import wave
w=wave.open('india.wav')
w2=wave.open('endian.wav','w')
w2.setnchannels(w.getnchannels())
w2.setsampwidth(w.getsampwidth())
w2.setframerate(w.getframerate())
frm=w.readframes(w.getnframes())
wave.big_endian=1
w2.writeframes(frm)
w.close()
w2.close()
