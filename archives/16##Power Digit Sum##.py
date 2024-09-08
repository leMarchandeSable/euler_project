"""
<p>$2^{15} = 32768$ and the sum of its digits is $3 + 2 + 7 + 6 + 8 = 26$.</p>
<p>What is the sum of the digits of the number $2^{1000}$?</p>
"""


def digit_sum(n):
    return sum([int(x) for x in str(n)])


n = 1000
a = 2**n
print(a, digit_sum(a))