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

def buildString (n, a, b, s):
    if a != 0:
        cheapersub = b // a
    else:
        cheapersub = 10000
    d = dict ()
    # dict for costs
    dc = dict ()
    pos = 2
    cost = a * 2
    infinite = 1000000000
    for i in range (0, 30002):
        dc [i] = infinite
    dc [2] = cost

    def findLongestSub (pos_, len_ = 2):
        fd = False
        while pos_ + len_ - 2 < n:
            sub = s [pos_ : pos_ + len_]
            sub_ = sub [ : -1]
            presub = s [pos - 1 : pos_ + len_ - 1]

#            found = s.find (sub, 0, pos_)
            # using dict ~ faster
            if sub in d:
                found = d [sub] [0]

            # next 2 elif: not much, but faster - can be left away
            elif sub_ in d and s [d [sub_] [0] + len_ - 1] == sub [-1: ] and d [sub_] [0] + len_ <= pos_:
                d [sub] = d [sub_]
                found = d [sub] [0]
            elif presub in d and s [d [presub] [0] + len_] == sub [-1: ]:
                d [sub] = d [presub] [0] + 1, len_ - 1
                found = d [sub] [0]

            else:
                found = s.find (sub, 0, pos_)
                if found >= 0:
                    d [sub] = found, len_ - 1
            if found == -1:
                if fd:
                    return sub, len_ - 1
                else:
                    return "", 0
            fd = True
            len_ += 1
        if fd:
            return sub, len_ - 2
        else:
            return "", 0

    lastLongest = 1
    while pos < n:
        #subT = findLongestSub (pos)
        subT = findLongestSub (pos, lastLongest - 1)
        # fill costs
        lastLongest = subT [1]
        dc [pos + lastLongest] = min (dc [pos + lastLongest], b + dc [pos])
        dc [pos + 1] = min (dc [pos + 1], a + dc [pos])
        pos += 1
    return dc [pos]

def main ():
    fptr = open(os.environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for t_itr in range(t):
        nab = input ().split ()
        n = int (nab[0])
        a = int (nab[1])
        b = int (nab[2])
        s = input ()
        result = buildString (n, a, b, s)
        fptr.write (str (result) + '\n')
        print (result)
    fptr.close ()
    
if __name__ == '__main__':
    main ()

"""
 Funktion findLongestSub: suche längsten substring und gib ihn zurück samt Länge
 oder Leerstring und 0, wenn keiner gefunden wird
 Beginne mit Länge 2, wenn gefunden in string bis aktueller Position, erhöhe Länge bis
 kein substring mehr gefunden wird.
 Verwendung eines dictionaries.
 Wenn nach substring gesucht wird, zuerst in dict sehen, ob schon mal danach gesucht wurde
 Wenn schon gesucht und gefunden wurde, gibt True zurück
 Wenn schon gesucht aber nicht gefunden wurde, gibt False zurück
 Wenn nicht in dict, suche substring in Teilstring (das ist der Teilstring von s vom 
 Beginn bis zu aktueller Position von s)
 Trage substring in dict ein: Mit True, wenn gefunden, andernfalls mit False
 
 Verwendung von "cheapersub" berechnet, ab wie vielen Stellen es billiger ist
 einen (möglichen gefundenen) substring zu verwenden
 
tc 20 correct out:
771187
2514362
24025545

tc 12 correct out:
625348
2119936
42163005

1
100 7890 7891
acbcrsjcrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcrsjrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcsbcbcrsjh Expected Output: 126246

1
10 10 11
cbcjbcbcjh
Expected Output: 71
on pos 4 (starting with 0): bc (11) + bcj (11) + h (10) = 31
                    better: b (10) + cbcj (11) + h (10) = 30

    def findLongestSubR (pos_):  # find from back
        len_ = 1
        while pos_ - len_ >= 0:
            sub = s [pos_ - len_: pos_]
            found = s.find (sub, 0, pos_ - len_)
            if found == -1:
                return len_ - 1
            len_ += 1
        return len_ - 1

    pos = n
    cost = 0
    while pos > 0:
        subT = findLongestSubR (pos)
        if subT > cheapersub:
            cost += b
            pos -= subT
        else:
            cost += a
            pos -= 1
    return cost


"""
