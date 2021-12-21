"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 08/11/2019
"""
from random import randint


def vul_lijst(aantal, onder, boven):
    lijst = []
    for i in range(aantal):
        lijst.append(randint(onder, boven))
    return lijst


lijst_random = vul_lijst(20, 10, 80)
lijst_even = []
lijst_oneven = []
n = 0
while n < len(lijst_random):
    if lijst_random[n] % 2 == 0:
        lijst_even.append(lijst_random[n])
        n += 1
    else:
        n += 1
n = 0
while n < len(lijst_random):
    if lijst_random[n] % 2 != 0:
        lijst_oneven.append(lijst_random[n])
        n += 1
    else:
        n += 1
print('lijst: ', lijst_random)
print('lijst_even: ', lijst_even)
print('lijst_oneven: ', lijst_oneven)
