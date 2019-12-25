#!/usr/bin/python3
from primes import sieve
from primes import logical_to_integer

def main ():
    sieve_array = sieve(100)
    prime_numbers = logical_to_integer (sieve_array, sum (sieve_array))
    print (prime_numbers)

if __name__ == '__main__':
    main ()
