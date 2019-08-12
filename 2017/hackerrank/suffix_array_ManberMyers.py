#!/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import defaultdict

def sort_bucket (str, bucket, order):
    d = defaultdict (list)
    for i in bucket:
        key = str [i : i + order]
        d [key].append (i)
    result = []
    for k,v in sorted (d.items ()):
        if len (v) > 1:
            result += sort_bucket (str, v, order * 2)
        else:
            result.append (v [0])
    return result
 
def suffix_array_ManberMyers (str):
    return sort_bucket (str, (i for i in range (len (str))), 1)

def main ():
    a = "Missisipi"
    result = suffix_array_ManberMyers (a)
    b = ""
    for i in result:
        b += (a [i])
    print (b)
    print (result)

if __name__ == '__main__':
    main ()
