"""
auteur: Yorben Joosen
groep: PR09
datum: 18/10/2019
"""
import math


def cirkel_omtrek(r):
    cirkelomtrek = 2*math.pi*r
    return cirkelomtrek


def bol_volume(r):
    bolvolume = 4*math.pi*r**3/3
    return bolvolume


print('straal', '  ', 'omtrek', '   ', 'volume')
for r in range(1, 11):
    print('{:>6}'.format(r), '{:8.3f}'.format(cirkel_omtrek(r)), '{:11.3f}'.format(bol_volume(r)))
