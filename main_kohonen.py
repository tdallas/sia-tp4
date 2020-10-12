from kohonen_network import Kohonen
from data_parser import DataParser
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

parser = DataParser('europe.csv')

kohonen = Kohonen(parser.get_numerical_csv(), 50, 50)
kohonen.train() 

def all_zeros(array):
    len(list(filter(lambda x: x == 0, array))) == 0

# print(kohonen.get_weights())

# print(len(list(filter(lambda x : x > 0, kohonen.get_count_weights()))))

print('TAMAÑOSQUI', len(list(filter(lambda x : not all_zeros(x), kohonen.build_u_matrix()))))

print(kohonen.build_u_matrix())
# kohonen.displayClusters(parser.get_numerical_csv())
