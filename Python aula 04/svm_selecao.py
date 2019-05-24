import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC

# Carregar os dados
# pré processamento
# dividir o conjunto de dados

# Treinamento
svm = SVC()

svm.fit(x_treinamento, y_treinamento)
previsoes =  svm.predict(x_teste)


taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_acerto

# Efetuar a seleção de atributos
#Adicionar a biblioteca para criação de florestas randomicas
from sklearn.ensemble import ExtraTreesClassifier

forest = ExtraTreesClassifier()
forest.fit(x_treinamento, y_treinamento)
importancias = forest.feature_importances_

# Efetuar o treinamento com os atributos mais importantes.
x_treinamento2 =  x_treinamento[:, [0,1,2,3]]
x_teste2 = x_teste[:, [0,1,2,3]]

# Treinamento
svm2 = SVC()
svm2.fit(x_treinamento2, y_treinamento)
previsoes2 = svm2.predict(x_teste2)
taxa_acerto = accuracy_score(y_teste, previsoes2)
taxa_acerto





















