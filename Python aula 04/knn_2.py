# instalação do scikit learn e dependencias
# pip install -U scikit-learn

import pandas as pd
import numpy as np

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

test.head()

test['class'].unique()

# Criando vetores de teste e treinamento

cols = ['shoe size', 'height']
cols2 = ['class']


# Treinamento
x_train = train.as_matrix(cols)
y_train = train.as_matrix(cols2)

# teste
x_test  = test.as_matrix(cols)
y_test = test.as_matrix(cols2)


from sklearn.neighbors import KNeighborsClassifier

# Treinamento das amostras
# knn ->
# weights -> 
knn  = KNeighborsClassifier(n_neighbors=3, weights='distance')


# Treinando
knn.fit(x_train, y_train.ravel())


# teste das amostras -> previsao
output = knn.predict(x_test)

output

y_test[0]
output[0]

correct = 0.0

for i in range(len(output)):
    if y_test[i][0] == output[i]:
        correct += 1

correct / len(output) * 100



    
    
    
    
    















