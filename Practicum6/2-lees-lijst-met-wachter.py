"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 08/11/2019
"""


def lees_lijst_met_wachter(wachter):
    lijst = []
    while wachter != -1:
        lijst.append(wachter)
        wachter = int(input('Geef volgende getal (-1 om te stoppen): '))
    return lijst


wachter = int(input('Geef volgende getal (-1 om te stoppen): '))
lijst1 = lees_lijst_met_wachter(wachter)
print('lijst        :', lijst1)
print('len(lijst)   :', len(lijst1))
print('sum(lijst)   :', sum(lijst1))
print('max(lijst)   :', max(lijst1))
print('min(lijst)   :', min(lijst1))
print('sorted(lijst):', sorted(lijst1))