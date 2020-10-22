from oja import Oja
import numpy as np
from data_parser import DataParser
from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt
import math

parser = DataParser('europe.csv')
standarized_matrix = np.array(parser.get_standarized_matrix()).T

oja = Oja(standarized_matrix)
weights_on_iteration, iterations = oja.train()
oja_component = oja.get_weights()

pca = PCA()
pca.fit_transform(standarized_matrix)
pca_component = pca.components_[0]

# Cambio los signos si es que salieron al reves
if oja_component[0] < 0:
    oja_component = [-oja_component[i] for i in range(len(oja_component))]
    oja_component = np.array(oja_component)
    for i in range(len(weights_on_iteration)):
        weights_on_iteration[i] = [-weights_on_iteration[i][j] for j in range(len(weights_on_iteration[i]))]
        weights_on_iteration[i] = np.array(weights_on_iteration[i])

weights_errors = np.zeros((len(iterations), len(weights_on_iteration[0])))
for i in range(len(weights_on_iteration)):
    weights_errors[i] = abs(weights_on_iteration[i] - pca_component)

weights_names = ['Area','GDP','Inflation','Life.expect','Military','Pop.growth','Unemployment']

for i in range(len(weights_on_iteration[0])):
    plt.plot(iterations, weights_errors[:,i], label=weights_names[i])
plt.legend(title='Variable')
plt.xlabel("Iteración", fontsize=16)
plt.ylabel("Error", fontsize=16)
plt.title('Primer Componente Principal errores')
plt.tight_layout()
plt.show()

print('Primer Componente Principal con Oja')
print(oja_component)

print('Primer Componente Principal con PCA')
print(pca_component)

print('Errores finales')
print(abs(oja_component - pca_component))

countries_string = parser.parse_as_class()
countries = []
values = []
for i in range(len(standarized_matrix)):
    countries.append(countries_string[i][0])
    values.append(sum(standarized_matrix[i] * pca_component))

countries_copy = countries.copy()
pca_values = values.copy()

tupla = list(zip(countries, values))
tupla.sort(key = lambda t: t[1])

for i in range(len(tupla)):
    plt.scatter(tupla[i][0], tupla[i][1])
plt.xlabel("País", fontsize=16)
plt.xticks(rotation=45)
plt.ylabel("Valor", fontsize=16)
plt.title('Valores de paises con PCA')
plt.tight_layout()
plt.show()

countries = []
values = []
for i in range(len(standarized_matrix)):
    countries.append(countries_string[i][0])
    values.append(sum(standarized_matrix[i] * oja_component))

oja_values = values.copy()

tupla = list(zip(countries, values))
tupla.sort(key = lambda t: t[1])

for i in range(len(tupla)):
    plt.scatter(tupla[i][0], tupla[i][1])
plt.xlabel("País", fontsize=16)
plt.xticks(rotation=45)
plt.ylabel("Valor", fontsize=16)
plt.title('Valores de paises con Oja')
plt.tight_layout()
plt.show()

print("Comparación de valores oja y pca:")
for i in range(len(countries_copy)):
    print("{}, OJA: {}, PCA: {}".format(countries[i], oja_values[i], pca_values[i]))