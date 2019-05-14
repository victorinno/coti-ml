# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:11:56 2019

@author: Aluno 10
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
import statsmodels.formula.api as sm

base = pd.read_csv("Eleicao.csv", sep = ";")
print(base.head())

#Grafico das despesas pela situação
#Candidatos eleitos e não eleitos

plt.scatter(base.DESPESAS, base.SITUACAO)

#Alguns valores do conjunto de dados
print(base.describe())

print(np.corrcoef(base.DESPESAS, base.SITUACAO))

#BASE -> DESPESAS em X

x = base.iloc[:, 2].values
y = base.iloc[:, 1].values

print(x.shape)

#Transformar em matriz

x = x[:, np.newaxis]
print(x.shape)

#Criação do modelo de regressão

modelo = LogisticRegression()
modelo.fit(x, y)

#Parametros de modelo
print(modelo.coef_)
print(modelo.intercept_)


