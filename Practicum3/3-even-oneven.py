"""

auteur: Joosen Yorben
groep: PR09
datum: 11/10/2019
"""


def is_even(getal):
    return getal % 2 == 0


getal = int(input('Geef getal (0 om te stoppen): '))
while getal != 0:
    if is_even(getal) == True:
        print(getal, 'is even')
    else: 
        print(getal, 'is oneven')
    getal = int(input('Geef getal (0 om te stoppen): '))

