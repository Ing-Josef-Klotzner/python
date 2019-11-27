#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 19:21:24 2017

@author: josef
"""
import urllib2
import re

html_now = ' <script type="text/javascript">\
var NvPage = {"PageId":28,"LanguageId":1,"PageHierarchy":".3.14.28.","IsPreview":false,"DesignMode":false};\
var FM = {"CountryID":13,"LanguageID":1,"PointID":2761369,"SiteID":392,"CountryCode":"AT","CountryName":"Austria","GoogleHint":"Austria Vienna","Capital":2761369,"MeteoMapRegion":"008","Point":{"ID":2761369,"Type":0,"Name":"Vienna","Latitude":48.2084900000,"Longtitude":16.3720800000,"Elevation":"171m"}};\
'

print html_now

#getcity=re.search('''GoogleHint = "(.*?)\s.*?"''', html)
#getcity=re.search('''GoogleHint":".*?\s(.*?)"''', html)
countryCode_fetch=re.search('CountryCode":"([A-Z]{2})', html_now)

print (countryCode_fetch.group(0))
print (countryCode_fetch.group(1))

exit()

CITY_ID = str(2761369) # self.screenlet.ZIP #brownse to http://freemeteo.com and find your city's id_number
print "===========================\nSelected Zip Code:", CITY_ID
#week=self.screenlet.day_translation[self.screenlet.language].copy()
#dn=datetime.date.weekday(datetime.date.today()) #current day number
#week[dn]= self.screenlet.today_translation[self.screenlet.language] #show today instead of the day name
print "Connecting..."
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
screenlet_lang = str(1)
screenlet_unitsCode = str(1)
freemeteo_7d = opener.open('http://freemeteo.com/default.asp?pid=23&gid=' + CITY_ID + '&la=' + screenlet_lang + '&sub_units=' + screenlet_unitsCode)
html=freemeteo_7d.read()
print "html   ", html
print "Getting current temperature..."
#get current temperature and icon code
freemeteo_now = opener.open('http://freemeteo.com/default.asp?pid=15&gid=' + CITY_ID + '&la=' + screenlet_lang + '&sub_units=' + screenlet_unitsCode)
html_now=freemeteo_now.read()
#
print "html_now   ", html_now
current_temp_fetch=re.search('class="temp">([-]?\d+)',html_now)
print "current_temp_fetch", current_temp_fetch
if current_temp_fetch!=None:
	print "OK!"
	current_temp=current_temp_fetch.group(1)
else:
	print "FAILED!"
	current_temp=''
print "Getting current weather icon code..."
current_icon_code_fetch=re.search('/Themes/1/Default/images/logo-new.png',html_now) #ver 0.2: changed (\d+N?) to (\d+[N|F]?)
if current_icon_code_fetch!=None:
	print "OK!"
	current_icon_code='-1'  # current_icon_code_fetch.group(1)
else:
	print "FAILED!"
	current_icon_code='-1'