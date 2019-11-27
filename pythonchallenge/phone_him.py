#! /usr/bin/env python2
# phone_him.py  --  created by Ing. Josef KlotzneIr
import xmlrpclib
phonebook = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print phonebook.system.listMethods()
print phonebook.system.methodHelp('phone')
print phonebook.phone('Bert')
print phonebook.phone('Leopold')
