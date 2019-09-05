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
from collections import deque
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def insertionSort1 (n, arr):
    def out_arr (ar):
        for i in ar:
            print (i, end = " ")
        print ()
    last = arr [-1]
    if len (arr) == 1: out_arr (arr)
    for i in range (n - 2, - 1, -1):
        if last < arr [i]:
            arr [i + 1] = arr [i]
            out_arr (arr)
        else: 
            arr [i + 1] = last
            out_arr (arr)
            return
    arr [i] = last
    out_arr (arr)
                
def main ():
#    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    arr = deque (map (int, input ().rstrip ().split ()))
    insertionSort1 (n, arr)
#    fptr.write (str (result) + '\n')
#    fptr.close ()

if __name__ == '__main__':
    main ()
