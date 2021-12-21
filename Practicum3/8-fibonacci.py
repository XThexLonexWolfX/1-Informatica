"""

auteur: Joosen Yorben
groep: PR09
datum: 14/10/2019
"""


def rij_van_fibonacci(aantal):
    a = 0
    b = 1
    print('Rij van Fibonacci (', aantal, 'elementen):')
    print(a, end=' ')
    print(b, end=' ')
    for i in range(aantal - 2): #-2 want de eerste a en b worden al geprint dus tellen niet bij de in range
        b += a
        a = b - a
        print(b, end=' ')


aantal = int(input('Geef het aantal elementen: '))
rij_van_fibonacci(aantal)
