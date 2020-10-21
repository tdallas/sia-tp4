from covid_parser import DataParser
from kohonen_network import Kohonen
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

covid_parser = DataParser('covid-data-arg.csv')

kohonen = Kohonen(covid_parser.get_standarized_matrix(), 100, 1000)
kohonen.train() 

som_map = kohonen.construct_nodes_map()
u_matrix = kohonen.build_u_matrix()

plt.imshow(u_matrix, cmap='gray')  # black = close = clusters
plt.colorbar()
plt.show()
