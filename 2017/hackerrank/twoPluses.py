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

def twoPluses (n, m, grid):
    # scan the grid vertically and then horizontally
    # mark middle of each continuous 'G' line with its count
    #     or if length is even, middle 2 with count - 1
    #   until count == 1:
    #       reduce count by 2; mark position - middle and pos + mid with count (now reduced)
    # scan horizontally in same way and put minimum of vertical and horizontal found counts
    # put counts (stars) to result list with coordinates
    # sort result list, take last 2
    # check if stars overlap, if they do remove smaller from list, again check and remove in case 
    # reload original list, check if there is larger pair not overlapping, 
    # if reducing largest star in size until size 3; resort list after reduc., then check 
    # 
    # calculating area: multiply length of stars by itself, reduce by 1
    # take maximum of product of last 2 and each single one
    sL = []
    for i in range (n):
        sL.append ([0] * m)
    start = -1
    for x in range (m):
        for y in range (n):
            pix = grid [y] [x]
            mid = (y + start) // 2
            if start == -1 and pix == 'G':
                if y == n - 1: sL [y] [x] = 1
                else: start = y
            elif start >= 0:
                if pix != 'G' or y == n - 1:
                    if y == n - 1 and pix == 'G': diff = y - start + 1
                    else: diff = y - start
                    odd = diff % 2
                    if (y != n - 1 or y == n - 1 and pix != 'G') and not odd:
                        mid -= 1
                    if not odd:
                        diff -= 1
                        sL [mid + 1] [x] = diff
                    sL [mid] [x] = diff
                    inc = 1
                    while diff >= 3:
                        diff -= 2
                        sL [mid - inc] [x] = diff
                        if odd: sL [mid + inc] [x] = diff
                        else: sL [mid + 1 + inc] [x] = diff
                        inc += 1
                    start = -1
    for l in sL:
        print ("".join (str (l)))
    # horizontally:
    hL = []
    for i in range (n):
        hL.append ([0] * m)
    start = -1
    res = []
    for y in range (n):
        for x in range (m):
            pix = grid [y] [x]
            mid = (x + start) // 2
            if start == -1 and pix == 'G':
                if x == m - 1:
                    hL [y] [x] = 1
                    if sL [y] [x] == 1: res.append ((1, y, x))
                else: start = x
            elif start >= 0:
                if pix != 'G' or x == m - 1:
                    if x == m - 1 and pix == 'G': diff = x - start + 1
                    else: diff = x - start
                    odd = diff % 2
                    if (x != m - 1 or x == m - 1 and pix != 'G') and not odd:
                        mid -= 1
                    if not odd:
                        diff -= 1
                        hL [y] [mid + 1] = diff
                        res.append ((min (diff, sL [y] [mid + 1]), y, mid + 1))
                    hL [y] [mid] = diff
                    res.append ((min (diff, sL [y] [mid]), y, mid))
                    inc = 1
                    while diff >= 3:
                        diff -= 2
                        hL [y] [mid - inc] = diff
                        res.append ((min (diff, sL [y] [mid - inc]), y, mid - inc))
                        if odd:
                            hL [y] [mid + inc] = diff
                            res.append ((min (diff, sL [y] [mid + inc]), y, mid + inc))
                        else:
                            hL [y] [mid + 1 + inc] = diff
                            res.append ((min (diff, sL [y] [mid + 1 + inc]), y, mid + 1 + inc))
                        inc += 1
                    start = -1
    res.sort ()
    reso = res [:]
    print (res)
#    del res [-2:]
    def ovlp (p1, p2):
        r2 = res [p2] [0] // 2;  r1 = res [p1] [0] // 2
        y2 = res [p2] [1]; y1 = res [p1] [1]
        x2 = res [p2] [2]; x1 = res [p1] [2]
        if (abs (y2 - y1) <= r1 and x1 >= x2 - r2 and x1 <= x2 + r2 or 
            abs (x2 - x1) <= r1 and y1 >= y2 - r2 and y1 <= y2 + r2 or
            y2 == y1 and x2 > x1 and x1 + r1 >= x2 - r2 or
            y2 == y1 and x1 > x2 and x2 + r2 >= x1 - r1 or
            x2 == x1 and y2 > y1 and y1 + r1 >= y2 - r2 or
            x2 == x1 and y1 > y2 and y2 + r2 >= y1 - r1):
            return True
        else: return False
    print (ovlp (-3, -2))
    # remove smaller star(s), if overlap
    def rmovlp ():
        while len (res) > 1:
            r2 = res [-1] [0] // 2;  r1 = res [-2] [0] // 2
            y2 = res [-1] [1]; y1 = res [-2] [1]
            x2 = res [-1] [2]; x1 = res [-2] [2]
            if (abs (y2 - y1) <= r1 and x1 >= x2 - r2 and x1 <= x2 + r2 or 
                abs (x2 - x1) <= r1 and y1 >= y2 - r2 and y1 <= y2 + r2 or
                y2 == y1 and x2 > x1 and x1 + r1 >= x2 - r2 or
                y2 == y1 and x1 > x2 and x2 + r2 >= x1 - r1 or
                x2 == x1 and y2 > y1 and y1 + r1 >= y2 - r2 or
                x2 == x1 and y1 > y2 and y2 + r2 >= y1 - r1):
                del res [-2:-1]; continue
            break
    # get list of all stars with len > 3; add all sizes of stars below max size to 3
    # to reso list; sort reso;   
    all_other_star_sizes = [(szo, y, x) for i, (sz, y, x) in enumerate (res)
        for szo in range (sz - 2, 1, -2) if sz > 3]
    print ("all other star sizes:", all_other_star_sizes)
    reso += all_other_star_sizes
    reso.sort ()
    print ("sorted reso list with all other sizes:", reso)
    #repeat this until new_max < old_max:
    # copy reso to res; remove smaller stars, if overlap from res; get maximum from mx
    # and resulting product of last two (biggest) from res; del last element from reso
    # (if len (reso) > 1
    def getMx ():
        if len (res) > 1: return (res [-1] [0] * 2 - 1) * (res [-2] [0] * 2 - 1)
        else: return -1000
    old_mx = mx = 0
    res = reso [:]
    rmovlp ()
    mx = max (mx, getMx ())
    if len (reso) > 1:
        del reso [-1]
    while mx >= old_mx and len (reso) > 1:
        old_mx = mx
        res = reso [:]
        rmovlp ()
        mx = max (mx, getMx ())
        del reso [-1]
    print (mx)
    return mx

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [n, m] = map (int, input ().split ())
    grid = []
    for _ in range (n):
        im = input ()
        grid.append (im)
    result = twoPluses (n, m, grid)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
