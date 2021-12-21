"""
auteur: Yorben Joosen
groep: PR09
datum: 18/10/2019
"""

naam = str(input('Geef een naam (stop om te stoppen): '))
while naam != 'stop':
    geboortejaar = int(input('Geef het geboortejaar: '))
    leeftijd = 2019 - geboortejaar
    print(naam, 'wordt dit jaar', leeftijd)
    naam = str(input('Geef een naam (stop om te stoppen): '))
