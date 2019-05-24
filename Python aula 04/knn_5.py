from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd
import numpy as np

base = pd.read_csv('heart.csv')

base.head()

base['target'].unique()

previsores = base.iloc[:, 0:13].values
classe = base.iloc[:, 13].values

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state = 0)

# KNN
knn  = KNeighborsClassifier(n_neighbors= 13, p=1)

knn.fit(x_treinamento, y_treinamento)

output = knn.predict(x_teste)

confusao = confusion_matrix(output, y_teste)
confusao

score = accuracy_score(output, y_teste)
score















