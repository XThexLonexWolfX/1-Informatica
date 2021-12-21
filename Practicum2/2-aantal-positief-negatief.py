"""

auteur : Joosen Yorben
groep : PR09
datum : 04/10/2019

"""

aantal = int(input('Geef een waarde voor aantal: '))
aantal_positieve = 0
aantal_negatieve = 0
n = 1
for i in range(1,aantal + 1):
    getal = int(input('Geef getal '+ str(n) + ': '))
    n += 1
    if getal >= 0:
        aantal_positieve += 1
    else:
        aantal_negatieve += 1
print('Het aantal positieve getallen:', aantal_positieve)
print('Het aantal negatieve getallen:', aantal_negatieve)
