"""
auteur: Yorben Joosen
groep: PR09
datum: 20/10/2019
"""
import math
import numpy

print('{:0}{:^17}{:0}'.format(-1, 0, 1))
print('{:-^20}'.format('') + '>Y')
y_factor = 10
y_offset = 10
for x in numpy.arange(0.0, 2 * math.pi+ 0.5, 0.333):
    print('{:17}'.format(int((y_offset + y_factor * math.sin(x))) * ' ' + '*'))
    print('{:^21s}'.format('|'))
print('{:^20s}'.format('V'))
print('{:^20s}'.format('X'))
