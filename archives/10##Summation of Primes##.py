"""
<p>The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.</p>
<p>Find the sum of all the primes below two million.</p>
"""
import numpy as np


def primes_sieve(p_n):
    sieve = np.ones(p_n)               # everything is prime to start
    s = 0

    for i in range(2, p_n):
        if sieve[i]:                       # still prime?
            s += i                         # count it!
            for j in range(2*i, p_n, i):   # cross off all multiples of i
                sieve[j] = False
    return s


p_n = 2*10**6
print(primes_sieve(p_n))
