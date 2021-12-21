"""

auteur : Joosen Yorben
groep : PR09
datum : 09/10/2019

"""
print('Druk driehoek met ingelezen spaties en hoogte')
spaties = int(input('Geef het aantal spaties: '))
hoogte = int(input('Geef de hoogte: '))
breedte = 1
n = 1
if hoogte > 5:
    print('Dit is niet mogelijk, maximum waarde voor de hoogte is 5')
else:
    for rij in range(hoogte):
        for kolom in range(spaties):
            print(' ', end='')
        for kolom in range(breedte):
            print(n, end='')
            n += 1
        n = 1
        spaties -= 1
        breedte += 2
        print('')