
cimport cython

@cython.cdivision (True)
cdef inline double recip_square_cy2 (int i):
    cdef:
        double x, s
    x = i ** 2
    s = 1 / x
    return s

def apr_pi (int n):
    """Compute an approximate value of pi."""
    cdef:
        int k
        double val
    val = 0
    for k in range (1, n + 1):
        x = recip_square_cy2 (k)
        val += x
    pi = (6 * val) ** .5
    return pi
