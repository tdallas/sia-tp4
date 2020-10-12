import numpy as np
import pandas as pd
from math import sqrt
import random as random
from scipy.spatial import distance
import matplotlib.pyplot as plt


def get_matrix_indexes_from_weights(index, x_length):
    row_index = (index - (index % x_length)) / x_length
    col_index = index % x_length
    return row_index, col_index


class Kohonen():
    def __init__(self, standarized_dataset, x_neurons_count, y_neurons_count, iteration_limit=250, eta=0.1, shape='R'):
        self.standarized_dataset = standarized_dataset
        self.x_neurons_count = x_neurons_count
        self.y_neurons_count = y_neurons_count
        self.iteration_limit = 50
        # self.iteration_limit = iteration_limit * \
        # self.x_neurons_count * self.y_neurons_count
        self.eta = eta
        self.weights = self.initialize_random_weights(
            len(standarized_dataset[0]))
        # We wont using this for much stuff right now
        self.shape = 'R'
        self.radius_limit = 1 if self.shape == 'R' else sqrt(2)
        # Initial radius is equal to 80% of the total neurons
        self.radius = x_neurons_count * y_neurons_count * 0.8

    def get_weights(self):
        return self.weights

    # We could also initialize weights taking random values from standarized_dataset
    def initialize_random_weights(self, component_size):
        weights = []
        current_neurons_count = 0
        while current_neurons_count < (self.x_neurons_count * self.y_neurons_count):
            weights.append(np.array(np.random.rand(component_size), dtype=float))
            current_neurons_count += 1
        return weights

    def euclidean_distance(self, vector_a, vector_b):
        return distance.euclidean(vector_a, vector_b)

    def get_node_with_min_distance(self, distances):
        return np.argmin(distances)

    # shape == 'R' --> RECTANGULAR
    # shape == 'H' --> HEXAGONAL
    def update_weights_of_neighborhood(self, min_weight_index, input):
        if self.shape == 'R':
            self.update_weights_of_neighborhood_R(min_weight_index, input)
        # else:
        #     self.update_weights_of_neighborhood_H(min_weight_index)

    # Im just updating its REALLY NEAR neighbors
    def update_weights_of_neighborhood_R(self, min_weight_index, input):
        # UP, DOWN, RIGHT, LEFT
        indexes = [min_weight_index - self.x_neurons_count,
                   min_weight_index + self.x_neurons_count,
                   min_weight_index + 1,
                   min_weight_index - 1]
        filter(lambda x: x >= 0 and x < len(self.weights), indexes)
        for index in indexes:
            self.weights[index] = self.weights[index] + \
                self.eta * (input-self.weights[index])

    def train(self):
        current_iteration = 0
        while current_iteration < self.iteration_limit:
            random_input_index = random.randint(
                0, len(self.standarized_dataset) - 1)
            random_input = self.standarized_dataset[random_input_index]

            weights_index = 0
            distances = []
            while weights_index < len(self.weights):
                distances.append(self.euclidean_distance(
                    self.weights[weights_index], random_input))
                weights_index += 1

            min_weight_index = self.get_node_with_min_distance(distances)
            self.update_weights_of_neighborhood(min_weight_index, random_input)
            print(min_weight_index)
            print(current_iteration, self.iteration_limit)
            current_iteration += 1

    def construct_nodes_map(self):
        som_map = []
        weights_index = 0
        x_index = 0
        while x_index < self.x_neurons_count:
            y_index = 0
            neurons_vector = []
            while y_index < self.y_neurons_count:
                neuron = self.weights[weights_index]
                weights_index+=1
                y_index+=1
                neurons_vector.append(neuron)
            som_map.append(neurons_vector)
            x_index+=1    
        return np.array(som_map)

    # def build_u_matrix(self):
        