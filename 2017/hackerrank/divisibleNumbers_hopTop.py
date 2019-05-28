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
import sys
from time import sleep

def getSum (m):
    m = abs (m)
    sum_ = 0
    while (m != 0): 
        sum_ += m % 10 
        m = m // 10
    return sum_

def getProd (m): 
    m = abs (m)
    if m != 0:
        prod = 1
    else: prod = m
    while (m != 0): 
        prod *= m % 10 
        m = m // 10
    return prod

def getDgtCnt (m): 
    m = abs (m)
    cnt = 0
    while (m != 0): 
        m = m // 10
        cnt += 1
    if cnt == 0: cnt = 1
    return cnt
# 11111112111121111116 % 28044 == 0, 20 Stellen
# 25425 112111111111111111111111111125 30
# 275 11111111111111111111111111114125 32
# 1111111111111111111111111111111111111111111111321125 % 1355 == 0
#     52 Stellen, richtig, aber zu langsam (mit divisibleNumbers_slow)
# 26085  1111111111111111111111111111111111111111117211111111111111115 61
# 3885 (braucht 7 Stellen durchgezählt) 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111116212115 109
# 16835 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111116212115 109
# 27195 (braucht 7 Stellen durchgezählt) 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111116212115 109
# 23245 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111116225 111
# 28125  1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111153125 142
# 24975 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111141525 204
# 15625 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111328125 465
# 21915 -> 22115   211915 -> 212115
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
    if m % 3885 == 0 or m == 16835: maxcxv = 7
    else: maxcxv = 6
    maxcv = 19
    maxc = maxci = 30
    if m == 26085: maxcx = 61  # braucht 19 Stellen 
    else: maxcx = 41
#    maxcx = 61
    up = False
    dgtcp1 = False
    maxCntDgt = fstCntDgt
    preNumNxt = num
    while True:
        dgt = (num % (10 ** (cntDgt + 1))) // 10 ** cntDgt
#        ctdiff = 0
#        print (num, numc, dgtc, end = ", ")
#        sleep (.01)
        cfv = True # come from valid
        while getSum (num) >= getProd (num) and dgt <= 9:
#            if dgtc == 31:
#                print ("s", num, num - numc, dgtc, cntDgt, maxc, end = " *, ")
#                sleep (.001)
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
#            if dgtc > 60 and dgtc < 63:
#                print ("a ", num, maxCntDgt + 1, dgtc, cntDgt, dgt, i, end = ", ")
            if dgt == 2 and cntDgt == fstCntDgt and maxCntDgt + 1 == dgtc and cfv:
                dgtcp1 = True # 1*)
#                cntDgt = maxCntDgt
#                break
            else: dgtcp1 = False
            cfv = False
            if cntDgt == 0 and even: num -= (dgt - 2) * 10 ** cntDgt   # *)
            else: num -= (dgt - 1) * 10 ** cntDgt
            cntDgt += 1
            num += 10 ** cntDgt

# 8112 -> 9111   instead   8112 -> 8121 -> 8211 -> 9111

            # maxCntDgt ermitteln und einsetzen wenn dgt = 2 dann bei 1*) cntDgt auf 
            # maxCntDgt setzen und digit rücksetzen und nächste erhöhen
            maxCntDgt = max (cntDgt, maxCntDgt)
            if dgtcp1:
                cntDgt = maxCntDgt
            dgt = (num % (10 ** (cntDgt + 1))) // 10 ** cntDgt
            numdiff = num - numc

            if dgtc >= maxc and numdiff > 10 ** maxc:
#                ctdiff = getDgtCnt (numdiff) - cntDgt - 1
                up = True
                break
            else: up = False
            if dgtcp1: #(dgt - 1) * 10 ** cntDgt == numdiff and dgtcp1:
                if dgt == 9 or cntDgt + 1 == dgtc:
                    preNumNxt = numc + 10 ** (cntDgt + 1)
                    cntDgt += 1
                else:
                    preNumNxt = numc + dgt * 10 ** cntDgt
#                if dgtc > 60 and dgtc < 63:
#                    print (" preNum ", preNumNxt, " num ", num," cntDgt ", cntDgt, end = ", ")
#                    sleep (.01)
                break
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
#            if dgtc > 60 and dgtc < 63:
#                print ("b ", num, num - numc, dgtc, cntDgt, dgt, i, end = ", ")
#                sleep (.01)
#        if dgtc == 200:
#            print (num, num - numc, cntDgt, dgtc, i, end = ",  ")
        gtdf = cntDgt + i
#        if dgtcp1:
#            numc += 10 ** gtdf
#            dgtc += 1
        if  gtdf >= dgtc or up: # and not dgtcp1:
#            maxCntDgt = fstCntDgt
            numc += 10 ** dgtc
            dgtc += 1
#            print (numc, cntDgt, dgtc, end = ", ")
            if dgtc == maxc + 1: i += maxc - maxcv; maxc = maxcv; maxCntDgt -= i + 2; # print ("m ", num, num - numc, maxCntDgt + 1, dgtc, cntDgt, dgt, i, end = ", ") # 26085 19 braucht Stellen
            if dgtc == maxcx + 1: i += maxc - maxcxv; maxc = maxcxv; maxCntDgt -= i + 2 # ab 42 (26085 62) Stellen
        if cntDgt >= maxc or up: # or dgtcp1:  # nur bis Stelle maxc durchzählen
            num = numc
            i += 1
        if dgtcp1:
            num = preNumNxt
            dgtcp1 = False
#            print (" preNumNxt ", end = ", ")
        cntDgt = fstCntDgt
# tc 46 59 68 falsch
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
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = divisibleNumbers(n)

    fptr.write(str(result) + '\n')

    fptr.close()

