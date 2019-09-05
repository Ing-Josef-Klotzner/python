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

def appendAndDelete (s, t, k):
    len_s = len (s)
    len_t = len (t)
    unequ = False

    if len_s > len_t: s_ = s; t_ = t; len_t_ = len_t; len_s_ = len_s
    else: s_ = t; t_ = s; len_t_ = len_s; len_s_ = len_t
    len_diff = len_s_ - len_t_; len_same = len_s_ - len_diff 
    for i in range (len_t_):
        if s_ [i] != t_ [i]:
            break
        else:
            if i + 1 == len_t_:
                i += 1
    ungleich = len_diff + (len_same - i) * 2
#    print ("ungleich", ungleich)
    
    unpair = True if k > ungleich and (k - ungleich) % 2 and k <= len_s + len_t else False
    
    no_go = ungleich > k or k == 0 and s != t or unpair
    if no_go: return "No"
    else: return "Yes"

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s = input ()
    t = input ()
    k = int (input ())
    result = appendAndDelete (s, t, k)
    print (result)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
