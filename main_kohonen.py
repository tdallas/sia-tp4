from kohonen_network import Kohonen
from data_parser import DataParser
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

parser = DataParser('europe.csv')

standarized_matrix = np.array(parser.get_standarized_matrix()).T


k_neurons = 5
kohonen = Kohonen(standarized_matrix, k_neurons, 2500)
kohonen.train() 

som_map = kohonen.construct_nodes_map()
u_matrix = kohonen.build_u_matrix()

countries_string = parser.parse_as_class()
neurons = [[[] for x in range(k_neurons)] for y in range(k_neurons)] 
for i in range(len(standarized_matrix)):
    best_i, best_j, best_difference = kohonen.get_best_matching(standarized_matrix[i])
    neurons[best_i][best_j].append(countries_string[i][0])
    print("Country: {}, Best neuron: {},{}".format(countries_string[i][0], best_i, best_j))

print(neurons)

plt.imshow(u_matrix, cmap='gray')  # black = close = clusters
plt.colorbar()
plt.show()