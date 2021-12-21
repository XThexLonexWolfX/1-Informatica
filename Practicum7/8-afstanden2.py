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
n = 0
verst = dict()
dichtst = dict()
max = dict()
min = dict()
puntenmax = dict()
puntenmin = dict()
nakijker = 0
maximum = 0
minimum = 1000
afstanden = []
print('punten:', punten)
print('De verst van elkaar gelegen punten zijn:')
for i in range(aantal_in_te_lezen_punten):
    if i == 0:
        while n < aantal_in_te_lezen_punten:
            if n != i:
                afstand = ((punten[i][0] - punten[n][0]) ** 2 + (punten[i][1] - punten[n][1]) ** 2) ** 0.5
                afstanden.append(afstand)
                if afstand > maximum:
                    puntenmax['begin'] = (0, 0)
                    puntenmax['einde'] = (n, n)
                    maximum = afstand
                elif afstand < minimum:
                    puntenmin['begin'] = (0, 0)
                    puntenmin['einde'] = (n, n)
                    minimum = afstand
                else:
                    afstand = afstand
            else:
                n = n
            n += 1
        n = 0
    elif i == 1:
        while n < aantal_in_te_lezen_punten:
            if n != i:
                afstand = ((punten[i][0] - punten[n][0]) ** 2 + (punten[i][1] - punten[n][1]) ** 2) ** 0.5
                afstanden.append(afstand)
                if afstand > maximum:
                    puntenmax['begin'] = (1, 1)
                    puntenmax['eind'] = (n, n)
                    maximum = afstand
                elif afstand < minimum:
                    puntenmin['begin'] = (1, 1)
                    puntenmin['einde'] = (n, n)
                    minimum = afstand
                else:
                    afstand = afstand
            else:
                n = n
            n += 1
        n = 0
    elif i == 2:
        while n < aantal_in_te_lezen_punten:
            if n != i:
                afstand = ((punten[i][0] - punten[n][0]) ** 2 + (punten[i][1] - punten[n][1]) ** 2) ** 0.5
                afstanden.append(afstand)
                if afstand > maximum:
                    puntenmax['begin'] = (2, 2)
                    puntenmax['eind'] = (n, n)
                    maximum = afstand
                elif afstand < minimum:
                    puntenmin['begin'] = (2, 2)
                    puntenmin['einde'] = (n, n)
                    minimum = afstand
                else:
                    afstand = afstand
            else:
                n = n
            n += 1
        n = 0
    elif i == 3:
        while n < aantal_in_te_lezen_punten:
            if n != i:
                afstand = ((punten[i][0] - punten[n][0]) ** 2 + (punten[i][1] - punten[n][1]) ** 2) ** 0.5
                afstanden.append(afstand)
                if afstand > maximum:
                    puntenmax['begin'] = (3, 3)
                    puntenmax['einde'] = (n, n)
                    maximum = afstand
                elif afstand < minimum:
                    puntenmin['begin'] = (3, 3)
                    puntenmin['einde'] = (n, n)
                    minimum = afstand
                else:
                    afstand = afstand
            else:
                n = n
            n += 1
        n = 0
    elif i == 4:
        while n < aantal_in_te_lezen_punten:
            if n != i:
                afstand = ((punten[i][0] - punten[n][0]) ** 2 + (punten[i][1] - punten[n][1]) ** 2) ** 0.5
                afstanden.append(afstand)
                if afstand > maximum:
                    puntenmax['begin'] = (4, 4)
                    puntenmax['einde'] = (n, n)
                    maximum = afstand
                elif afstand < minimum:
                    puntenmin['begin'] = (4, 4)
                    puntenmin['einde'] = (n, n)
                    minimum = afstand
                else:
                    afstand = afstand
            else:
                n = n
            n += 1
        n = 0
        max['afstand'] = maximum
        min['afstand'] = minimum
        verst = max.copy()
        verst.update(puntenmax)
        dichtst = min.copy()
        dichtst.update(puntenmin)
print(verst)
print(dichtst)
