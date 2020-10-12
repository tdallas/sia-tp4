from kohonen_network import Kohonen
from parser import Parser
import seaborn as sn
import matplotlib.pyplot as plt

parser = Parser('europe.csv')

kohonen = Kohonen(parser.get_numerical_csv(), 50, 50)
kohonen.train() 

print(kohonen.get_weights())

kohonen.displayClusters(parser.get_numerical_csv())
