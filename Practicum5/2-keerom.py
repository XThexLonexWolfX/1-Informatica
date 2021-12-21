"""
auteur: Yorben Joosen
groep: PR09
datum: 25/10/2019
"""


def keerom(woord):
    omgekeerd = woord[-1::-1]
    print(woord, 'geef omgekeerd', omgekeerd)


woord = input('Geef een woord(<enter> om te stoppen): ')
while woord != '':
    keerom(woord)
    woord = input('Geef een woord(<enter> om te stoppen): ')