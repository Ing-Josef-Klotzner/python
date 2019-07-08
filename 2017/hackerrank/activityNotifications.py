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
#from collections import deque
from sys import stdin
#from statistics import median
#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
tc 1
answer: 633
9 5
2 3 4 2 3 6 8 4 5
answer: 2
6 3
2 2 2 9 1 15
answer: 2
10 3
4 5 6 2 7 1 8 0 9 3
answer: 2
14 4
5 5 5 5 10 1 1 1 4 0 2 8 3 14
answer: 5
50 8
34 26 83 26 66 26 34 83 56 88 1 5 8 8 5 1 2 35 65 33 31 30 0 200 156 22 22 22 22 33 33 33 44 4 44 44 12 82 48 25 22 22 21 12 12 33 1 1 1 9
answer: 7

"""

def countSort (n, l):
    mxVal = 201
    c = [0] * mxVal
    for i in range (n):
        c [l [i]] += 1
    res = []
    for i in range (mxVal):
        if c [i]:
            res += [i] * c [i]
    return res

class CSM: # count sort median
    def __init__(self, lst, n):
        mxVal = 201
        self.lst_size = n
        self.odd = n % 2
        self.nh = n // 2
        self.csm_size = mxVal
        self.data = [0] * mxVal
        self.fill (lst, n)
        self.init_csm ()
    def fill (self, lst, n):
        for i in range (n):
            self.data [lst [i]] += 1
    def init_csm (self):
        hc = 0
        brk = False
        for i in range (self.csm_size):
            if self.data [i]:
                if hc + self.data [i] <= self.nh:
                    hc += self.data [i]
                    continue
                hc += self.data [i]
                for ix in range (self.data [i],0,-1):
                    hc -= 1
                    if hc <= self.nh:   # hc half counter
                        self.nhdf = ix  # diff2nh
                        self.nhnr = i   # nh number (in half of list)
                        brk = True
                        break
            if brk: break
    def csm (self):
        if self.odd:
            return self.nhnr
        else:
            if self.nhdf > 1: nh_1 = self.nhnr
            else:   # nh_1 is number in nh - 1
                nh_1 = self.nhnr - 1
                while not self.data [nh_1]: nh_1 -= 1
            return (nh_1 + self.nhnr) / 2
    def qu_csm (self, fst, new):   # queue - drop fst, add new
        self.data [fst] -= 1
        self.data [new] += 1
        if (fst == new or fst < self.nhnr and new < self.nhnr or
            fst > self.nhnr and new >= self.nhnr or
            fst == self.nhnr and new > self.nhnr 
                and self.data [self.nhnr] >= self.nhdf): pass
        elif (fst < self.nhnr and new >= self.nhnr or
            fst == self.nhnr and new > self.nhnr):
            if self.nhdf < self.data [self.nhnr]: self.nhdf += 1
            else:
                self.nhnr += 1
                while not self.data [self.nhnr]: self.nhnr += 1
                self.nhdf = 1
        elif (fst >= self.nhnr and new < self.nhnr):
            if self.nhdf > 1: self.nhdf -= 1
            else:
                self.nhnr -= 1
                while not self.data [self.nhnr]: self.nhnr -= 1
                self.nhdf = self.data [self.nhnr]
    def median (self):  # via creating sorted list (O (n))
        l = self.srt_lst ()
        nh = self.nh
        odd = self.odd
        return l [nh] if odd else (l [nh - 1] + l [nh]) / 2
    # fill a list to 'count array'
    def srt_lst (self):
        res = []
        for i in range (self.csm_size):
            if self.data [i]:
                res += [i] * self.data [i]
        return res

def activityNotifications (exptr, n, d):
    odd = d % 2
    dh = d // 2
    def get_med (seq):
        return seq [dh] if odd else (seq [dh - 1] + seq [dh]) / 2
    act = 0
    if n < 100 and d < 100:
        for i in range (d, n):
            md = get_med (sorted (exptr [i - d : i]))
            if exptr [i] >= md * 2:
                act += 1
        return act
    else:
        lst = CSM (exptr [ : d], d)
        for i in range (d, n):
            md = lst.csm ()
            if exptr [i] >= md * 2:  #lst.median () * 2: # md * 2:
                act += 1
            lst.qu_csm (exptr [i - d], exptr [i])
        return act

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [n, d] = map (int, input ().split ())
    #expenditure = list (map (int, stdin.readline ().rstrip ().split ()))
    expenditure = [int (x) for x in stdin.readline ().split ()]
    result = activityNotifications (expenditure, n, d)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
