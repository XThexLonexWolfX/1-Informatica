"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 15/11/2019
"""


def lees_puntenlijst(aantal):
    punten = []
    for i in range(aantal_in_te_lezen_punten):
        x = int(input('Geef punt ' + str(i + 1) + ' x: '))
        y = int(input('Geef punt ' + str(i + 1) + ' y: '))
        punten.append((x, y))
    return punten


aantal_in_te_lezen_punten = int(input('Geef het aantal in te lezen punten: '))
punten = lees_puntenlijst(aantal_in_te_lezen_punten)
extra_puntx = int(input('Geef punt x: '))
extra_punty = int(input('Geef punt y: '))
extra_punt = (extra_puntx, extra_punty)
print('punt:', extra_punt)
print('punten:', punten)
afstanden = []
for i in range(aantal_in_te_lezen_punten):
    afstand = ((punten[i][0] - extra_punt[0])**2 + (punten[i][1] - extra_punt[1])**2) ** 0.5
    afstanden.append(afstand)
print('afstanden:', afstanden)
print('Het dichtstbijgelegen punt is:', punten[afstanden.index(min(afstanden))])
print('Het verstgelegen punt is     :', punten[afstanden.index(max(afstanden))])
