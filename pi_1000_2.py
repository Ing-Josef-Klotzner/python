#!/usr/bin/env python2
def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = (10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x)
        else:
            q, r, t, k, m, x = (q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2)

my_array = []
i=0;
for x in make_pi():
    my_array.append(str(x))
    i+=1
    if i == 1001:
	break
big_string = "".join(my_array)

print "here is a big string:\npi= %s.%s" % (big_string[0],big_string[1:]) 