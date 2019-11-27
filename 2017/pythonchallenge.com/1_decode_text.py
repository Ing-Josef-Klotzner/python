#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from string import ascii_lowercase, ascii_uppercase

# a 97  ... z 122   A 65  ...   Z 90

# from string import ascii_lowercase
try:
    # Python 2
    from string import maketrans
except ImportError:
    # Python 3 made maketrans a static method
    maketrans = str.maketrans 

try:
    orig_txt = raw_input("text zu decodieren: ")
except NameError:
    orig_txt = input("text zu decodieren: ")

# orig_txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

out_txt = ""
shift = 2   # Anzahl Verschiebung im Alphabet

for char in orig_txt:
    if ord(char) >= 97 and ord(char) <= 120 or ord(char) >= 65 and ord(char) <= 88:
        out_txt += chr(ord(char)+shift)
    elif ord(char) >= 121 and ord(char) <= 122 or ord(char) >= 89 and ord(char) <= 90:
        out_txt += chr(ord(char)-(26-shift))
    else:
        out_txt += char
         
print("")
print("out text: ", out_txt)
print("")
cipher_map = maketrans(ascii_lowercase+ascii_uppercase, ascii_lowercase[shift:] + ascii_lowercase[:shift] + ascii_uppercase[shift:] + ascii_uppercase[:shift])
encrypted = orig_txt.translate(cipher_map)
print("out text using maketrans(): ", encrypted)
