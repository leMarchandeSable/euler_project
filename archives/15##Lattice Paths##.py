

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def combination(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# grid size
a = 20
b = 20
print(combination(a + b, a))
