#!/usr/bin/python3

import os
import sys
from time import sleep

def getSum (m): 
    sum_ = 0
    while (m != 0): 
        sum_ = sum_ + (m % 10) 
        m = m // 10
    return sum_

def getProd (m): 
    m_ = m
    if m != 0:
        prod = 1
    else: prod = m
    while (m != 0): 
    
        prod = prod * (m % 10) 
        m = m // 10
    return prod

def getDgtCnt (m): 
    cnt = 0
    while (m != 0): 
        m = m // 10
        cnt += 1
    return cnt
# 11111112111121111116 % 28044 == 0, 20 Stellen
# 1111111111111111111111111111111111111111111111321125 % 1355 == 0
#     52 Stellen, richtig, aber zu langsam
def numS (m):
    dgtc = dgtCntm = getDgtCnt (m)
    even = False
    def create (first_num):
        for i in range (1, dgtCntm):
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
    vold = num = first_num
    while True: #cntDgt <= dgtCnt:
        dgt = (num % (10 ** (cntDgt + 1))) // 10 ** cntDgt
        old = num
        fst = True
        while getSum (num) >= getProd (num) and dgt <= 9:
            print (num, cntDgt, end = " *, ")
            sleep (.01)
            if num % m == 0:
                return num
            if cntDgt == 0 and even:
                num += 2 * 10 ** cntDgt
                dgt += 2
            else:
                num += 10 ** cntDgt
                dgt += 1
        """
        while getSum (num) < getProd (num) or dgt > 9:
            Setze Ziffer zurück (beachte even)   *)
            setze Zähler cntDgt (+1) auf nächste Stelle und erhöhe sie
            dgt = (num % (10 ** (cntDgt + 1))) // 10 ** cntDgt
        setze Zähler cntDgt zurück auf fstCntDgt
        """
        while getSum (num) < getProd (num) or dgt >= 9:
#            print (num, end = ", ")
            num = old
#            print (num, end = ",  ")
            fst = False
#            if cntDgt == 0 and even: num -= (dgt - 2) * 10 ** cntDgt   # *)
#            else: num -= (dgt - 1) * 10 ** cntDgt
            cntDgt += 1
            if cntDgt >= dgtc:
                vold = num = vold + 10 ** cntDgt
                dgtc += 1
            else:
                num += 10 ** cntDgt
            dgt = (num % (10 ** (cntDgt + 1))) // 10 ** cntDgt
#            print (num, cntDgt, dgt, dgtc, end = ",   ")
#            sleep (.01)

#            print (num, end = ", ")
#            sleep (.01)
        cntDgt = fstCntDgt

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

