"""
<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
"""

n = 1000
l = range(n)
s = 0

for i in l:
    if i % 5 == 0 or i % 3 == 0:
        s += i

print(s)
