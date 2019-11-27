#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Fri Sep  8 20:52:41 2017

@author: josef
"""

#Python is amazing
#Create ASCII-Char HTML Table
 
strTable = "<html><table><tr><th>Char</th><th>ASCII</th></tr>"
 
for num in range(33,48):
 symb = chr(num)
 strRW = "<tr><td>"+str(symb)+ "</td><td>"+str(num)+"</td></tr>"
 strTable = strTable+strRW
 
strTable = strTable+"</table></html>"
 
hs = open("asciiCharHTMLTable.html", 'w')
hs.write(strTable)
 
print (strTable)