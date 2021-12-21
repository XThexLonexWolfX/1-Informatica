"""

auteur : Joosen Yorben
groep : PR09
datum : 04/10/2019

"""
getal = int(input('Geef getal (0 om te stoppen): '))
n = 0
while getal != 0:
    print(str(n) + ' X ' + str(getal) + ' = ' + str(n*getal))
    n += 1
    if n > 9:
        getal = int(input('Geef getal (0 om te stoppen): '))
        n = 0
