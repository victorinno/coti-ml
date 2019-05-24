import numpy as np
from sklearn import datasets, neighbors

# Datasets do iris
iris = datasets.load_iris()

# Dados do conjunto de iris -> atributos
x = iris.data

# DESC
iris.DESCR

# Classe -> target
y = iris.target

# nome das classes
iris.target_names


# Dividir  vetor de train e test
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 42) 

print(len(x_train))
print(len(x_test))

from sklearn.neighbors import KNeighborsClassifier

# Treinamento
knn  = KNeighborsClassifier(n_neighbors=18, p=2)

# Treinando
knn.fit(x_train, y_train.ravel())

# efetuando o teste
outputs = knn.predict(x_test)

outputs

correct = 0.0

for i in range(len(outputs)):
    if y_test[i] ==  outputs[i]:
        correct += 1
        
correct / len(outputs) * 100








































