#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from string import digits
import re

"""
10 what are you looking at? 

a = [1, 11, 21, 1211, 111221,   # to see when click at the bull
len(a[30]) = ?

analyze:
what kind of sequence is a ?
-> solution: next number digit is x * digit for each digit from previous number from left to rigt:
  for next number x and digit are building a pair of digits for each digit from previous number from left to right
    1,      11,      21,         1211,           111221
    |      / |      / |         /  |            /
    > 1*1 /  > 2*1 /  > 1*2 1*1    > 1*1 1*2 2*1 
"""
# site = "http://www.pythonchallenge.com/pc/return/"
# opt = "bull.html"

def next_element(el):
    n_el = ""
    match_iter_list = re.finditer('1+|2+|3+|4+|5+|6+|7+|8+|9+',el)
    for match in match_iter_list:
        match_list = zip(match.group(), match.span())
        if match_list != []:
            digit = match_list[0][0]
            if len(match_list) > 1:
                digit_count_as_str = str(int(match_list[1][1]) - int(match_list[0][1]))
                n_el += digit_count_as_str + digit
#                print("found", digit_count_as_str, "times", digit, "positional information:", end="")
            else:
                n_el += "1" + digit
#                print("found 1 time", digit, ", positional information:", end="")
#            print(match_list)
#    print("next element in sequence:",n_el)
    return n_el

el = "1"   # initial element of sequence
#el = "111221"

# print("next element mit Funktion next_element(): ", next_element(el))

# create sequence:
for seq in range(1, 31):
    n_el = next_element(el)
#    print("next element (",seq,"): ", n_el, "Length:", len(n_el))
    el = n_el
    

answer_to_find = len(n_el)
print("answer to find is: ", answer_to_find)

#webbrowser.open(site + answer_to_find)
