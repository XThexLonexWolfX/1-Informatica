"""

auteur: Joosen Yorben
groep: PR09
datum: 13/10/2019
"""


def rechthoek(spaties, breedte, hoogte, opvulteken): #breedte en hoogte weggedaan, want is niet nodig voor dennenboom
    hoogte = 2
    breedte = 3
    for rij in range(hoogte):                #Was eerst hoogte, maar voor dennenboom is hoogte altijd 2
        for kolom in range(spaties - 1):     #Komt anders niet overeen met de top van de dennenboom
            print(' ', end='')
        for kolom in range(breedte):          #Was eerst breedte, maar voor dennenboom is breedte altijd 3
            print(opvulteken, end='')
        print('')


def driehoek(spaties, hoogte, opvulteken):
    breedte = 1
    for rij in range(hoogte):
        for kolom in range(spaties):
            print(' ', end='')
        for kolom in range(breedte):
            print(opvulteken, end='')
        spaties -= 1
        breedte += 2
        print('')



def dennenboom(spaties, driehoeken, opvulteken):
            hoogte = 2
            while driehoeken > 0:
                driehoek(spaties, hoogte, opvulteken)
                driehoeken -= 1
                hoogte += 1
            rechthoek(spaties, breedte, hoogte, opvulteken)



spaties = int(input('Geef het aantal spaties: '))
hoogte = 2
breedte = 3
#hoogte = int(input('Geef de hoogte: ')) (wordt niet gebruikt bij dennenboom)
#breedte = int(input('Geef de breedte: '))  wordt niet gebruikt bij dennenboom)
opvulteken = input('Geef het opvulteken: ')
driehoeken = int(input('Geef het aantal keer driehoeken: '))
#rechthoek(spaties, breedte, hoogte, opvulteken) (wordt niet gebruikt bij dennenboom)
#driehoek(spaties, hoogte, opvulteken) (wordt niet gebruikt bij dennenboom)
dennenboom(spaties, driehoeken, opvulteken)
