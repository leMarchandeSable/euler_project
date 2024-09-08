import utils


def d(x):
    return sum(utils.get_proper_divisors(x))


def is_amicable_number(x):
    b = d(x)
    a = d(b)
    return (x == a) and (a != b)


n = 10000
s = 0
for i in range(1, n):
    if is_amicable_number(i):
        s += i

print(s)