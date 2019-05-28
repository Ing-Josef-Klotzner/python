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

def climbingLeaderboard (sc, scores, alice):
    # create rankList from scores
    rank = 1
    rankList = []; result = []
    rev_scores = scores [ : : -1]
    last_score = scores [0]
    for score in scores:
        if score != last_score: rank += 1
        rankList.append (rank)
        last_score = score
#    print (rankList)
    for ali_rank in alice:
        pos = sc - bisect (rev_scores, ali_rank)
        if pos != 0:
            res = rankList [pos - 1] + 1
            result.append (str(res) + "\n")
#            print (result)
        else: 
            res = 1
            result.append (str (res) + "\n")
#            print (result)
    return "".join (result)
    
def main ():
    fptr = open(environ['OUTPUT_PATH'], 'w')
    scores_count = int (input())
    scores = list (map (int, input ().rstrip ().split ()))
    alice_count = int (input ())
    alice = list (map (int, input ().rstrip ().split ()))
    result = climbingLeaderboard (scores_count, scores, alice)
    print (result)
    fptr.write(str (result) + '\n')
    fptr.close()

if __name__ == '__main__':
    main ()
