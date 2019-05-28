#!/usr/bin/python3

if __name__ == '__main__':
    n, m = map (int, input ().split ())
    inp = input ().split ()
    A = frozenset (input ().split ())
    B = frozenset (input ().split ())
    print (sum([(i in A) - (i in B) for i in inp]))
