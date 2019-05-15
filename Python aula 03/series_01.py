# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:48:04 2019

@author: Aluno 10
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

base = pd.read_csv('AirPassengers.csv')
print(base.head())

# =============================================================================
# Numero de passageiros e o mes
# 1940 a 1960
# Transformar o atributo mes em data
# =============================================================================

print(base.dtypes)

dataparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

print(dataparse)

base = pd.read_csv('AirPassengers.csv',
                   parse_dates = ['Month'],
                   index_col = 'Month',
                   date_parser = dataparse)

print(base.head())

# =============================================================================
# Transfora o data frame em um serie temporal
# =============================================================================

ts = base["#Passengers"]

# =============================================================================
# INdexação por intervalos
# =============================================================================

ts[:'1950-07-31']

ts['1950-01-01':'1950-07-31']

ts['1950']
ts.index.max()
ts.index.min()
plt.plot(ts)


# =============================================================================
# Agrupando por ano
# Codigo -> A, sgnifica a ano na função resample
# =============================================================================

ts_ano = ts.resample('A').sum()
plt.plot(ts_ano)

# =============================================================================
# Agrupas pelo mes
# =============================================================================

ts_mes = ts.groupby([lambda x: x.month]).sum()
ts_mes

plt.plot(ts_mes)

# =============================================================================
# Agrupas pelo mes ano
# =============================================================================

ts_mes_ano = ts.groupby([lambda x: (x.month, x.year)]).sum()
ts_mes_ano

ts_datas = ts['1960-01-01':'1960-12-01']
plt.plot(ts_datas)

# =============================================================================
# Decomposição da serie temporal
# =============================================================================

from statsmodels.tsa.seasonal import seasonal_decompose
decomposicao = seasonal_decompose(ts)

# =============================================================================
# Tendência
# =============================================================================

tendencia = decomposicao.trend
plt.plot(tendencia)
# =============================================================================
# Sazionalidade
# =============================================================================

sazonal = decomposicao.seasonal
plt.plot(sazonal)
# =============================================================================
# Efeito aleatorio
# =============================================================================

aleatorio = decomposicao.resid
plt.plot(aleatorio)

# =============================================================================
# Plotagem dos graficos
# dividindo em 4
# =============================================================================

plt.subplot(4, 1, 1)
plt.plot(ts, label = 'Original')
plt.legend(loc = 'best')

plt.subplot(4, 1, 2)
plt.plot(tendencia, label = 'Tendencia')
plt.legend(loc = 'best')

plt.subplot(4, 1, 3)
plt.plot(sazonal, label = 'Sazionalidade')
plt.legend(loc = 'best')

plt.subplot(4, 1, 4)
plt.plot(aleatorio, label = 'Aleatorio')
plt.legend(loc = 'best')

plt.tight_layout() #para mostrar o legends

# =============================================================================
# Previsão com media
# =============================================================================

ts.mean()

# =============================================================================
# Média do ultimo ano
# =============================================================================

ts['1960-01-01':'1960-12-01'].mean()

# =============================================================================
# Media movel
# =============================================================================

media_movel = ts.rolling(window = 12).mean()
media_movel
plt.plot(media_movel)
