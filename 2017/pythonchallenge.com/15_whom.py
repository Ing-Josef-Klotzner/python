#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import datetime, calendar
"""
15 whom
"""
# site = "http://www.pythonchallenge.com/pc/return/"
# opt = "uzi.html"

"""
<!-- he ain't the youngest, he is the second -->
<!-- todo: buy flowers for tomorrow -->
in picture a year 1**6, monday (0), 26th January
-> which year is this? (it is leap year - there is feb 29)
example:  today ...  Sat (5), 28th Okt 2017
datetime.datetime.today().weekday()
5
datetime.datetime.today().day
28
datetime.datetime.today().month
10
datetime.datetime.today().year
2017
"""
def reverse(lst):
#    ret =[]
#    for i in range(len(lst)):
#        ret.append(lst[-1-i])
#    return ret
##    return [lst[-1 -i] for i in range(len(lst))]
    return lst[::-1]
found = 1
#for year in reverse(range(1016,2006,20)):   # all leap years 1**6
for year in range(1016,2006,10)[::-1]:   # all leap years 1**6
    if datetime.datetime(year, 1, 26).weekday() == 0 and calendar.isleap(year):
        #print(year)   # output:  1976 1756 1576 1356 1176--> second: 1756
        if found == 2:
            print ("27.1." + str(year))
            break
        found += 1

answer_to_find = "mozart"
#print("answer to find is: ", answer_to_find)
#opt = "".join(x for x in lower(answer_to_find) if x in letters)
#print(" new site: http://www.pythonchallenge.com/pc/return/" + opt + ".html")
print("answer to find:", answer_to_find)
print("27.1.1756 is birtday of Wolfgang Amadeus Mozart")
##webbrowser.open(site + answer_to_find)


