# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:28:15 2019

@author: Aluno 10
"""

import numpy as np

# Arrange -> criar uma lista de numeros
array = np.arange(100000)
print(array)

#Arrays multdimensionais
mat = np.array([[1, 2], [3, 4]])
print(mat)

#randn
data = np.random.rand(2, 3)
print(data)

print(data.shape)

#dimensões

print(data.ndim)

#inserindo dados no array
arr = np.array([1, 2, 3])
print(arr)

print(np.insert(arr, 1, 10))

print(arr)

#Somatorio

a = np.array([[1, 2, 3], [4, 5, 6]])

print(a.sum())

#Somatorio no eixo 0
print(a.sum(axis = 0))

#Somatorio no eixo 1
print(a.sum(axis = 1))


print(np.insert(a, 1, 5, axis = 1))

#Juntando arrays

a1 = np.array([1, 2, 3])
print(np.append(a1, [4, 5, 6]))


a = np.array([[1, 2], [3, 4]])
print(a)

print(np.append(a, [[5, 6]], axis = 0))

#Transpose

print(a.T)

print(np.append(a.T, [[5, 6]], axis = 0))
