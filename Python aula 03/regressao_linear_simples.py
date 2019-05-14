# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:03:59 2019

@author: Aluno 10
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

#carregando os dados que serão usados
base = pd.read_csv('cars.csv')

base = base.drop('Unnamed: 0', axis = 1)

print(base.head())

#a biblioteca precisa uma matrix não aceia dataframe
#Dist
x = base.iloc[:,1].values
#Speed
y = base.iloc[:,0].values

correlacao = np.corrcoef(x,y)
print(correlacao)

x = x.reshape(-1,1)
print(x[0:10])

y = y.reshape(-1,1)
print(y[0:10])

#Criação do modelo de regressão linear
modelo = LinearRegression()
modelo.fit(x, y)

print(modelo.intercept_)
print(modelo.coef_)

plt.scatter(x,y)
plt.plot(x, modelo.predict(x), color = "red")

print(modelo.intercept_ + modelo.coef_ * 22)

teste = np.array([[22], [23], [24], [35]])
print(teste)

#residuais: soma dos residuais

print(modelo._residues)

from yellowbrick.regressor import ResidualsPlot

#plotagem dos residuais
visualizador = ResidualsPlot(modelo)
visualizador.fit(x, y)
visualizador.poof()
