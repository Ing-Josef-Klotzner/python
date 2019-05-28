#! /usr/bin/env python2
# cookies_.py  --  created by Ing. Josef Klotzner
import urllib2, urllib, cookielib, re, bz2
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('inflate', 'www.pythonchallenge.com', 'huge', 'file')
jar = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(jar)
opener = urllib2.build_opener(auth_handler, cookie_handler)
#print opener.open('http://www.pythonchallenge.com/pc/return/romance.html').read()

print opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=44827').read()
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
list(jar)[0].value = 'the+flowers+are+on+their+way'
print opener.open('http://www.pythonchallenge.com/pc/stuff/violin.php').read()

"""
for i in range(118): p = next_page(p, pp, message)
print ''.join(message)
print bz2.BZ2Decompressor().decompress(urllib.unquote_plus(''.join(message)))
"""
# result: BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90
# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
