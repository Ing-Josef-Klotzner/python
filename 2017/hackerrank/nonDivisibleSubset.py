#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from sys import version_info
if version_info.major == 3:
    pass
elif version_info.major == 2:
    input = raw_input
else:
    print ("Unknown python version - input function not safe")

from os import environ
#from sys import setrecursionlimit
#from math import ceil
from array import array
#from time import sleep

#setrecursionlimit (11000)
"""
from collections import Counter
m = Counter ([v % k for v in S])

print (sum ([max (m [i], m [k-i]) for i in range (1, (k-1) // 2 + 1)]) + min (m [0], 1) + int (k % 2 == 0 and m [k // 2] != 0))

Dies scheint zunächst in angemessener Zeitkomplexität schwer zu lösen zu sein. Nach weiteren Überlegungen denke ich, dass dies mit ein paar Überlegungen auf O(n) getan werden kann. Dies soll ein "einfaches" Problem sein, daher werde ich hier einige Algorithmenanleitungen geben.

Für jede Zahl K ist die Summe von 2 Werten (A & B) geradzahlig durch K teilbar, wenn die Summe der Reste von A/K + B/K  K ist. (Es gibt auch einen Sonderfall, bei dem beide A & B geradzahlig teilbar sind, was eine Summe von 0 ergibt.)

Für jeden dieser Reste gibt es 1 und nur 1 weiteren Restwert, der eine Summe durch K teilbar macht.

Beispiel: Mit K von 5 sind die restlichen Paare 1+4 & 2+3. Angesichts der Zahlen mit einem Rest von 1 können sie nicht mit JEDER der Zahlen mit dem Rest 4 gekoppelt werden (und umgekehrt). Wählen Sie also für die Anzahl der Werte in der Ergebnismenge den größeren der Werte mit Rest 1 gegenüber den Werten mit Rest 4. Wählen Sie das größere set von Rest 2 vs. Rest 3.

Für den Sonderfall, dass der Rest 0 ist, können sie aufgrund der Menge aller Werte, die einzeln durch K teilbar sind, nicht mit anderen gepaart werden. So kann maximal 1 Wert, der durch K gleichmäßig teilbar ist, zur Ergebnismenge addiert werden.

Für gerade Werte von K ist der gleiche Rest dem Fall 0 ähnlich. Für K = 6 sind die Paare 1+5, 2+4, 3+3. Für Werte mit Rest 3 kann höchstens ein Wert zur Ergebnismenge hinzugefügt werden.

10 5
770528134 663501748 384261537 800309024 103668401 538539662 385488901 101262949 557792122 46058493
out: 5

15 7
278 576 496 727 410 124 338 149 209 702 282 718 771 575 436
out: 11
"""
def nonDivisibleSubset (n, k, S):
    i = 0
    # create list of count of x % k from elements x of list S
    mcL = [0] * k
    for i in range (n):
        mod = S [i] % k
        mcL [mod] += 1
#    print ("list of count of mods:", mcL)
    # only 1 to add for divisible mod 0
    add0m = 1 if mcL [0] != 0 else 0
#    print ("mods to be combined:", m2c)
#    print ("add zero mod", add0m) 
    # mods: k (7) odd [1, 2, 3, 4, 5, 6] - can not combine: 1, 6   2, 5   3, 6
    # mods: k (6) even [1, 2, 3, 4, 5] - can not combine: 1, 5   2, 4   3, 3 (only 1 to add)
    addmm = 1 if not k % 2 and mcL [k // 2] != 0 else 0
#    print ("add mid mod", addmm)
    # take sum of max of counts of these mods not to combine 
    res = 0
    for i in range (1, (k - 1) // 2 + 1):
        res += max (mcL [i], mcL [k - i])
    res += add0m + addmm
    print (res)
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    nk = input ().split ()
    n = int (nk [0])
    k = int (nk [1])
    S = list (map (int, input ().rstrip ().split ()))
    result = nonDivisibleSubset (n, k, S)
    print ("\n", result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
