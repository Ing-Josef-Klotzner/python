#!/usr/bin/python3

if __name__ == '__main__':
    n = int (input ())  # number of set elements
    set_ = set (map (int, input ().split ()))
    N = int (input ())  # number of commands
    for i in range (N):
        cmd = input ()
        if "pop" in cmd:
            set_.pop ()
        else:
            comd, parS = cmd.split ()
            par = int (parS)
            if "remove" in comd:
                set_.remove (par)
            elif "discard" in comd:
                set_.discard (par)
    print (sum (set_))
