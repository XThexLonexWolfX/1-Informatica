"""
auteur: Joosen Yorben
groep: PR09
datum: 29/09/2019

Inlezen van drie getallen en de kleinste waarde afdrukken
"""
a = int(input('Geef coëfficient a: '))
b = int(input('Geef coëfficient b: '))
c = int(input('Geef coëfficient c: '))
D = b**2 - 4*a*c
x1 = (-b + D**(1/2)) / (2*a)
x2 = (-b - D**(1/2)) / (2*a)
if D > 0:
    print("De wortels zijn:")
    print("x1 =", x1)
    print("x2 =", x2)
elif D == 0:
    print("De wortels zijn: ")
    print("x1 = x2 =", x1)
else:
    print("De discriminant is negatief, geen reële wortels (", D, ")")
