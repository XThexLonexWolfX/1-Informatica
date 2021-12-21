"""

auteur: Joosen Yorben
groep: PR09
datum: 11/10/2019
"""


def maand_naar_seizoen(getal):
    if 3 <= getal <= 5:
        return str('lente')
    elif 6 <= getal <= 8:
        return  ('zomer')
    elif 9 <= getal <= 11:
        return ('herfst')
    else:
        return ('winter')


getal = int(input('Geef de maand (1..12): '))
maand_naar_seizoen(getal)
print('Maand', getal, 'ligt in de', maand_naar_seizoen(getal) + str('.'))

