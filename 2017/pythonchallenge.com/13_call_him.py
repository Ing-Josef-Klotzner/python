#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from string import letters, lower
import xmlrpc.client

"""
13 call him
"""
# site = "http://www.pythonchallenge.com/pc/return/"
# opt = "disproportional.html"

"""
solve possible with interactive python:
>>> import xmlrpc.client
>>> conn.system.listMethods()
['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
>>> conn.system.methodHelp("phone")
'Returns the phone of a person'
conn.phone("Bert")
'555-ITALY'

"""
conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
answer_to_find = conn.phone("Bert")

# answer_to_find = "in progress"
print("answer to find is: ", answer_to_find)
opt = "".join(x for x in lower(answer_to_find) if x in letters)
print(" new site: http://www.pythonchallenge.com/pc/return/" + opt + ".html")
##webbrowser.open(site + answer_to_find)
