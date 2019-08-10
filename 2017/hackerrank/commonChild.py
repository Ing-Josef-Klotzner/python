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
#setrecursionlimit (100000)

"""
SHINCHAN
NOHARAAA
out: 3

ABCDEF
FBDAMN
out: 2

WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS
FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC
out: 15
"""

# O (m * n) solution processing also letters, not only length
def commonChild (s1, s2):
    l1 = len (s1)
    l2 = len (s2)
    # we only need history of previous row
    lcs = [0] * (l2 + 1)
#    lcs_letters = [['']] * (l2 + 1)     # uncomment if also using letters
    for i in range (l1):
        lcsc = [0]
#        lcs_lettersc = [['']]          # uncomment if also using letters
        for j in range (l2):  # previous, left, above (2D table view)
            if s1 [i] == s2 [j]:
                # found. so add 1 to the length of previous longest sequence
                lcsc.append (lcs [j] + 1)   # previous + 1
#                lcs_lettersc.append ([])   # uncomment this and next 2 lines / letters
#                for ix in range (len (lcs_letters [j])):
#                    lcs_lettersc [j + 1].append (lcs_letters [j] [ix] + s1 [i])
            # if not matching pair, get the biggest previous value - merge letters
            elif lcs [j + 1] > lcsc [j]:   # above > left
                lcsc.append (lcs [j + 1])
#                lcs_lettersc.append (lcs_letters [j + 1])   # uncomment if letters
            else: lcsc.append (lcsc [j])   # comment line if using letters
## uncomment block if using also letters
#            elif lcsc [j] > lcs [j + 1]:   # left > above
#                lcsc.append (lcsc [j])
#                lcs_lettersc.append (lcs_lettersc [j])
#            else:                          # left == above
#                lcsc.append (lcsc [j])
#                lcs_lettersc.append ([])
#                lcs_lettersc [j + 1] += lcs_lettersc [j]
#                lcs_lettersc [j + 1] += lcs_letters [j + 1]
#                lcs_lettersc [j + 1] = list (set (lcs_lettersc [j + 1]))

        lcs = lcsc   # make current row the next previous row
#        lcs_letters = lcs_lettersc        # uncomment this and next line if letters
#    print (lcs_letters [j + 1])
    return lcs [j + 1]

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s1 = input ()
    s2 = input ()
    result = commonChild (s1, s2)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
