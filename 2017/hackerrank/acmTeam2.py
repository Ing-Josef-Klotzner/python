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
from itertools import combinations
#from sys import setrecursionlimit
#setrecursionlimit (11000)
# tc1:
# 97
# 5
def acmTeam (n, m, topic):
#    # convert topic list to int
#    tpcNrs = list (map (lambda x: int (x, 2), topic))
#    # create one_bon from bitwise or of all combinations of attendee pair topics
#    # ["1" bits of number (one_bon), count of number (cof_nr)]
#    cof_nr = 0
#    mx = 0
#    for i in range (n - 1):
#        for j in range (i + 1, n):
#            nr = tpcNrs [i] | tpcNrs [j]
#            one_bon = bin (nr).count ("1")
#            if one_bon > mx:
#                mx = one_bon
#                cof_nr = 1
#            elif one_bon == mx:
#                cof_nr += 1
#    return (mx, cof_nr)
    # convert topic list to int
    tpcNrs = list (map (lambda x: int (x, 2), topic))
#    create combinations of attendee pair topics
    comb = combinations (tpcNrs, 2)
    mx = 0
    count = 0
#     ("1" bits of number (one_bon), count of number (count))
    for i in comb:
        one_bon = bin (i [0] | i [1]).count('1')
        if one_bon > mx:            
            mx = one_bon
            count = 1
        elif one_bon == mx:
            count += 1
    return (mx, count)

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [n, m] = map (int, input().split ())
    topic = []
    for _ in range (n):
        topic_item = input ()
        topic.append (topic_item)
    result = acmTeam (n, m, topic)
    print ("\n", result)
    fptr.write ('\n'.join (map (str, result)))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
