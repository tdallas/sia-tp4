from kohonen_network import Kohonen
from data_parser import DataParser
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

parser = DataParser('europe.csv')

kohonen = Kohonen(parser.get_standarized_matrix(), 50, 500)
kohonen.train() 

som_map = kohonen.construct_nodes_map()
u_matrix = kohonen.build_u_matrix()

plt.imshow(u_matrix, cmap='gray')  # black = close = clusters
plt.colorbar()
plt.show()
