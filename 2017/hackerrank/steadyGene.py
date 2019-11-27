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
from sys import maxsize

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
8  
GAAATAAA
out: 5
8
GTTTCGAA
out: 1
8
GTTTCAAA
out: 3
40
TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC
out: 5
1500
"""
def mn (x, y):
    if x > y: return y
    else: return x
def fn (x):   # 0, 2, 6, 19  +1 // 3, mn (3, )  -> 0, 1, 2, 3
    xo = ord (x) - 65
    return mn (3, (xo + 1) // 3)
def steadyGene (n, gene):
    c = [0] * 4   # 0 : count of 'A', 1 : of 'C', 2 : of 'G' , 3 : of 'T'
    gc = n // 4      # optimum gene count
    # transform gene from ACGT (gene) to 0123 (genn)
#    genn = list (map (fn, gene))
#    print (genn)
    def isSteady (c):
        for v in c:
            if v > gc: return False
        return True 
    # create list of accumulated counts of ACGT
    start = 0; end = 0; mn_ = maxsize
    for i in range (n):
        c [fn (gene [i])] += 1
    if isSteady (c): return 0
    # while shfiting a window (start / end) taking out characters from count
    # within window, put back in after shift, searching for minimum size window
    for start in range (n):
        while end < n and not isSteady (c):
            c [fn (gene [end])] -= 1
            end += 1
#        print ("end += 1", end, end = ", ")
        if end == n: break
        mn_ = mn (mn_, end - start)
        c [fn (gene [start])] += 1
#        print ("start", start, "mn_", mn_, end = ", ")
    return mn_
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    gene = input ()
    result = steadyGene (n, gene)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
