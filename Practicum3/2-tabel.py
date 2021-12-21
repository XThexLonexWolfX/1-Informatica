"""

auteur: Joosen Yorben
groep: PR09
datum: 11/10/2019
"""


def druk_tabel(getal):
    for i in range(0, 10):
        print(str(i) + ' X ' + str(getal) + ' = ' + str(i * getal))


getal = int(input('Geef getal (-1 om te stoppen): '))
while getal != -1:
    druk_tabel(getal)
    getal = int(input('Geef getal (-1 om te stoppen): '))