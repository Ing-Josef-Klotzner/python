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

"""
10
90071992547409929007199254740993
45035996273704964503599627370497
22517998136852482251799813685249
11258999068426241125899906842625
562949953421312562949953421313
90071992547409928007199254740993
45035996273704963503599627370497
22517998136852481251799813685249
11258999068426240125899906842625
562949953421312462949953421313
out:
YES 9007199254740992
YES 4503599627370496
YES 2251799813685248
YES 1125899906842624
YES 562949953421312
NO
NO
NO
NO
NO
"""
def weight (u):
    ln = len (u)
    if ln == 0: return 0
    return v (u [0]) * ln

def v (c):
    return ord (c) - 96

# all divisors of a number
def adoan (x):
    pass
    
def separateNumbers (s, ln, lCtr_):
    if ln < 2: 
        print ("NO")
        return
    # find first two subsequence numbers
    brk1 = False
    while lCtr_ < ln:
        lCtr_ += 1   # length counter
        sp = lCtr_ // 2  # split Number count
        s1 = s [ : sp]; s2 = s [sp : lCtr_]
        nr1 = int (s1); nr2 = int (s2)
        if nr1 + 1 == nr2 and s1 [0] != '0':
            lns = len (s2)   # length of last subsequence number
#            print ()
#            print (s)
#            print ("nr1", nr1, "nr2", nr2)
#            print ("found subsequence numbers")
#            print ("split at", sp)
#            print ("length of last number:", lns)
#            print ("proceed at:", lCtr_)
            brk1 = True
            break
    if not brk1:
        print ("NO")
        return
    brk = False
    nr = nr2
    lCtr = lCtr_
    while lCtr < ln:
#        print ("lCtr", lCtr, "ln", ln)
        nr += 1
        if len (str (nr)) > lns:
            lns += 1
        sn = s [lCtr : lCtr + lns]
#        print ("nr", nr, "sn", int (sn), "lns", lns)
        if nr != int (sn):
#            print ("ungleich")
            brk = True
            break
        lCtr += lns
    if brk1 and brk:
        # there would be a "NO"
        # if there is maybe a bigger subsequence number search
        # again starting with +1 digit
        separateNumbers (s, ln, lCtr_ + 1)
        return
    print ("YES " + s1  if not brk else "NO")
    return

def main ():
#    fptr = open (environ ['OUTPUT_PATH'], 'w')
    q = int (input ())
    for _ in range (q):
        s = input ()
        ln = len (s)
        separateNumbers (s, ln, 1)
#    print (result)
#    fptr.write (result)
#    fptr.write ("\n")
#    fptr.close ()

if __name__ == '__main__':
    main ()
