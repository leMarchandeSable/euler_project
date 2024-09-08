import utils


def is_abundant(x):
    return x < sum(utils.get_proper_divisors(x))


# all abondant number
n = 28123
abondant = []
for i in range(12, n + 1):
    if is_abundant(i):
        abondant.append(i)

#all possible abondant sum < n
somme_abondant = [False] * (n + 1)
for i in range(len(abondant)):
    for j in range(i, len(abondant)):
        s = abondant[i] + abondant[j]
        if s <= n:
            somme_abondant[s] = True


somme_non_abondant = [i for i in range(1, n + 1) if not somme_abondant[i]]
print(abondant)
print(somme_non_abondant)
print(sum(somme_non_abondant))
