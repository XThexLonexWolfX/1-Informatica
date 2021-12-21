"""
auteur: Yorben Joosen
groep: PR09
datum: 18/10/2019
"""

import numpy

#Met while
"""print('   x         x²        x³     x**(1/2)')
x = 1
while x < 3.1:
    print('{:0.5f}'.format(x), '{:9.5f}'.format(x**2), '{:9.5f}'.format(x**3), '{:9.5f}'.format(x**(1/2)))
    x += 0.1"""
#Met for en numpy
print('   x         x²        x³     x**(1/2)')
for x in numpy.arange(1.0, 3.1, 0.1):
    print('{:0.5f}'.format(x), '{:9.5f}'.format(x**2), '{:9.5f}'.format(x**3), '{:9.5f}'.format(x**(1/2)))