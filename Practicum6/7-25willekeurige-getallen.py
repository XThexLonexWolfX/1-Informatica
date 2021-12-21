"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 13/11/2019
"""
from random import randint


def vul_lijst(aantal, onder, boven):
    lijst = []
    for i in range(aantal):
        lijst.append(randint(onder, boven))
    return lijst


n = 0
lijst_voor = vul_lijst(25,10,35)
print('Lijst voor:', lijst_voor)
while n < len(lijst_voor):
    if lijst_voor[n] % 5 == 0:
        del lijst_voor[n]
    else:
        n += 1
print('Lijst na:', lijst_voor)
