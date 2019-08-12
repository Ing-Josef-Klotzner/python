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
from array import array
from bisect import bisect
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def biggerIsGreater (st):
    # go from back,
    # if next is smaller, swap them -> finish 
    # if next is greater or equal, compare next 2
    #   if next not greater any more, swap next with next greater in popped list
    #       attach the popped list sorted (should already be)
    #   if no next -> "no answer"

    s = array ('u', st)
    back = array ('u', [])
    answer = "no answer"
    while (len (s) > 1):
        back.extend (s.pop ())
        nxt = s [-1]
        this = back [-1]
        if nxt >= this:
            continue
        else:
            ins = bisect (back, nxt)  # find where to remove and insert
            s [-1], back [ins] = back [ins], nxt  # swap
            return "".join (s) + "".join (back)
    return answer    

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        s = input ()
        result = biggerIsGreater (s)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
