"""

auteur: Joosen Yorben
groep: PR09
datum: 14/10/2019
"""


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n - 2): #-2 want de eerste a en b worden al geprint dus tellen niet bij de in range
        b += a
        a = b - a
    return b


n = int(input('Geef het hoeveelste element: '))
fibonacci(n)
print('Element', n, 'van de rij van fibonacci is', fibonacci(n))