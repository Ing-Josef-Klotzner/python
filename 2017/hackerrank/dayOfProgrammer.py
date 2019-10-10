#!/usr/bin/python3

from os import environ

def dayOfProgrammer (year):
    def isLeapYear ():
        if year >= 1700 and year <= 1917:
            if year % 4 == 0: return True
            else: return False
        elif year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0): return True
        else: return False
    if year == 1918: dayOfProgrammer = 26
    elif isLeapYear (): dayOfProgrammer = 12
    else: dayOfProgrammer = 13
    return str (dayOfProgrammer) + ".09." + str (year)
 
if __name__ == '__main__':
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    year = int (input ().strip ())
    result = dayOfProgrammer (year)
    print (result)
    fptr.write (result + '\n')
    fptr.close ()

