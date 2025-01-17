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
    def __init__(self, standarized_dataset, k_neurons_count, iteration_limit=250, eta=0.1, shape='R'):
        self.standarized_dataset = standarized_dataset
        self.k_neurons_count = k_neurons_count
        self.iteration_limit = iteration_limit
        self.eta = eta
        self.weights = self.initialize_random_weights(
            len(standarized_dataset[0]))
        self.count_weights = np.zeros(len(self.weights))
        # We wont using this for much stuff right now
        self.shape = 'R'
        self.radius_limit = 1 if self.shape == 'R' else sqrt(2)
        # Initial radius is equal to 80% of the total neurons
        self.radius = k_neurons_count * k_neurons_count * 0.8
        self.som_map = []
        self.som_map_build = False

    def get_weights(self):
        return self.weights

    # We could also initialize weights taking random values from standarized_dataset
    def initialize_random_weights(self, component_size):
        weights = []
        current_neurons_count = 0
        while current_neurons_count < (self.k_neurons_count * self.k_neurons_count):
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
        indexes = [min_weight_index - self.k_neurons_count,
                   min_weight_index + self.k_neurons_count,
                   min_weight_index + 1,
                   min_weight_index - 1]
        indexes_filtered = filter(lambda x: x >= 0 and x < len(self.weights), indexes)
        for index in indexes_filtered:
            self.weights[index] = self.weights[index] + \
                self.eta * (input-self.weights[index])

    def calculate_avg_distance_to_neighborhood(self, current_index):
        # UP, DOWN, RIGHT, LEFT
        indexes = [current_index - self.k_neurons_count,
                   current_index + self.k_neurons_count,
                   current_index + 1,
                   current_index - 1]
        indexes_filtered = list(filter(lambda x: x >= 0 and x < len(self.weights), indexes))
        if len(indexes_filtered) == 0:
            return 0 
        avg = 0
        for index in indexes_filtered:
            avg += self.euclidean_distance(self.weights[current_index], self.weights[index])
        return avg / len(list(indexes_filtered))

    def get_count_weights(self):
        return self.count_weights

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
            self.count_weights[min_weight_index]+=1
            # print(min_weight_index, self.count_weights[min_weight_index])
            # print('going to index', min_weight_index)
            self.update_weights_of_neighborhood(min_weight_index, random_input)
            # print(min_weight_index)
            # print(current_iteration, self.iteration_limit)
            current_iteration += 1

    def construct_nodes_map(self):
        self.som_map_build = True
        self.som_map=[]
        for index in range(len(self.weights)):
            if index % self.k_neurons_count == 0:
                som_row = []
            som_row.append(self.weights[index])
            if index % self.k_neurons_count == self.k_neurons_count - 1:
                self.som_map.append(som_row)
        return self.som_map

    def build_u_matrix(self):
        u_matrix=[]
        for index in range(len(self.weights)):
            if index % self.k_neurons_count == 0:
                u_row = []
            u_row.append(self.calculate_avg_distance_to_neighborhood(index))
            if index % self.k_neurons_count == self.k_neurons_count - 1:
                u_matrix.append(u_row)
        return u_matrix

    def weight_difference(self, weight, input):
        avg = 0
        for index in range(len(weight)):
            avg += self.euclidean_distance(weight[index], input[index])
        return avg / len(weight)

    def get_best_matching(self, input):
        if not self.som_map_build:
            self.construct_nodes_map()
        best_i = 0
        best_j = 0
        best_difference = 1.7976931348623157e+308
        for i in range(self.k_neurons_count):
            for j in range(self.k_neurons_count):
                difference = self.weight_difference(self.som_map[i][j], input)
                if difference < best_difference:
                    best_difference = difference
                    best_i = i
                    best_j = j
        return best_i, best_j, best_difference