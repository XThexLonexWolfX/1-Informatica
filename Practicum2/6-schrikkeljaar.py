"""

auteur : Joosen Yorben
groep : PR09
datum : 05/10/2019

"""
jaartal = int(input('Geef een jaartal 1000..3000 (0 om te stoppen): '))
schrikkeljaar = 0
while jaartal != 0:
    if jaartal < 1000 or jaartal > 3000:
        print(jaartal, 'ligt niet in het interval 1000..3000 !')
    while 1000 <= jaartal <= 3000:
        if jaartal % 4 == 0 and jaartal % 100 != 0 or jaartal % 400 == 0:
            print(jaartal, 'is een schrikkeljaar')
            jaartal = int(input('Geef een jaartal 1000..3000 (0 om te stoppen: '))
        else:
            print(jaartal, 'is GEEN schrikkeljaar')
            jaartal = int(input('Geef een jaartal 1000..3000 (0 om te stoppen): '))