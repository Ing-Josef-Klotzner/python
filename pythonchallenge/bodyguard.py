#! /usr/bin/env python2
# bodyguard.py  --  created by Ing. Josef Klotzner
import re
pat = re.compile('(?<=[A-Z]{3})(?<![A-Z].{3})([a-z])(?=[A-Z]{3})(?!.{3}[A-Z])')
fobj = open("bodyguard.txt", "r")
for line in fobj:
    x=pat.findall(line.strip())
    if x:
        print ''.join(x),
"""
One small letter, surrounded by <b>EXACTLY</b> three big bodyguards on 
each of its sides.
"""

"""
(?<=[A-Z]{3})  # assert that there are 3 uppercase letters before the current position
(?<![A-Z].{3}) # assert that there is no uppercase letter 4 characters before the current position
([a-z])        # match a lowercase character (all characters in the example are ASCII)
(?=[A-Z]{3})   # assert that there are 3 uppercase letter after the current position
(?!.{3}[A-Z])  # assert that there is no uppercase letter 4 characters after the current position
"""
