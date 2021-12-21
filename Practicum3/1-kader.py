"""

auteur: Joosen Yorben
groep: PR09
datum: 11/10/2019
"""


def druk_in_kader(woord):
        boven_en_onderkant_kader = str('+' + '-' * len(woord) + '+')
        zijkanten_kader = str('|' + woord + '|')
        print(boven_en_onderkant_kader)
        print(zijkanten_kader)
        print(boven_en_onderkant_kader)


woord = input('Geef een waarde voor woord (stop om te stoppen): ')
while woord != 'stop':
    druk_in_kader(woord)
    woord = input('Geef een waarde voor woord (stop om te stoppen): ')
