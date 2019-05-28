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

from os import environ

def countingValleys (n, s):
    level = 0
    last_level = 0
    valleys = 0
    for step in s:
        if step == 'U': level += 1
        else: level -= 1
        if last_level == 0 and level == -1:
            valleys += 1
        #print (last_level, level)
        last_level = level
    return valleys

if __name__ == '__main__':
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    s = input ()
    result = countingValleys (n, s)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()
