# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:22:07 2019

@author: Aluno 10
"""

import pandas as pd

pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 10)
#pd.set_option('display.width', 1000)

help(pd.read_csv)

print("===ler um xls")

populacao = pd.read_excel('total-populacao-pernambuco.xls')
print(populacao.head())

print("===Tratar por coluna")
print(populacao['Total de mulheres'])
print("===Mulheres por homem por cidade")
print(populacao['Total de mulheres'] / populacao['Total de homens'])

print("===Mulheres por homem")
print(populacao['Total de mulheres'].sum() / populacao['Total de homens'].sum())

print("===Mulheres por homem Razão")
print(100 * populacao['Total de mulheres'] / (populacao['Total de mulheres'].sum() / populacao['Total de homens'].sum()))

