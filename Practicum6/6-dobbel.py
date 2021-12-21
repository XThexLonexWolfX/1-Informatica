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
dobbel_lijst = vul_lijst(60,1,6)
print('Dobbel lijst:', dobbel_lijst)
frequentie_lijst = []
for i in range(7):
    frequentie_lijst.append(dobbel_lijst.count(i))
print('Frequentie_lijst:', frequentie_lijst)
for i in range(1, 7):
    print(i, '*' * frequentie_lijst[i])
