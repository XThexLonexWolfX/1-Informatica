from werknemer import Werknemer
from datetime import date


class Bediende(Werknemer):
    def __init__(self, naam, geboortedatum, kinderen_ten_laste, maandwedde):
        super().__init__(naam, geboortedatum, kinderen_ten_laste)
        self.__maandwedde = maandwedde

    def __str__(self):
        return 'Bediende: ' + super().__str__() + ' maandwedde ' + str(self.__maandwedde)

    def __repr__(self):
        return 'Bediende(' + super().__repr__() + ', ' + str(self.__maandwedde) + ')'

    def get_maandwedde(self):
        return self.__maandwedde

    def set_maandwedde(self, nieuw):
        self.__maandwedde = nieuw

    def get_type_arbeidsovereenkomst(self):
        return 'Bediende'


def main():
    print('Test klasse Bediende:')
    b1 = Bediende('Mia', date(1995, 10, 16), 1, 2200.0)
    print('b1:', b1)
    b2 = Bediende('Jef', date(1996, 8, 21), 0, 1800.0)
    print('b2:', b2)
    b2.set_naam('Jefke')
    print("Na b1.set_naam('Jefke'):", b2)
    b2.set_geboortedatum(date(1997, 8, 21))
    print('Na b2.set_geboortedatum(date(1997, 8, 21)):', b2)
    print('b2.get_naam():', b2.get_naam())
    print('b2.get_geboortedatum():', b2.get_geboortedatum())
    b1.set_kinderen_ten_laste(2)
    print('Na b1.set_kinderen_ten_laste(1):', b1)
    b2.set_maandwedde(b2.get_maandwedde() * 1.05)
    print('b2.set_maandwedde(b2.get_maandwedde() * 1.05) (5% opslag):', b2)
    print('b1:', b1)
    print('b2:', b2)
    lijst = [b1, b2]
    print('lijst = [b1, b2]:', lijst)


if __name__ == '__main__':
    main()
