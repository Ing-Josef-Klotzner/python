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

def queensAttack (n, k, r_q, c_q, obstacles):
    # A single cell may contain more than one obstacle -> does not matter
    print (obstacles)
    # reduce obstacles just to maximum closest 8 around queen
    # go through all obstacles: 
    #   is obst on same row, same column, same diagonal 1 or same diagonal 2 as queen?
    #   if yes: if lower: store closer - this or last lower obstacle
    #           if higher: store closer - this or last higher obstacle
    # resulting in max 8 closest obstacles   (d1 columns up, d2 columns down)
    # lower row obst (lr), higher row obst (hr), lower col obst (lc), higher col obst (hc)
    # lower d1 obst (lu), higher d1 obst (hu), lower d2 obst (ld), higher d2 obst (hd)
    # initialize to outer limits:
    lr = (r_q, 0); hr = (r_q, n + 1); lc = (0, c_q); hc = (n + 1, c_q)
    if c_q > r_q: 
        lu = (0, c_q - r_q)
        hu = (r_q + n + 1 - c_q, n + 1)
    elif c_q < r_q:
        lu = (r_q - c_q, 0)
        hu = (n + 1, c_q + n + 1 - r_q)
    else:
        lu = (0, 0)
        hu = (n + 1, n + 1)
    if n + 1 - c_q < r_q:
        ld = (r_q - (n + 1 - c_q), n + 1)
        hd = (n + 1, r_q + (n + 1 - c_q))
    elif n + 1 - c_q > r_q:
        ld = (0, r_q + c_q)
        hd = (r_q + c_q, 0)
    else:
        ld = (0, n + 1)
        hd = (n + 1, 0)
    print (lr, hr, lc, hc, lu, hu, ld, hd)
    # narrow down the obstacles around queen
    for ob in obstacles:
        if ob [0] == r_q:
            if ob [1] < c_q: lr = max (lr, ob)
            else: hr = min (hr, ob)
        if ob [1] == c_q:
            if ob [0] < r_q: lc = max (lc, ob)
            else: hc = min (hc, ob)
        if r_q - ob [0] == c_q - ob [1]:
            if ob [0] < r_q: lu = max (lu, ob)
            else: hu = min (hu, ob)
        if r_q - ob [0] == ob [1] - c_q:
            if ob [0] < r_q: ld = max (ld, ob)
            else: hd = min (hd, ob)
    print (lr, hr, lc, hc, lu, hu, ld, hd)

    # count of attack positions (cap)
    cap = 0
    cap += c_q - lr [1]  +  hr [1] - c_q +  r_q - lc [0] +  hc [0] - r_q
    cap += c_q - lu [1]  +  hu [1] - c_q  +  r_q - ld [0] + hd [0] - r_q - 8
    return cap

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [n, k] = map (int, input().split ())
    [r_q, c_q] = map (int, input().split ())
    obstacles = []
    for _ in range (k):
        obstacles.append (tuple (map (int, input ().rstrip ().split ())))
    result = queensAttack (n, k, r_q, c_q, obstacles)
    print ("\n", result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
