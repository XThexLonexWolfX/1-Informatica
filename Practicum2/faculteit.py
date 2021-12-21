"""

auteur : Joosen Yorben
groep : PR09
datum : 04/10/2019

Inlezen van een positief getal en berekenen en afdrukken van de faculteit
"""

n = int(input('Geef positief getal: '))
while n < 0:
    print('Het getal moet positief zijn!')
    n = int(input('Geef positief getal: '))
faculteit = 1
teller = 1
while teller <= n:
    faculteit = faculteit * teller
    teller += 1
print('De faculteit van', n, 'is', faculteit)