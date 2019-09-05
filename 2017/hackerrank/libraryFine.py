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
#from sys import setrecursionlimit

#setrecursionlimit (11000)

def libraryFine (d1, m1, y1, d2, m2, y2):
    #print (d1, m1, y1, d2, m2, y2)
    if y1 == y2 and m1 == m2 and d1 > d2:
        return (d1 - d2) * 15
    if y1 == y2 and m1 > m2:
        return (m1 - m2) * 500
    if y1 > y2:
        return 10000
    return 0
        
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    d1M1Y1 = input ().split ()
    d1 = int (d1M1Y1 [0])
    m1 = int (d1M1Y1 [1])
    y1 = int (d1M1Y1 [2])
    d2M2Y2 = input ().split ()
    d2 = int (d2M2Y2 [0])
    m2 = int (d2M2Y2 [1])
    y2 = int (d2M2Y2 [2])
    result = libraryFine (d1, m1, y1, d2, m2, y2)
    print ("\n", result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
