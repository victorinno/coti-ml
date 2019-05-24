from sklearn.datasets import load_boston
boston = load_boston()

type(boston)

# dados
boston.data.shape

# nomes dos conjuntos de dados
boston.feature_names

# classe
boston.target


from sklearn.neighbors import KNeighborsRegressor
k= 9
knn  = KNeighborsRegressor(n_neighbors=k)
knn.fit(boston.data, boston.target)

print(boston.target[0])
print(knn.predict([boston.data[0]]))

# efetuar a previsão de 50 registros

import numpy as np
import matplotlib.pyplot as plt

x, y  = boston.data[:50], boston.target[:50]

y_ = knn.fit(x, y).predict(x)

y_


plt.plot(np.linspace(-1, 1, 50), y, label='data', color = 'black')
plt.plot(np.linspace(-1, 1, 50), y_, label='prediction', color = 'red')
plt.legend()
plt.show()

# erro quadrático medio
from sklearn.metrics import mean_squared_error
mean_squared_error(boston.target[:50], y_)










































