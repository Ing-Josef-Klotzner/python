#!/usr/bin/python3

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            yield q
            D[q * q] = [q]
#            print ("prime", q, D)
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
#            print ("     ", q, D)
            del D[q]
        q += 1

if __name__ == '__main__':
    Primzahl_x = int (input ("Bitte geben Sie an, die wie vielte Primzahl sie ausgeben wollen: "))
    primes_L = []
    for i, prime in zip (range (1, Primzahl_x + 1), gen_primes()):
        if i == Primzahl_x:
            print (prime)
        primes_L.append (prime)
#    print (primes_L)
    print ("now calculating Riemann row for square")
    result = 1
    for prime in primes_L:
        prime__2 = prime ** 2
        result *= prime__2 / (prime__2 - 1)
    print ("Riemann row for square is: ", result)

    print ("now calculating Riemann row for ^3")
    result = 1
    for prime in primes_L:
        prime__2 = prime ** 3
        result *= prime__2 / (prime__2 - 1)
    print ("Riemann row for ^3 is: ", result)

    print ("now calculating Riemann row for ^4")
    result = 1
    for prime in primes_L:
        prime__2 = prime ** 4
        result *= prime__2 / (prime__2 - 1)
    print ("Riemann row for ^4 is: ", result)
    
    for i in range (5, 30):
        result = 1
        for prime in primes_L:
            prime__2 = prime ** i
            result *= prime__2 / (prime__2 - 1)
        if result < 0.001 or i % 1 == 0 or i == 5:
            print ("Riemann row for ^",i , "is: ", result)
        
