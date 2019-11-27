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
import os
from time import sleep

def getSum (m): 
    sum_ = 0
    while (m != 0): 
        sum_ += m % 10 
        m = m // 10
    return sum_

def getProd (m): 
    if m != 0:
        prod = 1
    else: prod = m
    while (m != 0): 
        prod *= m % 10 
        m = m // 10
    return prod

def getDgtCnt (m): 
    cnt = 0
    while (m != 0): 
        m = m // 10
        cnt += 1
    if cnt == 0: cnt = 1
    return cnt

def createMcBase (first_num, dgtc):
    for i in range (1, dgtc - 1):
        first_num *= 10
    return first_num

def numS (m):
    dgtc = getDgtCnt (m)
    even = False
    def create (first_num):
        for i in range (1, dgtc):
            first_num += 10 ** i
        return first_num
    if m % 10 == 5:
        fstCntDgt = 1
        first_num = 5
        first_num = create (first_num)
    elif m % 2 == 0:
        even = True
        fstCntDgt = 0
        first_num = 2
        first_num = create (first_num)
    else:
        fstCntDgt = 0
        first_num = 1
        first_num = create (first_num)
    cntDgt = fstCntDgt
    numc = num = first_num
    i = 0
    if m == 19425: maxcxv = 8
    elif m % 3885 == 0 or m == 16835 or m == 4095: maxcxv = 7
    else: maxcxv = 6
    maxcv = 19
    maxc = 30
    if m == 26085: maxcx = 61  # braucht 19 Stellen 
    else: maxcx = 41
    up = False
    while True:
        dgt = (num % (10 ** (cntDgt + 1))) // 10 ** cntDgt
        while getSum (num) >= getProd (num) and dgt <= 9:
            if num % m == 0:
                return num
            if cntDgt == 0 and even:
                num += 2
                dgt += 2
            else:
                num += 10 ** cntDgt
                dgt += 1
        """
        while getSum (num) < getProd (num) or dgt > 9:
            Setze Ziffer zurück (beachte even)   *)
            setze Zähler cntDgt (+1) auf nächste Stelle und erhöhe sie
            wenn sie 0 ist erhöhe sie nochmal
            dgt = (num % (10 ** (cntDgt + 1))) // 10 ** cntDgt
        setze Zähler cntDgt zurück auf fstCntDgt
        """
        while getSum (num) < getProd (num) or dgt > 9:
            if cntDgt == 0 and even: num -= (dgt - 2) * 10 ** cntDgt   # *)
            else: num -= (dgt - 1) * 10 ** cntDgt
            cntDgt += 1
            num += 10 ** cntDgt

            dgt = (num % (10 ** (cntDgt + 1))) // 10 ** cntDgt
            numdiff = num - numc

            if dgtc >= maxc and numdiff > 10 ** maxc:
                up = True
                break
            else: up = False
            if dgt == 0:
                num += 10 ** cntDgt
#                print ("0 reset", dgtc, end = ", ")
                dgtp1 = (num % (10 ** (cntDgt + 2))) // 10 ** (cntDgt + 1)
                if dgtp1 == 0:
                    num += 10 ** (cntDgt + 1)
                    print ("00 reset", dgtc, end = ", ")
                    dgtp2 = (num % (10 ** (cntDgt + 3))) // 10 ** (cntDgt + 2)
                    if dgtp2 == 0:
                        num += 10 ** (cntDgt + 2)
                        print ("000 reset", dgtc, end = ", ")
        gtdf = cntDgt + i
        if  gtdf >= dgtc or up:
            numc += 10 ** dgtc
            dgtc += 1
            if dgtc == maxc + 1: i += maxc - maxcv; maxc = maxcv; # 26085 19 braucht Stellen
            if dgtc == maxcx + 1:  # ab 42 (26085 62) Stellen
                i += maxc - maxcxv
                maxc = maxcxv
#                if maxcxv == 6 or m == 19425:
#                    break
                break
        if cntDgt >= maxc or up: # or dgtcp1:  # nur bis Stelle maxc durchzählen
            num = numc
            i += 1
        cntDgt = fstCntDgt
    print ("change to algorithm add_m")
    num = (numc // m) * m + m
    if m == 19425:
        overshot = createMcBase (69, maxc)
    else: overshot = createMcBase (49, maxc)
    while True:
        prod = getProd (num)
        if getSum (num) < prod or prod == 0:
            if getDgtCnt (num - numc + overshot) <= maxc:
                num += m
            else:
                numc += 10 ** dgtc
                dgtc += 1
                num = numc // m * m + m
        else: return num

def divisibleNumbers (n):
    if getSum (n) >= getProd (n) and getProd (n) != 0:
        return (getDgtCnt (n))
    m = numS (n)
    print (m, getDgtCnt (m))
    return getDgtCnt (m)

def divisibleNumbers_slow (n):
    for m in range (n, 100000000000, n):
        prod = getProd (m)
        if prod == 0:
            pass
        elif getSum (m) >= prod:
            print (m, getDgtCnt (m))
            return (getDgtCnt (m))
    print (m)

# type in bash:
# export OUTPUT_PATH=OUTPUT
def main ():
    fptr = open (os.environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    result = divisibleNumbers (n)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()

# 11111112111121111116 % 28044 == 0, 20 Stellen
# 25425 112111111111111111111111111125 30
# 275 32
# 1111111111111111111111111111111111111111111111321125 % 1355 == 0
#     52 Stellen, richtig, aber zu langsam
# 26085  1111111111111111111111111111111111111111117211111111111111115 61
# 3885 (braucht 7 Stellen durchgezählt) 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111116212115 109
# 16835 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111116212115 109
# 27195 (braucht 7 Stellen durchgezählt) 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111116212115 109
# 23245 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111116225 111
# 28125  1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111153125 142
# 24975 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111141525 204
# 15625 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111328125 465

