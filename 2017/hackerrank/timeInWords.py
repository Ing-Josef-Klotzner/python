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
"""
At minutes = 0, use o' clock. For 1 <= minutes <= 30, use past, and for 30 < minutes use to. Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described. 
"""
def timeInWords (h, m):
    hour = ["twelve", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "one"]
    minutes = ["zero", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
        "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four",
        "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "thirty",
        "thirty one", "thirty two", "thirty three", "thirty four", "thirty five", "thirty six",
        "thirty seven", "thirty eight", "thirty nine", "fourty", "fourty one", "fourty two",
        "fourty three", "fourty four", "fourty five", "fourty six", "fourty seven", "fourty eight",
        "fourty nine", "fifty", "fifty one", "fifty two", "fifty three", "fifty four",
        "fifty five", "fifty six", "fifty seven", "fifty eight", "fifty nine"]
    if m == 0:
        return hour [h] + " o' clock"
    elif m == 15:
        return "quarter past " + hour [h]
    elif m == 30:
        return "half past " + hour [h]
    elif m == 45:
        return "quarter to " + hour [h + 1]
    elif m == 1:
        return minutes [m] + " minute past " + hour [h]
    elif m > 1 and m < 30:
        return minutes [m] + " minutes past " + hour [h]
    elif m == 59:
        return minutes [60 - m] + " minute to " + hour [h + 1]
    else: return minutes [60 - m] + " minutes to " + hour [h + 1]

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    h = int (input ())
    m = int (input ())
    result = timeInWords (h, m)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
