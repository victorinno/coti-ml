# =============================================================================
# Instalar o pyclustering
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer
from sklearn import datasets

iris = datasets.load_iris()

# =============================================================================
# Não precisa configurar o numero de cluster, ele descobre sozinho indices
# aleatorios o medoids
# =============================================================================

cluster = kmedoids(iris.data[:, 0:2], [3, 12, 20])
cluster.get_medoids()
cluster.process()

previsoes = cluster.get_clusters()

print(len(previsoes))

for grupo in previsoes:
    print(len(grupo))

print(previsoes[0])

# =============================================================================
# pegar medoids -> são usados como centro para a classificação
# =============================================================================

medoids = cluster.get_medoids()
print(medoids)

v = cluster_visualizer()
v.append_clusters(previsoes, iris.data[:, 0:2])
v.append_cluster(medoids, iris.data[:, 0:2], marker= '*',
                 markersize = 15)
v.show()

