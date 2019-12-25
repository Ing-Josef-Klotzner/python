#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from sys import version_info
if version_info.major == 3:
    pass
elif version_info.major == 2:
    input = raw_input
else:
    print ("Unknown python version - input function not safe")

def growingPlant(upSpeed, downSpeed, desiredHeight):
    def grow (height = 0, days = 0):
        days += 1
        height += upSpeed
        if height >= desiredHeight: return days
        height -= downSpeed
        return grow (height, days)
    days = grow ()
    return days

def main ():
    a = 100
    b = 10
    c = 910
    print (growingPlant (a, b, c))

if __name__ == '__main__':
    main ()
