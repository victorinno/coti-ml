# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:56:35 2019

@author: Aluno 10
"""

import pandas as pd
import numpy as np

print('Series -> dados em uma unica dimensao')

s = pd.Series([1,4,5,6,7,10,6])
print(s)
print(s[0])

print(s[2:4])

print(' Descrição da serie(antigo summary do R)')

print(s.describe())

print('Media')
print(s.mean())

print('Mediana')
print(s.median())

print('Verificar duplicados')
print(s.duplicated())

s2 = pd.Series([11, 5, 8])
print('append')

print(s.append(s2))

print('Pandas -> antigo data frame do R -> tabela com linhas e colunas')

df = pd.DataFrame([
            ['Python web', 2000],
            ['Machine learning', 3000],
            ['Lógica de programação', 4500]
            
        ])

print(df)
print('Nome de colunas')
df = pd.DataFrame([
            ['Python web', 2000],
            ['Machine learning', 3000],
            ['Lógica de programação', 4500]
        ], columns = ['curso', 'alunos'])

print(df)


print('selecionando por colunas')
print(df['curso'])
print(df['alunos'])

print('as funções podem ser sobre as colunas')

print(df['alunos'].mean())
print(df['alunos'].median())

print("Acessar o conteudo do dataFrame pelo iloc -> indice")
print(df.iloc[1])
print(df.iloc[1]['alunos'])
