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

# =============================================================================
# #Grafico das despesas pela situação
# #Candidatos eleitos e não eleitos
# =============================================================================
plt.scatter(base.DESPESAS, base.SITUACAO)

# =============================================================================
# #Alguns valores do conjunto de dados
# =============================================================================
print(base.describe())

print(np.corrcoef(base.DESPESAS, base.SITUACAO))

# =============================================================================
# #BASE -> DESPESAS em X
# =============================================================================

x = base.iloc[:, 2].values
y = base.iloc[:, 1].values

print(x.shape)

# =============================================================================
# #Transformar em matriz
# =============================================================================

x = x[:, np.newaxis]
print(x.shape)

# =============================================================================
# #Criação do modelo de regressão
# =============================================================================

modelo = LogisticRegression()
modelo.fit(x, y)

# =============================================================================
# #Parametros de modelo
# =============================================================================
print(modelo.coef_)
print(modelo.intercept_)

# =============================================================================
# #Valores que serão previstos
# =============================================================================

x_teste = np.linspace(10,3000)
len(x_teste)

# =============================================================================
# Calculo da sigmoid do x, função utilizada na regressão logística
# =============================================================================
def model(x):
    return 1 / (1 + np.exp(-x))

# =============================================================================
# Ravel -> numpy array matriz para vetor
# =============================================================================

r = model(x_teste * modelo.coef_ + modelo.intercept_).ravel()

plt.scatter(x, y)
plt.plot(x_teste, r, c = 'red')

# =============================================================================
# Utilizar o arquivo com os novos candidatos
# Uma nova previsão
# =============================================================================

base_previsoes = pd.read_csv('NovosCandidatos.csv', sep = ';')
despesas = base_previsoes.iloc[:, 1].values

despesas = despesas[:, np.newaxis]
print(despesas.shape)
previsoes_teste = modelo.predict(despesas)
print(previsoes_teste)

print(base_previsoes)
