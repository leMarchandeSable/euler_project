"""
<p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
<p>What is the smallest positive number that is <strong class="tooltip">evenly divisible<span class="tooltiptext">divisible with no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>
"""


def is_evenly_divisible_by_n(x, divisors):
    for divisor in reversed(divisors):
        if x % divisor != 0:
            return False
    return True


divisors = [7, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# reduced divisors for n = 10: [6, 7, 8, 9, 10]
# reduced divisors for n = 20: [7, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

i = max(divisors)
while not is_evenly_divisible_by_n(i, divisors):
    i += max(divisors)

print(i)
# 232792560