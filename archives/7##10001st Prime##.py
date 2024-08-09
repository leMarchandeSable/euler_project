"""
<p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.</p>
<p>What is the $10\,001$st prime number?</p>
"""
import numpy as np


def primes_sieve(n):
    p_n = int(2 * n * np.log(n))       # over-estimate p_n
    sieve = np.ones(p_n)               # everything is prime to start
    count = 0

    for i in range(2, p_n):
        if sieve[i]:                       # still prime?
            count += 1                     # count it!
            if count == n:                 # done!
                return i
            for j in range(2*i, p_n, i):   # cross off all multiples of i
                sieve[j] = False


n = 10001
print(primes_sieve(n))
