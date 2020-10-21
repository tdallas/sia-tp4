import numpy as np

class Oja():
    def __init__(self, standarized_dataset, iteration_limit=2500, eta=0.0001):
        self.standarized_dataset = standarized_dataset
        self.eta = eta
        self.weights = np.array(np.random.rand(len(standarized_dataset[0])), dtype=float)
        self.iteration_limit = iteration_limit

    def train(self):
        iterations = []
        weights_on_iteration = []
        for iteration in range(self.iteration_limit):
            for x in self.standarized_dataset:
                y = 0.0
                for j in range(len(x)):
                    y += self.weights[j] * x[j]
                for j in range(len(x)):
                    self.weights[j] += self.eta * (y * x[j] - y * y * self.weights[j])
            iterations.append(iteration)
            weights_on_iteration.append(self.weights.copy())
        return weights_on_iteration, iterations
    
    def get_weights(self):
        return self.weights