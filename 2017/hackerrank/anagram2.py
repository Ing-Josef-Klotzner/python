#! /usr/bin/python3
from collections import Counter
#from __future__ import print_function
for _ in range (int (input ())):
    s = input ()
    if len (s) % 2 == 1:
        print ("-1")
        continue
    a1 = (Counter (s [ : len (s) // 2]))
    a2 = (Counter (s [len (s) // 2 : ]))
#    print (a1)
#    print (a2)
#    print (a1 - a2)
    temp = a1 - a2
    print (sum (temp.values ()))

