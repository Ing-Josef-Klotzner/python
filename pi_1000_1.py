#!/usr/bin/env python3
from time import sleep
def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = (10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x)
        else:
            q, r, t, k, m, x = (q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2)

i = 0;
pi_str = ""
for x in make_pi():
#    print x
#    sleep(1)
    pi_str += str(x)
    i += 1
    if i == 1001:
        break

print ("pi= %s.%s" % (pi_str[0],pi_str[1:]))
