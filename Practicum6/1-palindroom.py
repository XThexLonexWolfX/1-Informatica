"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 08/11/2019
"""


def lees_lijst(aantal):
    lijst1 = []
    for i in range(aantal):
        getal = int(input('Geef getal '+str(i+1)+' : '))
        lijst1.append(getal)
    return lijst1


def is_lijst_palindroom(lijst):
    palindroom = True
    voor = 0
    achter = len(lijst) - 1
    while palindroom and voor < achter:
        palindroom = lijst[voor] == lijst[achter]
        voor += 1
        achter -= 1
    return palindroom


aantal = int(input('Geef het aantal: '))
lijst = lees_lijst(aantal)
if is_lijst_palindroom(lijst) == True:
    print(lijst, 'is een palindroom')
else:
    print(lijst, 'is geen palindroom')
