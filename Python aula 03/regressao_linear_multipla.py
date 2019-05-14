# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:34:49 2019

@author: Aluno 10
"""

from yellowbrick.regressor import ResidualsPlot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

base = pd.read_csv('mt_cars.csv')
base = base.drop(['Unnamed: 0'], axis = 1)

print(base.head())
print(base.shape)

#Dados da regressão multipla

x = base.iloc[:, 1:4].values
y = base.iloc[:, 0].values

print(x[0:10])
print(y[0:10])

#Regressão multipla

modelo = LinearRegression()
modelo.fit(x,y)

print(modelo.score(x,y))

#predição
registro = np.array([[4,200,100]])

print(modelo.predict(registro))

