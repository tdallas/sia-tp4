import pandas as pd
from country import Country

class Parser():
    def __init__(self, csv_path):
        self.europe = self.parse_csv(csv_path)

    def parse_csv(self, csv_path):
        return pd.read_csv(csv_path).values

    def parse_as_class(self):
        return list(map(self.europe))

    def get_numerical_csv(self):
        return list(map(lambda value: value[1:], self.europe))

    def get_csv(self):
        return self.europe
