"""

auteur: Joosen Yorben
groep: PR09
datum: 11/10/2019
"""


def is_schrikkeljaar(jaar):
    return jaar % 4 == 0 and jaar % 100 != 0 or jaar % 400 == 0

jaar = int(input('Geef een jaartal 0..9999 (0 om te stoppen): '))
while jaar != 0:
    if jaar < 0 or jaar > 9999:
        print(jaar, 'ligt niet in het interval 0..9999')
    elif is_schrikkeljaar(jaar) == True:
        print(jaar, 'is een schrikkeljaar')
    else:
        print(jaar, 'is GEEN schrikkeljaar')
    jaar = int(input('Geef een jaartal 0..9999 (0 om te stoppen): '))
