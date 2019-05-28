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

def catAndMouse (x, y, z):
    catA = abs (x - z); catB = abs (y - z)
    if catA == catB: return "Mouse C"
    elif catA < catB: return "Cat A"
    else: return "Cat B"

if __name__ == '__main__':
    fptr = open(environ['OUTPUT_PATH'], 'w')
    q = int (input())
    for q_itr in range (q):
        xyz = input ().split ()
        x = int (xyz [0])
        y = int (xyz [1])
        z = int (xyz [2])
        result = catAndMouse (x, y, z)
        print (result)
        fptr.write(str (result) + '\n')
    fptr.close()
