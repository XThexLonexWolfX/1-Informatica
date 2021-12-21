"""
auteur: Yorben Joosen
groep: PR09
datum: 18/10/2019
"""
print('decimaal', 'octaal', 'hexadecimaal', ' ', 'binair')
for i in range(33):
    print('{:>8}'.format(i), '{:>6}'.format(oct(i)), '{:>12}'.format(hex(i)), '{:>8}'.format(bin(i)))
