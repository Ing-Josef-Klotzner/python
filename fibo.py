#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from __future__ import absolute_import, division, print_function
from sys import argv
from decimal import Decimal
# Fibonacci numbers module
#
#print (len(argv))
if len(argv) == 1:
	print ("usage: "+argv[0]+" 'Fibonnaci number'")
	print ("Es wird per default Fibonnaci Zahl 8 berechnet")
	argv.append(8)
def fib(n):    # write Fibonacci series up to n
	a, b = 0, 1
	while b <= n:
		print (b),
		a, b = b, a+b

def fib2(n): # return Fibonacci series up to nth Fibonnaci
	result = []
	count=1
	a, b = 0, 1
	while count <= n:
		result.append(b)
		a, b = b, a+b
		count+=1
	return result

def fib3(n): # return Fibonacci number n - recursive method
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib3(n-1) + fib3(n-2)

# direkte Formel:
def fib4(n) : 
    # 1/sqrt(5) * ( ( ( 1 + sqrt (5)) / 2 ) ** n - ( ( 1 - sqrt (5)) / 2 ) ** n )
    sqrt_5 = Decimal(5).sqrt()
    return int ( "{:.0f}".format ( 1 / sqrt_5 * ( ( ( 1 + sqrt_5) / 2 ) ** n - ( ( 1 - sqrt_5) / 2 ) ** n ) ) )
# haskell lösung
# fib5 n = 
#   let
#     fib = 1: 1: zipWith (+) fib (tail fib)
#   in
#     fib !! n

if __name__ == "__main__":
#	fib(int(argv[1]))
    print (" Fibonnaci Zahl rekursiv gerechnet: ")
    print ( fib3 (int(argv[1])) )
    print ( "Fibonnaci Zahl "+str(argv[1])+" mit Formel gerechnet: " )
    print ( fib4 (int(argv[1])) )
    result=fib2(int(argv[1]))
    print ( result )  #  wenn nur letzte gewünscht [-1]
#	print fib3(int(argv[1]))
    length = 0
    for zahl in xrange(len(result)):
        length+=len(str(result[zahl]))
    print ("Anzahl der Summe der Stellen aller Zahlen der Reihe: "+str(length))
