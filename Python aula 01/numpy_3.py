# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:17:27 2019

@author: Aluno 10
"""

import numpy as np

l = [10, 20, 30, 40, 50]

#converte a lista
a = np.array(l)
print(a)

#copia a lista
"""
gera referência de memoria por conta do numpy, se fosse lista do python seria 
uma copia mesmo
"""

b = a[:] 
print(b)

b[0] = 20000

print(a[0])

a = np.array(l)

c = a.copy()

a[0] = 1000

print(a)
print(c)
