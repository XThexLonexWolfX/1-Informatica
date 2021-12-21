"""

auteur: Joosen Yorben
groep: PR09
datum: 13/10/2019
"""


def som_cijfers(getal):
    som = 0
    while getal != 0:
        rest = getal % 10
        getal = getal // 10
        som += rest
    return som

getal = int(input('Geef getal (negatief om te stoppen): '))
while getal > 0:
    som_cijfers(getal)
    print('De som van de cijfers van', getal, 'is', som_cijfers(getal))
    getal = int(input('Geef getal (negatief om te stoppen): '))
