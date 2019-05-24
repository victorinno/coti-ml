# =============================================================================
# Instalar o pacote scikit-fuzzy
# =============================================================================

from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
import skfuzzy

iris = datasets.load_iris()

# =============================================================================
# Transportar a matriz -> T = transformar linha em coluna
# Agrupamento parcial difuso
# Um elemento pode participar a mais de um grupo
# Data -> conjunto de dados que será analisado
# Error -> 0.005, valor minimo de error
# maxitter -> numero maximo de iteracoes
# =============================================================================

r = skfuzzy.cmeans(data = iris.data.T, c = 3, m = 2, error = 0.005,
                   maxiter = 1000, init = None)

# =============================================================================
# r -> retorna uma tupla com 7 posicoes
# =============================================================================

previsoes_porcentam = r[1]

# =============================================================================
# Probabilidade do primeiro registro estr em uma das 3 classes
# =============================================================================

print(previsoes_porcentam[0][1])
print(previsoes_porcentam[1][1])
print(previsoes_porcentam[2][1])

previsoes = previsoes_porcentam.argmax(axis = 0)

confusao = confusion_matrix(previsoes, iris.target)

print(confusao)
