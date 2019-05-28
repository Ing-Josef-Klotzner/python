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
from bisect import bisect

#    position = bisect.bisect_left(l, r)
#    bisect.insort_left(l, r)

def designerPdfViewer (h, word):
#    def func (x):
#        return h [ord (x) - 97]
#    heights = map (func, word)
    heights = map (lambda x: h [ord (x) - 97], word)
    height = max (heights)
    return height * len (word)
    
def main ():
    fptr = open(environ['OUTPUT_PATH'], 'w')
    h = list (map (int, input ().rstrip ().split ()))
    word = input()
    result = designerPdfViewer (h, word)
    print (result)
    fptr.write(str (result) + '\n')
    fptr.close()

if __name__ == '__main__':
    main ()
