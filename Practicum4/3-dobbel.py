"""
auteur: Yorben Joosen
groep: PR09
datum: 18/10/2019
"""
#Probeer met while lus if dobbel = i print X else print spatie
import random


def dobbel():
    x = random.randrange(1, 6)
    return x


teken = 'X'
print('Beurt  1 2 3 4 5 6')
for rij in range(13):
    print('{:5}'.format(rij), end='')
    dobbel()
    if dobbel() == 1:
        print('{:>3}'.format(teken))
    elif dobbel() == 2:
        print('{:>5}'.format(teken))
    elif dobbel() == 3:
        print('{:>7}'.format(teken))
    elif dobbel() == 4:
        print('{:>9}'.format(teken))
    elif dobbel() == 5:
        print('{:>11}'.format(teken))
    else:
        print('{:>13}'.format(teken))
