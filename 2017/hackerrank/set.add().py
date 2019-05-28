#!/usr/bin/python3

if __name__ == '__main__':
    N = int (input ())
    set_ = set ([])
    for i in range (N):
        country = input ()
        set_.add (country)
    print (len (set_))
