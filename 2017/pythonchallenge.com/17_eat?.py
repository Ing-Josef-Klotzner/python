#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
17 eat?
"""
site = "http://www.pythonchallenge.com/pc/return/"
opt = "romance.html"

"""
"""
#http://www.pythonchallenge.com/pc/return/romance.html
import urllib2
from urllib import quote_plus, unquote_plus
import cookielib
import re
print("Staring to follow the busynothing chain, but also picking up the crumbs!")
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),urllib2.HTTPHandler())
def getPage(nothing="12345"):
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
	req = urllib2.Request(url+nothing)
	response = opener.open(req)
	return response.read()
pat = re.compile(r"(.*?)and the next busynothing is (\d*)$")
num = 12345
cookievals = []
count = 0
while True:
	count += 1
	m = pat.match(getPage(str(num)))
	for cookie in cj:
			cookievals.append(unquote_plus(cookie.value))
	if m == None:
		break
	elif count > 400:
		print("400 times is more than enough")
		break
	else:
		print(str(count) + ": " + m.group(0))
		num = int(m.group(2))
print("Done retrieving cookies")
print()
print("Decompressing the message")
import bz2
message = bz2.decompress("".join(cookievals))
print("The message is: %s" % message)
print()
print("Mozart was born to Leopold...")
print("Looking up Leopold")
##Call his father Leopold
import xmlrpclib
x= xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
number = x.phone("Leopold")
print("Leopold's number is: %s" % number )
print()
print("Calling Leopold and sending him the mssage")
o = urllib2.build_opener()
message = "the flowers are on their way"
o.addheaders.append(('Cookie', 'info='+quote_plus(message)))
res = o.open("http://www.pythonchallenge.com/pc/stuff/violin.php")
print("Message sent!")
print()
print("His response is...")
print(res.read())


answer_to_find = "balloons"
#print("answer to find is: ", answer_to_find)
#opt = "".join(x for x in lower(answer_to_find) if x in letters)
#print(" new site: http://www.pythonchallenge.com/pc/return/" + opt + ".html")
print("answer to find:", answer_to_find)
##webbrowser.open(site + answer_to_find)


