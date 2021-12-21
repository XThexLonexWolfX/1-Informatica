"""
auteur: Joosen Yorben
groep: PR09
datum: 29/09/2019

Inlezen van twee getallen en afdrukken of het even of oneven is
"""
x = int(input('Geef getal: '))
y = (x%2 ==0 )
if y == True:
    print(x, 'is even')
else:
    print(x, 'is oneven')