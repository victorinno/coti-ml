import pandas as pd
from sklearn.model_selection import train_test_split
# GaussianNB -> não trabalha com dados categoricos.
# Efetuar o pré processamento para poder 
# efetuar o processamento.

from sklearn.naive_bayes import GaussianNB

credito = pd.read_csv('Credit.csv')

len(credito)

credito.shape

# Dividir as colunas de previsores e classes
previsores = credito.iloc[:, 0:20].values
classe = credito.iloc[:, 20].values

previsores[0: 20]


# Efetuar o pré processamento dos dados
from sklearn.preprocessing import LabelEncoder

# Criar o objeto
labelencoder = LabelEncoder()


previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelencoder.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder.fit_transform(previsores[:, 5])
previsores[:, 6] = labelencoder.fit_transform(previsores[:, 6])
previsores[:, 8] = labelencoder.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder.fit_transform(previsores[:, 9])
previsores[:, 11] = labelencoder.fit_transform(previsores[:, 11])
previsores[:, 13] = labelencoder.fit_transform(previsores[:,13])
previsores[:, 14] = labelencoder.fit_transform(previsores[:, 14])
previsores[:, 16] = labelencoder.fit_transform(previsores[:, 16])
previsores[:, 18] = labelencoder.fit_transform(previsores[:, 18])
previsores[:, 19] = labelencoder.fit_transform(previsores[:, 19])


previsores[0]


# Dividir o conjunto de dados
x_treinamento,x_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state = 0)

# criar o objeto do naive
naive_bayes = GaussianNB()
naive_bayes.fit(x_treinamento, y_treinamento)

# predict
previsoes = naive_bayes.predict(x_teste)
previsoes

from sklearn.metrics import confusion_matrix, accuracy_score
confusao =  confusion_matrix(y_teste, previsoes)
confusao

taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_acerto


# Melhor visualização da matriz de confusao
from yellowbrick.classifier import ConfusionMatrix

#Efetuar o treinamento
v  = ConfusionMatrix(GaussianNB())
v.fit(x_treinamento, y_treinamento)
v.score(x_teste, y_teste)
v.poof()
































































