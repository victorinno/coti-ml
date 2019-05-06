# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:58:29 2019

@author: Aluno 10
"""

import pandas as pd
import pydataset

print("===Conjunto de dados no padrão de um dataframe")
print(pydataset.data())

print("===Tipo dataframe")
print(type(pydataset.data()))

titanic = pydataset.data("titanic")
print(titanic.head())
print(titanic.tail(10))

print(titanic.describe())

print("===Contar valores")
print(titanic['class'].value_counts())

print("Tamanho do dataset")
print(len(pydataset.data()))

