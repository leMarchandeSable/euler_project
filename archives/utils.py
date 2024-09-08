abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def combination(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def permutation(n, k):
    return int(factorial(n) / factorial(n - k))


def digit_sum(n):
    return sum([int(x) for x in str(n)])


def get_divisors(n):
    l = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            l.append(i)
            if i != n//i:
                l.append(n//i)
    return list(sorted(l))


def get_proper_divisors(n):
    l = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            l.append(i)
            if i != n//i:
                l.append(n//i)
    l.remove(n)
    return list(sorted(l))