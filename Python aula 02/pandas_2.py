# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:38:37 2019

@author: Aluno 10
"""

import pandas as pd
import numpy as np

df = pd.DataFrame([
                    ['PE', 'Pernambuco', 'Recife'],
                    ['RJ', 'Rio de Janeiro', 'Rio de Janeiro'],
                    ['PB', 'Paraiba', 'João Pessoa'],
                    ['SP', 'São Paulo', 'São Paulo'],
                    ['MG', 'Minas Gerais', 'Belo Horizonte'],
                    ['CE', 'Ceará', 'Fortaleza'],
                ], columns = ['Sigla', 'Nome', 'Capital'])

print(df)
print(df['Sigla'])

print("====Indice do data frame")

print(df.index)

print("====Acessar o indice igual o index, mas está deprecida")
print("====Nem sempre o indice precisa ser numerico, ele pode ser categórico")
print(df.ix[0])
print("====Dá para usar o iloc ou loc")
print("====loc inclui a ultima posição quando é particionado")
print("====iloc não inclui a ultima posição quando é particionado")
print(df.iloc[:2])
print("====")
print(df.loc[:2])

print("====Subistituir o indice")
df.index = df['Sigla']
print(df)
print("====Remover colunas")
del df['Sigla']
print(df)