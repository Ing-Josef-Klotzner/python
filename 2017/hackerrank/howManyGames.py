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

def howManyGames (p, d, m, s):
    # linearer Preisabfall von p bis kurz vor m
    # letzter linearer x.ter Abfall (llx): (p - m) // d + 1
    llx = (p - m) // d + 1
    # durchschnittlicher Preis bis xter Abfall: (p + (p - d * (x - 1))) / 2
    avP = (p + p - d * (llx - 1)) / 2
    # Wenn s > avP * llx berechnet sich Anzahl Käufe:  llx + (s - avP * llx) // m
#    print (llx, avP)
    if s > avP * llx:
        return int (llx + (s - avP * llx) // m)
    else:
        # kann nur weniger oder gleich viel kaufen als s // avP
        try_ = s // avP
#        avtP = (p + p - d * (try_ - 1)) / 2
#        preis = avtP * try_
#        print (avtP, preis)
        while ((p + p - d * (try_ - 1)) / 2) * try_ > s:
            try_ -= 1
        return int (try_) 

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [p, d, m, s] = map (int, input ().split ())
    result = howManyGames (p, d, m, s)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
