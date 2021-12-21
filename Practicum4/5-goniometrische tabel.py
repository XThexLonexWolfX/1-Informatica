"""
auteur: Yorben Joosen
groep: PR09
datum: 18/10/2019
"""

import math
iets = 'sin'


def gradennaarradialen():
    radialen = graden*(math.pi/180)
    return radialen


print('      0°     30°     45°     60°     90°     180°     270°')
while iets == 'sin':
    graden = 0
    print('sin', '{:.4f}  '.format(math.sin(gradennaarradialen())), end='')
    graden = 30
    print('{:0.4f}  '.format(math.sin(gradennaarradialen())), end='')
    graden = 45
    print('{:0.4f}  '.format(math.sin(gradennaarradialen())), end='')
    graden = 60
    print('{:0.4f}  '.format(math.sin(gradennaarradialen())), end='')
    graden = 90
    print('{:0.4f}  '.format(math.sin(gradennaarradialen())), end='')
    graden = 180
    print('{:0.4f}  '.format(math.sin(gradennaarradialen())), end='')
    graden = 270
    print('{:0.4f}'.format(math.sin(gradennaarradialen())))
    iets = 'cos'
while iets == 'cos':
    graden = 0
    print('cos', '{:0.4f}  '.format(math.cos(gradennaarradialen())), end='')
    graden = 30
    print('{:0.4f}  '.format(math.cos(gradennaarradialen())), end='')
    graden = 45
    print('{:0.4f}  '.format(math.cos(gradennaarradialen())), end='')
    graden = 60
    print('{:0.4f}  '.format(math.cos(gradennaarradialen())), end='')
    graden = 90
    print('{:0.4f} '.format(math.cos(gradennaarradialen())), end='')
    graden = 180
    print('{:0.4f}  '.format(math.cos(gradennaarradialen())), end='')
    graden = 270
    print('{:0.4f}'.format(math.cos(gradennaarradialen())))
    iets = 'tan'
while iets == 'tan':
    graden = 0
    print('tan', '{:0.4f}  '.format(math.tan(gradennaarradialen())), end='')
    graden = 30
    print('{:0.4f}  '.format(math.tan(gradennaarradialen())), end='')
    graden = 45
    print('{:0.4f}  '.format(math.tan(gradennaarradialen())), end='')
    graden = 60
    print('{:0.4f}     '.format(math.tan(gradennaarradialen())), end='')
    graden = 90
    print('{:0.4f} '.format(math.inf), end='')
    graden = 180
    print('{:0.4f}     '.format(math.tan(gradennaarradialen())), end='')
    graden = 270
    print('{:0.4f}'.format(- math.inf), end='')
    iets= 'stop'