from sys import stdin, stdout

def ham (n, s):
    s = [0] + list (s)
    q = int (input ())
    for q_ in range (q):
        cmd, *par = stdin.readline ().rstrip ().split ()
        if cmd == "C":
            l, r, ch = par
            l = int (l); r = int (r)
            s [l: r + 1] = (r - l + 1) * ch
        elif cmd == "S":
            l1, r1, l2, r2 = map (int, par)
            s [l1: r2 + 1] = s [l2: r2 + 1] + s [r1 + 1: l2] + s [l1: r1 + 1]
            print (s)
        elif cmd == "R":
            l, r = map (int, par)
            s [l: r + 1] = s [r: l - 1: -1]
        elif cmd == "W":
            l, r = map (int, par)
            stdout.write (''.join (s [l: r + 1]) + '\n')
        else:
            l, r, ln = map (int, par)
            d = 0
            for i in range (ln):
                if s [l + i] != s [r + i]: d += 1
            stdout.write (str (d) + ' \n')
                        

n = int (input ())
s = stdin.readline ()
ham (n, s)
