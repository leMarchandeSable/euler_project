"""
<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
<p>What is the largest prime factor of the number $600851475143$?</p>
"""


def decomposition_nombres_premiers(n):
    """
    Il existe les algorithmes de factorisation par divisions itératives classiques,
    l'algorithme rho de Pollard, les courbes elliptiques ou encore l'algorithme du crible quadratique.
    dCode utilise une combinaison de tous pour factoriser rapidement.
    https://www.dcode.fr/decomposition-nombres-premiers
    """
    i = 2
    facteurs = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            facteurs.append(i)
    if n > 1:
        facteurs.append(n)
    return facteurs


n = 600851475143

factors = decomposition_nombres_premiers(n)
print(max(factors))
