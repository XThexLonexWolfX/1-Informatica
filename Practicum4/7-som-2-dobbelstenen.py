"""
auteur: Yorben Joosen
groep: PR09
datum: 20/10/2019
"""
import random
aantal_keer_7 = 0


def dobbel1():
    x = random.randrange(1, 6)
    return x


def dobbel2():
    x = random.randrange(1, 6)
    return x


for i in range(101):
    som_2_dobbelstenen = dobbel1() + dobbel2()
    if som_2_dobbelstenen == 7:
        aantal_keer_7 += 1
print('Tijdens de 100 beurten was de som van de twee dobbelstenen', aantal_keer_7, 'keer zeven')
