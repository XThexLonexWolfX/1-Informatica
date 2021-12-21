"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 15/11/2019
"""


def lees_puntenlijst(aantal):
    punten = []
    aantal_hoeken = 3
    for i in range(aantal_hoeken):
        x = int(input('Geef punt ' + str(i + 1) + ' x: '))
        y = int(input('Geef punt ' + str(i + 1) + ' y: '))
        punten.append((x, y))
    print('punten:', punten)
    return punten


def omtrek(puntenlijst):
    teller = 0
    i = 0
    afstanden = []
    aantal_hoeken = 3
    while i < aantal_hoeken:
        if teller > aantal_hoeken - 2:
            afstand = ((puntenlijst[0][0] - puntenlijst[aantal_hoeken - 1][0]) ** 2 + (puntenlijst[0][1] - puntenlijst[aantal_hoeken - 1][1])**2)**0.5
        else:
            afstand = ((puntenlijst[i][0] - puntenlijst[i + 1][0]) ** 2 + (puntenlijst[i][1] - puntenlijst[i + 1][1])**2)**0.5
            teller += 1
        afstanden.append(afstand)
        i += 1
    return afstanden


puntenlijst = lees_puntenlijst(3)
print('De omtrek is:', sum(omtrek(puntenlijst)))

