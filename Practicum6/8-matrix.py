"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 13/11/2019
"""
from random import randrange


def vulmatrix(dimrij, dimkolom, onder, boven):
    m = []
    for i in range(dimrij):
        m.append([])
        for j in range(dimkolom):
            m[i].append(randrange(onder, boven))
    return m


def drukmatrix(titel, m):
    print(titel + ': (' + str(len(m)) + 'x' + str(len(m[0])) + ')')
    for i in range(len(m)):
        for j in range(len(m[0])):
            print('{:3d}'.format(m[i][j]), end='')
        print()


def scalaire_som(matrix, getal):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            som = matrix[i][j] + getal
            print('{:3d}'.format(som), end='')
        print()


def scalair_product(matrix, getal):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            product = matrix[i][j] * getal
            print('{:3d}'.format(product), end='')
        print()


def matrix_getransponneerde(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print('{:3d}'.format(matrix[j][i]), end='')
        print()


def matrix_som(mat1, mat2):
    print('matrix_som(mat1, mat2): (3x3)')
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            element = mat1[i][j] + mat2[i][j]
            print('{:3d}'.format(element), end='')
        print()

def matrix_product(mat1, mat2):
    print('matrix_product(mat1,mat2): (3x3)')
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            product = mat1[i][0] * mat2[0][j] + mat1[i][1] * mat2[1][j] + mat1[i][2] * mat2[2][j]
            print('{:3d}'.format(product), end=' ')
        print()


mat1 = vulmatrix(3, 3, 1, 9)
mat2 = vulmatrix(3, 3, 1, 9)
drukmatrix('mat1', mat1)
print('scalaire_som(mat1, 10)')
scalaire_som(mat1, 10)
drukmatrix('mat2', mat2)
print('scalaire_som(mat2, 10)')
scalaire_som(mat2, 10)
print('getransponeerde mat1')
matrix_getransponneerde(mat1)
print('getransponeerde mat2')
matrix_getransponneerde(mat2)
print('scalair product(mat1, 10')
scalair_product(mat1, 10)
print('scalair product(mat2, 10')
scalair_product(mat2, 10)
matrix_som(mat1, mat2)
matrix_product(mat1, mat2)
