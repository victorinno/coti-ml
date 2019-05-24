# instalar pacote do graphviz
# pip install graphviz
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier

# Treinamento
arvore =  DecisionTreeClassifier()
arvore.fit(x_treinamento, y_treinamento)

# Efetuar as previsoes
previsoes = arvore.predict(x_teste)
previsoes

confusao = confusion_matrix(y_teste, previsoes)
confusao

taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_acerto
