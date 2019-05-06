# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:10:19 2019

@author: Aluno 10
"""

import pandas as pd
import pydataset

print("===Dados categoricos")
titanic = pydataset.data("titanic")

print(titanic.head(5))
print(titanic.columns)
print("===Numero de bytes usados")
print(titanic['class'].nbytes)

print("===Classe")
print(type(titanic['class']))

print("===Transforma em dados categoricos do pandas")
titanic['class'] = titanic['class'].astype('category')
#print(titanic['class'])
print(titanic['class'].nbytes)


