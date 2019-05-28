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

# max = 31622 ** 2 (< 10 ** 9)

def squares (a, b):
    von = int (a ** .5)
    bis = int (b ** .5)
    print (von, bis)
    return bis - von + 1 if von ** 2 == a else bis - von 

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    q = int (input ())
    for q_itr in range (q):
        ab = input ().split ()
        a = int (ab [0])
        b = int (ab [1])
        result = squares (a, b)
        print ("\n", result)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()

