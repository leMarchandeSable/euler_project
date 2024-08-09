"""
<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385.$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
"""


def sum_square(n):
    s = 0
    for i in range(1, n + 1):
        s += i**2
    return s


def square_sum(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s**2


n = 100
a = sum_square(n)
b = square_sum(n)
print(b - a)