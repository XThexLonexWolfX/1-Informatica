"""

auteur : Joosen Yorben
groep : PR09
datum : 05/10/2019

"""
getal = int(input('Geef een waarde voor het te zoeken getal: '))
waarde = 0
teller = 0
n = 0
while teller < 6:
    teller += 1
    waarde = int(input('Geef een waarde voor het getal ' + str(teller) + ': '))
    if waarde == getal:
        n += 1
print ('Het getal ' + str(getal) + ' komt ' + str(n) + ' voor')