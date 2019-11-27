#! /usr/bin/env python2
# alphabet_shift_coded_text.py  --  created by Ing. Josef Klotzner
import re
import sys
from string import maketrans
intab = "yzabcdefghijklmnopqrstuvwxYZABCDEFGHIJKLMNOPQRSTUVWX"
outtab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
trantab = maketrans(intab, outtab)
text="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
conv_text = []
#text_list=iter(text)
text_list=text
print
print "original text: ", text
print
#print text_list
print "solution by shift ascii by 2 - direct output to terminal:"
for t in text_list:
    if t.isalpha():
        if t == "y":
            c = "a"
        elif t == "z":
            c = "b"
        elif t == "Y":
            c = "A"
        elif t == "Z":
            c = "B"
        else:
            c = chr(ord(t)+2)
        sys.stdout.write(c)
        conv_text.append(c)
    if not t.isalpha():
        sys.stdout.write(t)
        conv_text.append(t)
print
print
print "output from text variable"
print "".join(conv_text)
print
print "solution with string.maketrans:"
print text.translate(trantab)
print
#print "Transitiontable:"
#print trantab
