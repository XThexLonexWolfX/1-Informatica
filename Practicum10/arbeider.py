from werknemer import Werknemer
from datetime import date


class Arbeider(Werknemer):
    def __init__(self, naam, geboortedatum, kinderen_ten_laste, uurloon, aantal_uren):
        super().__init__(naam, geboortedatum, kinderen_ten_laste)
        self.__uurloon = uurloon
        self.__aantal_uren = aantal_uren

    def __str__(self):
        return 'Arbeider: ' + super().__str__() + ' uurloon: ' + str(self.__uurloon) + ' uren: ' + str(self.__aantal_uren)

    def __repr__(self):
        return 'Arbeider(' + super().__repr__() + ', ' + str(self.__uurloon) + ', ' + str(self.__aantal_uren) + ')'

    def get_uurloon(self):
        return self.__uurloon

    def get_aantal_uren(self):
        return self.__aantal_uren

    def set_uurloon(self, nieuw):
        self.__uurloon = nieuw

    def set_aantal_uren(self, nieuw):
        self.__aantal_uren = nieuw

    def get_type_arbeidsovereenkomst(self):
        return 'Arbeider'

    def get_maandwedde(self):
        return self.__uurloon * self.__aantal_uren



def main():
    print('Test klasse Arbeider:')
    a1 = Arbeider('Wim', date(1994, 5, 18), 2, 15, 160)
    print('a1:', a1)
    a2 = Arbeider('Els', date(1992, 6, 13), 0, 13, 128)
    print('a2:', a2)
    print('a1.get_maandwedde():', a1.get_maandwedde())
    print('a2.get_maandwedde():', a2.get_maandwedde())
    a2.set_uurloon(14)
    print('Na a2.set_uurloon(14):', a2)
    a2.set_aantal_uren(140)
    print('Na a2.set_aantal_uren(140):', a2)
    print('a2.get_uurloon():', a2.get_uurloon())
    print('a2.get_aantal_uren():', a2.get_aantal_uren())
    print('a2.get_maandwedde():', a2.get_maandwedde())
    print('a1:', a1)
    print('a2:', a2)
    lijst = [a1, a2]
    print('lijst = [a1, a2]:', lijst)



if __name__ == '__main__':
    main()
