#!/usr/bin/python3
from primes import sieve
from primes import logical_to_integer

def main ():
    sieve_array = sieve(1000000)
    prime_numbers = logical_to_integer (sieve_array, sum (sieve_array))
    print (len (prime_numbers))
    print (prime_numbers [-1])

if __name__ == '__main__':
    main ()
