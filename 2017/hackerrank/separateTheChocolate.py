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
from copy import deepcopy
#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
solution pattern (chocolate part can only grow with this patterns):
m == n: solution times 4 directions times 2 (changed owner of chocolate)
ungleich: (solution h + solution v) * 2

DDDDDDD   DDDDDDDD
D         ..D.....  combinations of crossing path !!
DDDDDDD   .DDDDDD.
D         ...D....
DDDDDDD   .DDDDDD.
D         ........ 

3 3 4 
UDD
UUT
UTT
2?

2 6 0
TTTUTU
TUUDUU

1

3 3 9
UUU
UDU
UTU

13

4 8 29
UUUUUUUU
DDDUDDDD
UUUUUUUU
UUUUUUUU

4

5 7 15
UUUUUUU
UUUUUUU
UUDUUUU
UUDUUUU
UUUUUUU

1244
"""

def separateTheChocolate (chocolate, m, n, k):
    o = m - 1; p = n - 1
    # only squares
    def rotate_ (choc, rot):
        q = len (choc); r = len (choc [0])
        s = q - 1; t = r - 1
        res = deepcopy (choc)
        rot = rot % 4
        if rot:
            for  i in range (q):
                for j in range (r):
                    if rot == 1: res [j] [t - i] = choc [i] [j]
                    if rot == 2: res [s - i] [t - j] = choc [i] [j]
                    if rot == 3: res [s - j] [i] = choc [i] [j]
            return res
        else: return choc
    def rotate (choc, rot):
        q = len (choc); r = len (choc [0])
        rot = rot % 4
        u = max (q, r); v = u - 1
#        s = q - 1; t = r - 1
        res = [[g for g in range (u)] for h in range (u)]   # create (res choc)
        if rot:
            for  i in range (q):
                for j in range (r):
                    if rot == 1:
                        res [j] [v - i] = choc [i] [j]
                    if rot == 2: res [v - i] [v - j] = choc [i] [j]
                    if rot == 3:
                        res [v - j] [i] = choc [i] [j]
            # remove unnecessary lines / columns
            if q > r and rot == 1: del (res) [r : ]  # remove lines after
            if q > r and rot == 3: del (res) [ : q - r]  # remove lines before
            if q < r and rot == 2: del (res) [ : r - q]  # remove lines before
            if q > r and rot == 2:   # remove columns before
                for i in range (q): del (res [i]) [ : q - r]
            if q < r and rot == 1:   # remove columns before
                for i in range (r): del (res [i]) [ : r - q]
            if q < r and rot == 3:   # remove columns after
                for i in range (r): del (res [i]) [q: ]
            return res
        else: return choc
    def find (c): # just for single line
        d = [];  l = max (m, n)
        for i in range (l):
            if m == 1 and c == chocolate [0] [i]: d.append (i)
            elif n == 1 and c == chocolate [i] [0]: d.append (i)
        return d
    def find2 (c, choci = chocolate):
        e = len (choci); f = len (choci [0])
        d = []
        for y in range (e):
            for x in range (f):
                if c == choci [y] [x]: d.append ((y, x))
        return d
    def maskU (xmax, posu):  # just for visualizes
        e = len (xmax); f = len (xmax [0])
        res = [['.' for g in range (f)] for h in range (e)]
        for y, x in posu:
            res [y] [x] = 'U'
        return res
    def count (b, e): # just for single line
        cnt = 0
        for i in range (b, e):
            if abs (r - 1 - i - i) <= k: cnt += 1
        return cnt
    def oppCrns (a, b):
        if a and b:
            # check if a and b are on diagonal corners
            return ((0,0) in a and (o,p) in b or (0,p) in a and (o,0) in b or
                    (0,0) in b and (o,p) in a or (0,p) in b and (o,0) in a)
    if m == 0 or n == 0: return 0
    if m == 1 and n == 1: return 1  # testcase: 1 (unteilbares?) Stück = 1 Teilung !!!
    if m == 1 or n == 1:
        r = max (m, n) - 1
        D = find ('D'); T = find ('T')
        if D and T:
            if D [0] > T [0]: D, T = T, D
            cnt = count (D [-1], T [0])
            return cnt
        elif D or T:
            if T: D = T
            cnt = count (D [-1], r)
            cnt += count (0, D [0])
            return cnt
        else: return count (0, r)
    D = find2 ('D'); T = find2 ('T'); U = find2 ('U')
    print (D)
    print (T)
    ld = len (D); lt = len (T)
    if m == 2 and n == 2:
        if ld == 4 or lt == 4: return 0
        if ld == 3 or lt == 3:
            if k >= 2: return 1
            else: return 0
        if ld == 2 and lt == 2 : return 1
        if ld == 2:
            if (0,0) in D and (o,p) in D or (0,p) in D and (o,0) in D:
                if lt == 1: 
                    if k > 1: return 1
                    else: return 0
                else: return 2
            return 1  # k irrelevant (symmetric)
        if lt == 2:
            if (0,0) in T and (o,p) in T or (0,p) in T and (o,0) in T:
                if ld == 1: 
                    if k > 1: return 1
                    else: return 0
                else: return 2
            return 1  # k irrelevant (symmetric)
        if D and T:
            if oppCrns (D, T):
                if k >= 2: return 4
                else: return 2
            else: return 2
        if D or T: 
            return 4
        else:
            if k > 1: return 12  # 3 possibilities times 4 directions
            else: return 4
    if m == 2 or n == 2:
        ch = chocolate
        if D or T: 
            if k >= 2: return 4
            elif n == 2:
                ch = rotate (chocolate, 1)
            else:
                ch = chocolate
                if (ch [0] [0] == 'D' and ch [1] [0] == 'D' or
                    ch [0] [0] == 'T' and ch [1] [0] == 'T' or
                    ch [0] [p] == 'D' and ch [1] [p] == 'D' or
                    ch [0] [p] == 'T' and ch [1] [p] == 'T'):
                    return 1
                else:
                    return 2
        else: 
            if k >= 2: return 8
            else: return 4
    XFmax = [['X','X','X','X','X','X','X','X'],
            ['X','.','.','.','.','.','.','.'],
            ['X','X','X','X','X','X','X','.'],
            ['X','.','.','.','.','.','.','.'],
            ['X','X','X','X','X','X','X','.'],
            ['X','.','.','.','.','.','.','.'],
            ['X','X','X','X','X','X','X','.'],
            ['X','.','.','.','.','.','.','.']]
    XXFmax = [['X','X','X','X','X','X','X','X'],
            ['.','X','X','X','X','X','X','.'],
            ['.','X','X','X','X','X','X','.'],
            ['.','X','X','X','X','X','X','.'],
            ['.','X','X','X','X','X','X','.'],
            ['.','X','X','X','X','X','X','.'],
            ['.','X','X','X','X','X','X','.'],
            ['.','.','.','.','.','.','.','.']]
    xXFmax = [['X','X','X','X','X','X','X','X'],
            ['.','.','.','.','.','.','.','.'],
            ['.','X','X','X','X','X','X','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','X','X','X','X','X','X','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','X','X','X','X','X','X','.'],
            ['.','.','.','.','.','.','.','.']]
    XXFmin = [['.','X','X','X','X','X','X','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','X','X','X','X','X','X','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','X','X','X','X','X','X','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','X','X','X','X','X','X','.'],
            ['.','.','.','.','.','.','.','.']]
    XXmin = XXmax = XXmx = XXmn = UXmin = []
    posXXmax = posXXmin = posXXmx = posXXmn = posXU = []
    UXmin = []
    if n >= 4:
        XXmin = [i [ : 1] + i [1 : p] + i [7 : ] for i in XXFmin [ : m]]
        XXmax = [i [ : 1] + i [1 : p] + i [7 : ] for i in XXFmax [ : m]]
        xXmax = [i [ : 1] + i [1 : p] + i [7 : ] for i in xXFmax [ : m]]
        if m == 4 or m == 6: XXmax [o] = XXFmax [-1] [ : m]
        if m == 5 or m == 7:
            XXmx = [i [ : 1] + i [1 : p] + i [7 : ] for i in XXFmax [1 : m + 1]]
            XXmn = [i [ : 1] + i [1 : p] + i [7 : ] for i in XXFmin [1 : m + 1]]
            posXXmx = find2 ('X', XXmx); posXXmn = find2 ('X', XXmn)
            XXmax [o] [0] = 'X'; XXmax [o] [p] = 'X'
            xXmax [o] [0] = 'X'; xXmax [o] [p] = 'X'
        posXXmax = find2 ('X', XXmax); posXXmin = find2 ('X', XXmin)
        kXIst = len (find2 ('X', xXmax)) - len (find2 ('.', xXmax))
        print (kXIst) 
        posXU = posXXmin + find2 ('.', xXmax)
        UXmin = maskU (XXmax, posXU)   # just to visualize - don't need'
    XXRmin = []; XXRmax = []
    posXXRmax = posXXRmin = posXXRmx = posXXRmn = posXUR = []
    if m >= 4: # swapped dimensions for fitting rotated choci
        XXRmin = [i [ : 1] + i [1 : o] + i [7 : ] for i in XXFmin [ : n]]
        XXRmax = [i [ : 1] + i [1 : o] + i [7 : ] for i in XXFmax [ : n]]
        xXRmax = [i [ : 1] + i [1 : o] + i [7 : ] for i in xXFmax [ : n]]
        if n == 4 or n == 6: XXRmax [o] = XXFmax [-1] [ : n]
        if n == 5 or n == 7:
            XXRmx = [i [ : 1] + i [1 : o] + i [7 : ] for i in XXFmax [1 : n + 1]]
            XXRmn = [i [ : 1] + i [1 : o] + i [7 : ] for i in XXFmin [1 : n + 1]]
            posXXRmx = find2 ('X', XXRmx); posXXRmn = find2 ('X', XXRmn)
            XXRmax [p] [0] = 'X'; XXRmax [p] [o] = 'X'
            xXRmax [p] [0] = 'X'; xXRmax [p] [o] = 'X'
        posXXRmax = find2 ('X', XXRmax); posXXRmin = find2 ('X', XXRmin)
        kXRIst = len (find2 ('X', xXRmax)) - len (find2 ('.', xXRmax))
        print (kXRIst) 
        posXUR = posXXRmin + find2 ('.', xXRmax)
        UXRmin = maskU (XXRmax, posXUR)   # just to visualize - don't need'
    print ("UXmin")
    for i in UXmin:
        print (i)
    print ("UXRmin")
    for i in UXRmin:
        print (i)
    print ()
    for i in XXmn:
        print (i)
    print ("<- XXmn   XXmx ->")
    for i in XXmx:
        print (i)
    Xmin = Xmax = XRmin = XRmax = []
    posXmax = posXmin = posU = posXRmax = posXRmin = posUR = []
    Umin = []; URmin = []
    z = 0; zz = 0
    if not m % 2: z = 1
    if n >= 3:
        if m == 3: Xmax = [i [ : n] for i in XFmax [ : m]]
        else: Xmax = [i [ : p] + i [7 : ] for i in XFmax [ : m]]
        if m % 2: Xmax [o] [p] = 'X'
        Xmin = [i [ : p] for i in XFmax [ : m - z]]
        kIst = len (find2 ('X', Xmax)) - len (find2 ('.', Xmax))
        print (kIst)
        posXmax = find2 ('X', Xmax)
        posXmin = find2 ('X', Xmin)
        posU = posXmin + find2 ('.', Xmax)
        Umin = maskU (Xmax, posU)  # just to visualize - don't need'
    if not n % 2: zz = 1
    if m >= 3:
        if n == 3: XRmax = [i [ : m] for i in XFmax [ : n]]
        else: XRmax = [i [ : o] + i [7 : ] for i in XFmax [ : n]]
        if n % 2: XRmax [p] [o] = 'X'
        XRmin = [i [ : o] for i in XFmax [ : n - zz]]
        kRIst = len (find2 ('X', XRmax)) - len (find2 ('.', XRmax))
        print (kRIst)
        posXRmax = find2 ('X', XRmax)
        posXRmin = find2 ('X', XRmin)
        posUR = posXRmin + find2 ('.', XRmax)
        URmin = maskU (XRmax, posUR)   # just to visualize - don't need'
    print ("Xmax:")
    for i in Xmax:
        print (i)
    print ("XRmax")
    for i in XRmax:
        print (i)
    print ("Xmin:")
    for i in Xmin:
        print (i)
    print ("XRmin")
    for i in XRmin:
        print (i)

    # just to visualize - don't need'
    print ("Umin")
    for i in Umin:
        print (i)
    print ("UXmin")
    for i in UXmin:
        print (i)
    print ()
    def allXnoY (x, y, dr, posx = posXmin, posxR = posXRmin, posmx = posXmax, posmxR = posXRmax):
        posxm = posxR if dr % 2 else posx
        posxmx = posmxR if dr % 2 else posmx
        if x:
            for i in x:
                if i not in posxmx: return False
        if y:
            for i in y:
                if i in posxm: return False
        if not x and not y: return False
        return True
    def allU (U, dr, posU = posU, posUR = posUR):
        if dr % 2: posu = posUR
        else: posu = posU
        for i in posu:
            if i not in U: return False
        return True
    # check for all 4 directions of chocolate, if Ds or Ts fit in Xmin
    # if 'D' fit means, no 'T' fit into Xmin
    # if f.e. 'D' fits, check if upper right corner is an 'U' (if, * 2 possibilities)
    # if n != 8: if m % 2: if lower right corner is an 'U' -> * 2 possibilities
    # check rotation 0 (as it is):
    res = res_ = res3 = resX = rsX = rsX_ = rsXo = rsXu = 0
    for dr in [0, 2, 1, 3]:
        chocR = rotate (chocolate, dr)
        if dr == 1: 
            m, n = n, m
            o, p = p, o
        for i in chocR:
            print (i)
        print (dr)
        if dr % 2: ki = kRIst; kxi = kXRIst
        else: ki = kIst; kxi = kXIst
        D = find2 ('D', chocR); T = find2 ('T', chocR); U = find2 ('U', chocR)
        for d, t in [(D, T), (T, D)]:
            chcD0 = []; chcT0 = []
            if d: chcD0 = chocR [d [0] [0]] [d [0] [1]]
            if t: chcT0 = chocR [t [0] [0]] [t [0] [1]]
            d0isD = True if (chcD0 == 'D' or chcT0 == 'T') else False
            d0isT = True if (chcD0 == 'T' or chcT0 == 'D') else False
            if allXnoY (d, t, dr) or allU (U, dr):
                urU = chocR [0] [p] == 'U'
                llU = chocR [o] [0] == 'U'; rlU = chocR [o] [p] == 'U'
                Ucs = urU + rlU if m % 2 else urU + llU if n != 8 else urU
                if k >= abs (kxi - 2 * Ucs): res_ = 2 ** Ucs
                print (k, kxi, Ucs)
#                if urU and k >= abs (ki - 2): res_ = 2
#                elif k >= abs (ki): res_ = 1
#                if n != 8 and m % 2 and rlU:
#                    if urU and k >= abs (ki - 4) or not urU and k >= abs (ki - 2): res_ *= 2
#                if not m % 2 and llU and k >= abs (ki - 2): res_ *= 2
                if m == 3 and k > 7:
                    if (not d and not t or 
                        d0isD and chocR [0] [p] != 'T' and
                        chocR [1] [p] != 'T' and chocR [o] [p] != 'T' or
                        d0isT and chocR [0] [p] != 'D' and
                        chocR [1] [p] != 'D' and chocR [o] [p] != 'D'): 
                            if m == 3 and n == 3: res3 = 1 # one hole in the middle
                            else: res3 = 2
            if (allXnoY (d, t, dr, posXXmin, posXXRmin, posXXmax, posXXRmax) or
                allU (U, dr, posXU, posXUR)) and m > 3 and k >= abs (kxi): # and not m % 2:
                # find all combinations for linking even lines (0 to 6)
                # check if all crossings are NOT other(s) part
                for y in range (1, min (6, o), 2):
#                    ntAloP = (ntAloP and not
#                    (d0isD and all ([chocR [y] [x] == 'T' for x in range (1, p)]) or
#                    d0isT and all ([chocR [y] [x] == 'D' for x in range (1, p)])))
                    ln = True
                    for x in range (1, p):
                        choyx = chocR [y] [x]
                        ln = ln and ((d0isD and choyx == 'T') or
                                    d0isT and choyx == 'D')
                    chLn = chocR [y] [1 : p]
                    Xs = max (len (find2 ('D', chLn) if d0isD else []), 
                                len (find2 ('T', chLn) if d0isT else []))
                    if ln or Xs > 1:
                        resX = 0
                        break
                    Us = len (find2 ('U', chLn))
                    if Xs == 1: 
                        print ("Xs 1")
                        resX = resX if resX else 1
                    elif (not d and not t and dr < 2) or (d or t):
                        resX = resX * Us if resX else Us
                    else: resX = 0; break
                ulU = chocR [0] [0] == 'U'; urU = chocR [0] [p] == 'U'
                llU = chocR [o] [0] == 'U'; lrU = chocR [o] [p] == 'U'
                Ucs = ulU + urU + llU + lrU if m == 5 or m == 7 else ulU + urU
                if k >= abs (kxi - 2 * Ucs): resX *= 2 ** Ucs
            if (allXnoY (d, t, dr, posXXmn, posXXRmn, posXXmx, posXXRmx) or
                allU (U, dr, posXU, posXUR)):
                for y in range (0, m, 2):
                    if y == 2 or (m == 7 and y == 4):
                        ln = True
                        for x in range (1, p):
                            choyx = chocR [y] [x]
                            ln = ln and ((d0isD and choyx == 'T') or
                                        d0isT and choyx == 'D')
                        chLn = chocR [y] [1 : p]
                        Xs = max (len (find2 ('D', chLn) if d0isD else []), 
                                    len (find2 ('T', chLn) if d0isT else []))
                        if ln or Xs > 1:
                            print ("break for", y)
                            rsX = 0
                            break
                        Us = len (find2 ('U', chLn))
                        if Xs == 1: 
                            print ("xs 1")
                            rsX = rsX if rsX else 1
                        elif (not d and not t and dr < 2) or (d or t):
                            rsX = rsX * Us if rsX else Us
                        else: rsX = 0; break
                    if y == 0:
                        chLn = [chocR [y] [ : n]] + [chocR [1] [ : 1] + 
                                ['.'] * (n-2) + chocR [1] [p : ]]
                        Xs = max (len (find2 ('D', chLn) if d0isD else []),
                                len (find2 ('T', chLn) if d0isT else []))
                        if Xs > 1:
                            rsXo = 0
                            break
                        Us = len (find2 ('U', chLn))
                        if Xs == 1:
                            print ("xso 1")
                            rsXo = rsXo if rsXo else 1
                        elif (not d and not t and dr < 2) or (d or t): 
                            rsXo = rsXo * Us if rsXo else Us
                        else: rsXo = 0; break
                    if y == o:
                        chLn = [chocR [o - 1] [ : 1] + ['.'] * (n - 2) +
                                chocR [o - 1] [p : ]] + [chocR [y] [ : n]]
                        Xs = max (len (find2 ('D', chLn) if d0isD else []),
                                len (find2 ('T', chLn) if d0isT else []))
                        if Xs > 1:
                            rsXu = 0
                            break
                        Us = len (find2 ('U', chLn))
                        if Xs == 1:
                            print ("xsu 1")
                            rsXu = rsXu if rsXu else 1
                        elif (not d and not t and dr < 2) or (d or t): 
                            rsXu = rsXu * Us if rsXu else Us
                        else: rsXu = 0; break
                    rsX_ = rsXo + rsXu
            print (res, res_, resX, rsX, rsX_, end = ", ")
            res += res_ + resX + rsX * rsX_  #+ res3
            res_ = 0; resX = 0; rsX = 0; rsX_ = rsXo = rsXu = 0
        print ()
    return res + res3
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [m, n, k] = map (int, input ().rstrip ().split ())
    chocolate = []
    for _ in range (m):
        hm = input ()
        chocolate.append (list (hm))
    result = separateTheChocolate (chocolate, m, n, k)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
