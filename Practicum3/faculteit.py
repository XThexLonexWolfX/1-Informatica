"""

auteur: Joosen Yorben
groep: PR09
datum: 11/10/2019
"""


def faculteit(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


n = int(input('Geef getal (negatief om te stoppen): '))
while n >= 0:
    print('De faculteit van', n, 'is', faculteit(n))
    n = int(input('Geef getal (negatief om te stoppen): '))