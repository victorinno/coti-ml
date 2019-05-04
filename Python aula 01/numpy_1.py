# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:27:41 2019

@author: Aluno 10
"""

import numpy

a = numpy.array([10,20,30,50])
print(a)

print(type(a))

mat = numpy.array([[1,2], [3,4]])
print(mat)

#Acessando posição da matriz
print(mat[1,1])

#Indice negativo: de traz pra frente
print(mat[-1,-1])

#Transposição
print(mat.transpose())

m1 = numpy.array(numpy.array([[1,2],[3,4]]))
m2 = numpy.array(numpy.array([[5,6],[7,8]]))

print(m1)
print(m2)

#Operações

print(m1 + m2)

print(m1 - m2)

# Funções

m3 = numpy.array([1,2,3,4])

print(m3)

# Argmax -> indice do maior elemento

p = m3.argmax()

print(m3[p])

# Argmin -> indice do menor elemento
p = m3.argmin()
print(m3[p])




