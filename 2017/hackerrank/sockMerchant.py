#!/usr/bin/python3

from os import environ
from array import array


def sockMerchant (n, ar):
    socksA = array ('I', [0 for i in range (101)]) # array for 101 colors
    for col in ar:
        socksA [col] += 1
    total = 0
    for ones in socksA:
        total += ones // 2
    return total

if __name__ == '__main__':
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    ar = list (map (int, input ().rstrip ().split ()))
    result = sockMerchant (n, ar)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()
