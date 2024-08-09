"""
<p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
<p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>
"""


def is_palindromic(x):
    val = str(x)
    n = len(val)

    for i in range(n//2):
        if val[i] != val[n-i-1]:
            return False
    return True


nb_digit = 3
maxi = int("9" * nb_digit) + 1
mini = 10**(nb_digit - 1)
l = []

for i in range(mini, maxi):
    for j in range(i, maxi):

        if is_palindromic(i*j):
            print(i, j, i*j)
            l.append(i*j)
print()
print(max(l))
