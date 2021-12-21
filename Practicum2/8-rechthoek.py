"""

auteur : Joosen Yorben
groep : PR09
datum : 05/10/2019

"""
print('Druk rechthoek met ingelezen spaties, breedte, hoogte, randteken en opvulteken')
spaties = int(input('Geef het aantal spaties: '))
breedte = int(input('Geef de breedte: '))
hoogte = int(input('Geef de hoogte: '))
opvulteken = input('Geef het opvulteken: ')

for rij in range(hoogte):
    for kolom in range(spaties):
        print(' ', end='')
    for kolom in range(breedte):
        print(opvulteken, end='')
    print('')