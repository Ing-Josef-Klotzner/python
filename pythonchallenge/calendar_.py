#! /usr/bin/env python2
# calendar.py  --  created by Ing. Josef KlotzneIr
import datetime
from calendar import isleap,weekday
for year in range(1996,1582,-20):
    if datetime.date(year, 1, 1).weekday() == 3:   # 3=Thursday
        print year,
print filter(lambda y: isleap(y) and 0 == weekday(y, 1, 26), range(1006, 2000, 10))[-2]
