"""
auteur: Joosen Yorben
groep: PR09
datum: 29/09/2019

Inlezen van drie getallen en de kleinste waarde afdrukken
"""
getal1 = int(input('Geef getal1: '))
getal2 = int(input('Geef getal2: '))
getal3 = int(input('Geef getal3: '))
if getal1<getal2<getal3 or getal1<getal3<getal2:
    print('De kleinste waarde is ',getal1)
if getal2<getal3:
    print('De kleinste waarde is ',getal2)
else:
    print('De kleinste waarde is ',getal3)