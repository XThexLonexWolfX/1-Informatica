from arbeider import Arbeider
from bediende import Bediende
from datetime import date

a1 = Arbeider('Wim', date(1994, 5, 18), 2, 15, 160)
a2 = Arbeider('Els', date(1992, 6, 13), 0, 13, 128)
a3 = Arbeider('Jos', date(1997, 3, 17), 0, 10, 187)
b1 = Bediende('Mia', date(1995, 10, 16), 1, 2200.0)
b2 = Bediende('Jef', date(1996, 8, 21), 0, 1800.0)
b3 = Bediende('Pim', date(1991, 11, 28), 1, 2600.0)
lijst = [a1, a2, a3, b1, b2, b3]


def overzicht(lijst):
    for i in range(6):
        print(str(lijst[i].get_naam()) + '     ' + str(lijst[i].get_geboortedatum()) + '       ' + str(lijst[i].get_kinderen_ten_laste()) + '            ' + str(lijst[i].get_type_arbeidsovereenkomst()) + '     ' + str(lijst[i].get_maandwedde()))


def arbeiders_overzicht(lijst):
    for i in range(3):
        print(str(lijst[i].get_naam()) + '     ' + str(lijst[i].get_geboortedatum()) + '       ' + str(lijst[i].get_kinderen_ten_laste()) + '     ' + str(lijst[i].get_maandwedde()))


def bedienden_overzicht(lijst):
    for i in range(3, 6):
        print(str(lijst[i].get_naam()) + '     ' + str(lijst[i].get_geboortedatum()) + '       ' + str(lijst[i].get_kinderen_ten_laste()) + '     ' + str(lijst[i].get_maandwedde()))


print('Personeeloverzicht:')
print('naam    geboortedatum kind arbeidsovereenkomst maandwedde')
overzicht(lijst)
print('Overzicht arbeiders:')
print('naam    geboortedatum kind maandwedde')
arbeiders_overzicht(lijst)
print('Overzicht bedienden:')
print('naam    geboortedatum kind maandwedde')
bedienden_overzicht(lijst)
