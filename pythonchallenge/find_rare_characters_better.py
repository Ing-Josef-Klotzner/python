#! /usr/bin/env python2
# find_rare_characters.py  --  created by Ing. Josef Klotzner
import string
text = ''.join([line.rstrip() for line in open('view-source_www.pythonchallenge.com_pc_def_ocr.txt')])
print filter(lambda x: x in string.letters,text)
# equality
