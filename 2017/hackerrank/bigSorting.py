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
from sys import stdin
#from sys import setrecursionlimit
#setrecursionlimit (11000)

                
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    unsorted = []
    unsorted = [x.split () [0] for x in stdin]
    fptr.write ('\n'.join (sorted (unsorted, key = lambda x: (len(x), x))))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
