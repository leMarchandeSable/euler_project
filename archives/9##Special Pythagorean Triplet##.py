"""
<p>A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
$$a^2 + b^2 = c^2.$$</p>
<p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
<p>There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.</p>
"""


def generate_triplet(m, n):
    # euclid's formula
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2
    return a, b, c


for n in range(1, 100):
    for m in range(n + 1, 100):
        a, b, c = generate_triplet(m, n)

        if a + b + c == 1000:
            print(a, b, c)
            print(a * b * c)