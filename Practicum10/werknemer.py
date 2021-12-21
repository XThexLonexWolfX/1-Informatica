from persoon import Persoon
from datetime import date


class Werknemer(Persoon):
    def __init__(self, naam, geboortedatum, kinderen_ten_laste):
        super().__init__(naam, geboortedatum)
        self.__kinderen_ten_laste = kinderen_ten_laste

    def __str__(self):
        return 'Werknemer: ' + super().__str__() + ' Kinderen ten laste: ' + str(self.__kinderen_ten_laste)

    def __repr__(self):
        return 'Werknemer(' + super().__repr__() + ', ' + str(self.__kinderen_ten_laste) + ')'

    def get_kinderen_ten_laste(self):
        return self.__kinderen_ten_laste

    def set_kinderen_ten_laste(self, nieuw_kinderen_ten_laste):
        self.__kinderen_ten_laste = nieuw_kinderen_ten_laste

    def get_type_arbeidsovereenkomst(self):
        return 'Werknemer'


def main():
    print('Test klasse Werknemer:')
    w1 = Werknemer('Jan', date(1996, 11, 15), 0)
    print('w1:', w1)
    w2 =  Werknemer('Ann', date(2002, 9, 23), 0)
    print('w2:', w2)
    w1.set_naam('Jantje')
    print("Na w1.set_naam('Jantje'):", w1)
    w1.set_geboortedatum(date(2015, 11, 15))
    print('Na w1.set_geboortedatum(date(2015, 11, 15)):', w1)
    print('w1.get_naam():', w1.get_naam())
    print('w1.get_geboortedatum():', w1.get_geboortedatum())
    w2.set_kinderen_ten_laste(1)
    print('Na w2.set_kinderen_ten_laste(1):', w2)
    lijst = [w1, w2]
    print('lijst = [w1, w2]:', lijst)


if __name__ == '__main__':
    main()
