"""
auteur: Joosen Yorben
groep: PR09
datum: 29/09/2019

Inlezen van een getal tot 12 en het bijhorende seizoen afdrukken
"""
maand = int(input('Geef de maand (1...12): '))
if maand < 1 or maand > 12:
    print('Dit is geen maand')
elif 3 <= maand <= 5:
    print('lente')
elif 6 <= maand <= 8:
    print('zomer')
elif 9<= maand <=11:
    print('herfst')
else:
    print('winter')