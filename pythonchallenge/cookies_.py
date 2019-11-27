#! /usr/bin/env python2
# cookies_.py  --  created by Ing. Josef Klotzner
import urllib2, urllib, cookielib, re, bz2
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('inflate', 'www.pythonchallenge.com', 'huge', 'file')
jar = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(jar)
opener = urllib2.build_opener(auth_handler, cookie_handler)
#print opener.open('http://www.pythonchallenge.com/pc/return/romance.html').read()

#print opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=44827').read()
#print list(jar)
def next_page(p, pp, message):
    text = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s' % p).read()
    m = re.search('and the next busynothing is ([0-9]+)', text)
    message.append(list(jar)[0].value)
    if m: 
        pp.append(m.group(1))
    else: 
        print text
        return
    print ''.join(message)
    return m.group(1)
p = 12345
pp = []
message = []
for i in range(118): p = next_page(p, pp, message)
print ''.join(message)
print bz2.BZ2Decompressor().decompress(urllib.unquote_plus(''.join(message)))
