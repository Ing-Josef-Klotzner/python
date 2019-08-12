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

def rotate (ar, rt):
   rotations = rt % len (ar)
   return ar [- rotations : ] + ar [ : - rotations]

def matrixRotation (matrix, m, n, rt):
    mr = min (m, n) // 2   # max Rings
    # convert matrix to rings
    rgs = []
    for r in range (mr):
        ar = deque ()
        lucy = r; lucx = r; rucy = r; rucx = n - 1 - r
        llcy = m - 1 - r; llcx = r; rlcy = m - 1 - r; rlcx = n - 1 - r
        for y in range (lucy + 1, llcy): ar.append (matrix [y] [lucx])
        # for x in range (llcx, rlcx + 1): ar.append (matrix [llcy] [x])
        ar.extend (matrix [llcy] [llcx : rlcx + 1])
        for y in range (rlcy - 1, rucy, -1): ar.append (matrix [y] [rlcx])
        #for x in range (rucx, lucx - 1, -1): ar.append (matrix [rucy] [x])
        ar.extend (matrix [rucy] [lucx : rucx + 1] [::-1])
        # rotate ar
        ar.rotate (rt)
        rgs.append (ar)
    # convert rings back to matrix
    for r in range (mr):
        lucy = r; lucx = r; rucy = r; rucx = n - 1 - r
        llcy = m - 1 - r; llcx = r; rlcy = m - 1 - r; rlcx = n - 1 - r
        for y in range (lucy + 1, llcy): matrix [y] [lucx] = rgs [r].popleft ()
        for x in range (llcx, rlcx + 1): matrix [llcy] [x] = rgs [r].popleft ()
        for y in range (rlcy - 1, rucy, -1): matrix [y] [rlcx] = rgs [r].popleft ()
        for x in range (rucx, lucx - 1, -1): matrix [rucy] [x] = rgs [r].popleft ()
    res = ""
    for i, l in enumerate (matrix):
        if i:
            res += "\n" + "".join (map (lambda x: x + " ", map (str, l)))
        else:
            res = "".join (map (lambda x: x + " ", map (str, l)))
    return res
                
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [m, n, rt] = map (int, input ().rstrip ().split ())
    matrix = []
    for _ in range (m):
        matrix.append (list (map (int, input ().rstrip ().split ())))
    result = matrixRotation (matrix, m, n, rt)
    print (result)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
