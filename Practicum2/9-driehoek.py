"""

auteur : Joosen Yorben
groep : PR09
datum : 05/10/2019

"""
print('Druk driehoek met ingelezen spaties, hoogte en teken')
spaties = int(input('Geef het aantal spaties: '))
hoogte = int(input('Geef de hoogte: '))
opvulteken = input('Geef het teken: ')
breedte = 1
for rij in range(hoogte):
    for kolom in range(spaties):
        print(' ', end='')
    for kolom in range(breedte):
        print(opvulteken, end='')
    spaties -= 1
    breedte += 2
    print('')