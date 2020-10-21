import pandas as pd
import numpy as np
from country import Country


def get_standar_deviation(array):
    return np.std(array)

def get_average(array):
    return np.average(array)


class DataParser():
    def __init__(self, csv_path):
        self.covid = self.parse_csv(csv_path)

    def parse_csv(self, csv_path):
        return pd.read_csv(csv_path).values

    def get_csv(self):
        return self.covid

    def get_standarized_matrix(self):
        numerical_matrix = np.array(self.covid, dtype=float)
        standarized_matrix = []
        for row in numerical_matrix:
            average_row = get_average(row)
            standard_deviation = get_standar_deviation(row)

            standarized_row = list(map(lambda x : (x - average_row) / standard_deviation, row))
            standarized_matrix.append(standarized_row)
        return standarized_matrix
