"""
auteur: Yorben Joosen
groep: PR09
datum: 25/10/2019
"""


def lees_geheel_getal(onder, boven):
    getal_string = input('Geef getal tussen ' + str(onder) + ' en ' + str(boven) + ': ')
    while not (onder <= int(getal_string) <= boven):
        print('Geen positief geheel getal of buiten bereik!')
        getal_string = input('Geef getal tussen ' + str(onder) + ' en ' + str(boven) + ': ')
    return int(getal_string)


som = 0
for i in range(3):
    getal = lees_geheel_getal(10, 20)
    som += getal
som /= 3
print('Het gemiddelde van de 3 getallen is', som)
