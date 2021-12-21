"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 08/11/2019
"""


def lees_namen(naam):
    lijst = []
    while naam != '':
        lijst.append(naam)
        naam = input('Geef een naam (<enter> om te stoppen): ')
    print('Ingelezen namen:', lijst)
    return lijst


naam = input('Geef een naam (<enter> om te stoppen): ')
lijst1 = lees_namen(naam)
print('Gesorteerde namen:', sorted(lijst1))
print('Namenlijst:')
for i in range(len(lijst1)):
    print(sorted(lijst1)[i])
