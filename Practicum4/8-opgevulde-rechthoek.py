"""
auteur: Yorben Joosen
groep: PR09
datum: 20/10/2019
"""
import random


def randomx():
    x = random.randrange(100)
    if x < 75:
        print(' ', end='')
    else:
        print('X', end='')


print('Druk rechtoek met ongeveer 75% spaties en 25% X')
print('+------------------+')
for rij in range(8):
    print('|', end='')
    for kolom in range(18):
        randomx()
    print('|')
print('+------------------+')
