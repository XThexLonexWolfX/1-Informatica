"""
auteur: Yorben Joosen
groep: PR09
datum: 29/09/2019

Inlezen van twee getallen en het afdrukken van na keuze of de som of het verschil
"""

getal1 = int(input('Geef getal1: '))
getal2 = int(input('Geef getal2: '))
keuze = input('Geef + voor som of - voor het verschil: ')
if keuze == '+':
    resultaat = getal1 + getal2
else:
    resultaat = getal1 - getal2
print(getal1, keuze, getal2, 'is', resultaat)