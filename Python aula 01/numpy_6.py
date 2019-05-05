# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:12:53 2019

@author: Aluno 10
"""

import numpy as np

val1, val2, val3 = np.loadtxt('dados.txt', skiprows = 1, unpack = True)


print(val1)
print(val2)
print(val3)


my_array = np.genfromtxt("dados2.txt", skip_header = 1, filling_values = 1000)
print(my_array)

data = np.genfromtxt('iris.data', delimiter = ',', usecols = (0, 1, 2, 3))
print(data)

print(len(data))

print(data.dtype)

print(data[:50, 0])

import matplotlib.pyplot as plt

plt.plot(data[:50, 0], c = 'Red', ls = ':', marker = 's', ms = 8,
         label = 'Comp. Sepala do Iris-Setosa')
plt.plot(data[50:100, 0], c = 'Black', ls = ':', marker = 'o', ms = 8,
         label = 'Comp. Sepala do Iris-Versicolor')
plt.legend()
plt.show()
