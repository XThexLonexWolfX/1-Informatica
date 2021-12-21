from datetime import date


class Persoon:
    def __init__(self, naam, geboortedatum):
        self.__naam_van_de_persoon = naam
        self.__geboortedatum = geboortedatum
        self.__leeftijd = date.today().year - self.__geboortedatum.year - ((date.today().month, date.today().day) < (self.__geboortedatum.month, self.__geboortedatum.day))

    def __str__(self):
        return 'Naam: ' + str(self.__naam_van_de_persoon) + ' Geboortedatum: ' + str(self.__geboortedatum)

    def __repr__(self):
        return 'Persoon(' + str(self.__naam_van_de_persoon) + ', ' + str(self.__geboortedatum) + ')'

    def get_naam(self):
        return self.__naam_van_de_persoon

    def get_geboortedatum(self):
        return self.__geboortedatum

    def set_naam(self, nieuwe_naam):
        self.__naam_van_de_persoon = nieuwe_naam

    def set_geboortedatum(self, nieuwe_geboortedatum):
        self.__geboortedatum = nieuwe_geboortedatum

    def get_leeftijd(self):
        return self.__leeftijd


def main():
    print('Test klasse Persoon:')
    p1 = Persoon('Jan', date(2001, 11, 15))
    print('p1: ', p1)
    p2 = Persoon('Ann', date(2002, 9, 23))
    print('p2: ', p2)
    p1.set_naam('Jantje')
    print("Na p1.set_naam('Jantje'):", p1)
    p1.set_geboortedatum(date(2015, 11, 15))
    print('Na p1.set_geboortedatum(date(2015, 11, 15)):',  p1)
    print('p1.get_naam():', p1.get_naam())
    print('p1.get_geboortedatum():', p1.get_geboortedatum())
    lijst = [p1, p2]
    print('lijst = [p1, p2]:', lijst)


if __name__ == '__main__':
    main()
