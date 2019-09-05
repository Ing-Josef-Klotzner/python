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
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def organizingContainers (n, container):
    answer = "Possible"
    # Lösung: es muss so viele x'en geben wie Kugeln im container x sind
    balls = [0] * (n + 1)
    sum_cont = [0] * (n + 1)
    for b in range (n):
        for c in range (n):
            balls [b] += container [c] [b]
            sum_cont [c] += container [c] [b]
    balls.sort ()
    sum_cont.sort ()
    if sum_cont != balls:
        answer = "Impossible"
    return answer 


def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    q = int (input ())
    for _ in range (q):
        n = int (input ())
        container = []
        for _ in range (n):
            container.append (list (map (int, input ().rstrip ().split ())))
        result = organizingContainers (n, container)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
