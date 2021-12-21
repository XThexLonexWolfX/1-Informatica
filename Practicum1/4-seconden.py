"""
auteur: Joosen Yorben
groep: PR09
datum: 29/09/2019

Aantal seconden omzetten in uren, minuten en seconden
"""
aantal_seconden = int(input('Geef het totaal aantal seconden: '))
uren = aantal_seconden//3600
rest = aantal_seconden%3600
minuten = rest//60
seconden = rest%60
print(uren, 'uren', minuten, 'minuten', seconden, 'seconden')