"""

auteur : Joosen Yorben
groep : PR09
datum : 05/10/2019

"""
print('Druk driehoek met ingelezen spaties, hoogte en teken')
spaties = int(input('Geef het aantal spaties: '))
hoogte = int(input('Geef de hoogte: '))
randteken = input('Geef het randteken: ')
opvulteken = input('Geef het teken: ')
breedte = 1
for kolom in range(spaties):
    print(' ', end='')
for kolom in range(1):
    print(randteken)
for rij in range(hoogte - 2):
    for kolom in range(spaties - 1):
        print(' ', end='')
    for kolom in range(1):
        print(randteken, end='')
    for kolom in range(breedte):
        print(opvulteken, end='')
    for kolom in range(1):
        print(randteken, end='')
    spaties -= 1
    breedte += 2
    print('')
for kolom in range(spaties - 1):
    print(' ', end='')
for kolom in range(breedte + 2):
    print(randteken, end='')
