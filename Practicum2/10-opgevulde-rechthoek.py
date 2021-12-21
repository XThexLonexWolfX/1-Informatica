"""

auteur : Joosen Yorben
groep : PR09
datum : 05/10/2019

"""
print('Druk rechthoek met ingelezen spaties, breedte, hoogte, randteken en opvulteken')
spaties = int(input('Geef het aantal spaties: '))
breedte = int(input('Geef de breedte: '))
hoogte = int(input('Geef de hoogte: '))
randteken = input('Geef het randteken: ')
opvulteken = input('Geef het opvulteken: ')
for kolom in range(spaties):
    print(' ', end='')
for kolom in range(breedte):
    print(randteken, end='')
print('')
for rij in range(hoogte - 2):
    for kolom in range(spaties):
        print(' ', end='')
    for kolom in range(1):
        print(randteken, end='')
    for kolom in range(breedte - 2):
        print(opvulteken, end='')
    for kolom in range(1):
        print(randteken, end='')
    print('')
for kolom in range(spaties):
    print(' ', end='')
for kolom in range(breedte):
    print(randteken, end='')
