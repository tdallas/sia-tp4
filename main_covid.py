from covid_parser import DataParser
from kohonen_network import Kohonen
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

covid_parser = DataParser('covid-data-arg.csv')

kohonen = Kohonen(covid_parser.get_standarized_matrix(), 100, 800)
kohonen.train() 

som_map = kohonen.construct_nodes_map()
u_matrix = kohonen.build_u_matrix()

plt.imshow(u_matrix, cmap='gray')  # black = close = clusters
plt.colorbar()
plt.show()

k_neurons = 100

days = list(range(0, 230))

standarized_matrix = np.array(covid_parser.get_standarized_matrix())

neurons = [[[] for x in range(k_neurons)] for y in range(k_neurons)] 
for i in range(len(standarized_matrix)):
    best_i, best_j, best_difference = kohonen.get_best_matching(standarized_matrix[i])
    neurons[best_i][best_j].append(' Day: ' + str(days[i]))
    print("Day: {}, Best neuron: {},{}, Best difference: {}".format(days[i], best_i, best_j, best_difference))

# print('días por neurona')
# print(neurons)

fig, ax = plt.subplots()
for i in range(k_neurons):
    for j in range(k_neurons):
        if len(neurons[i][j]) > 0:
            ax.scatter(i, j)
            ax.annotate('\n'.join(neurons[i][j]), (i, j))
        else:
            ax.scatter(i, j)
plt.title('Días agrupados por neurona')
plt.tight_layout()
plt.show()

plt.imshow(u_matrix, cmap='gray', origin='lower')  # black = close = clusters
plt.colorbar()
plt.title('Matriz U')
plt.tight_layout()
plt.show()