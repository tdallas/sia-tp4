from kohonen_network import Kohonen
from parser import Parser

parser = Parser('europe.csv')

kohonen = Kohonen(parser.get_numerical_csv(), 50, 50)
kohonen.train() 

print(kohonen.get_weights())