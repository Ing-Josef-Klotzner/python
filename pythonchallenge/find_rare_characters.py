#! /usr/bin/env python2
# find_rare_characters.py  --  created by Ing. Josef Klotzner
from collections import Counter
fobj = open("view-source_www.pythonchallenge.com_pc_def_ocr.txt", "r")
c=Counter()
for line in fobj:
    c += Counter(line.strip())
print c
"""
output:
Counter({')': 6186, '@': 6157, '(': 6154, ']': 6152, '#': 6115, '_': 6112, '[': 6108, '}': 6105, '%': 6104, '!': 6079, '+': 6066, '$': 6046, '{': 6046, '&': 6043, '*': 6034, '^': 6030, 'a': 1, 'e': 1, 'i': 1, 'l': 1, 'q': 1, 'u': 1, 't': 1, 'y': 1})
in short:   aeilquty  .... solution word in order of occurance of characters: equality
"""
