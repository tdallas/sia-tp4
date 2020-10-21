from oja import Oja
import numpy as np
from data_parser import DataParser
from sklearn.decomposition import PCA 

parser = DataParser('europe.csv')
standarized_matrix = np.array(parser.get_standarized_matrix())

oja = Oja(standarized_matrix.T)
oja.train()

pca = PCA()
pca.fit_transform(standarized_matrix.T)

print('Primer Componente Principal con Oja')
print(oja.get_weights())

print('Primer Componente Principal con PCA')
print(pca.components_[0])