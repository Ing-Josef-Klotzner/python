#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from string import ascii_lowercase, ascii_uppercase, translate, letters, count
from time import sleep

import urllib, re, collections, webbrowser

"""
dont try all nothings
"""
site = "http://www.pythonchallenge.com/pc/def/"
opt = "linkedlist.php?nothing="
html_string = ""
answer_to_find = ""

def get_next_nothing(nothing):
    reduce_count = 1
    do_not_reduce_count = 0
    try:
        html_string = urllib.urlopen(site + opt + nothing).read()
        #html_lines = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').readlines()
        if "next nothing is" in html_string:
            return html_string, None, "".join(re.findall('next nothing is ([0-9]*)$', html_string)), do_not_reduce_count
        elif "Divide" in html_string:
            return html_string, None, str(int(nothing)//2), do_not_reduce_count
        else:
            return html_string, html_string, "", do_not_reduce_count
    except IOError:
        print("")
        print("the server pythonchallenge can not be reached. Will try again ...")
        return "try again in 3 seconds", None , nothing, reduce_count
        sleep(3)

nothing = "72758" # this you get when calling first just with php?nothing
nothing = "12345" # this is found in sourcecode when called with php?nothing
count = 0

while count < 280:   # reduced from 400 after seen answer is on position 270
    html_string, answer_found, nothing, count_reduce = get_next_nothing(nothing)
    if answer_found:
        answer_to_find = answer_found
        answer_count = count
    count += 1 - count_reduce
    print(str(count) + " " + html_string + "  (number: " + (nothing if nothing != "" else "") + ")")
print("")
print("The " + str(answer_count) + " answer to find is: " + answer_to_find)
webbrowser.open(site + answer_to_find)
