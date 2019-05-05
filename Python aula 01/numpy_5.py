# -*- coding: utf-8 -*-
"""
Created on Sat May  4 20:01:05 2019

@author: Aluno 10
"""

import numpy as np

a = np.array([[1, 2], [3,4]])
print(a)

#Repeat
print(np.repeat(a, 3))

print(np.repeat(a, 2, axis = 0))

print(np.repeat(a, 2, axis = 1))


#Tile
"""
Repete o array todo
"""
a = np.array([1, 2, 3])
print(np.tile(a, 2))

#dividindo um array -> split
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

#Split
print(np.array_split(a, 2, axis = 0))

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(b)

arrays = np.array_split(b, 4, axis = 0)

for array in arrays:
    print(array)
    
#Arrays de zeros
    
print(np.zeros(4))

print(np.zeros((2, 2)))


print(np.ones(4))
print(np.ones((2, 2)))
print(np.ones((5,4,6,8)))

#Arrys, Identidade

d = np.eye(3)
print(d)


#Indexação boleana

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)

idx = (a > 2)
print(idx)


#Juntando arrays

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

print(np.concatenate((a, b), axis = 0))


#Shuffle

a = np.arange(10)
np.random.shuffle(a)
print(a)

a = np.array([1, 10 + 2j, 20 + 5j], dtype = complex)
print(a)

print(a[1])
print(a[1] + a[2])
print(a[1] - a[2])
print(a[1] * a[2])
print(a[1] / a[2])

#gerando arrays

print(np.arange(10))

print(np.arange(1, 100, 2))

#lim spaces

print(np.linspace(2.0, 3.0, 5))









