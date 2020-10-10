from parser import Parser
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
from sklearn.covariance import EmpiricalCovariance
from sklearn.decomposition import PCA 

parser = Parser('europe.csv')
# print(parser.get_numerical_csv())
# print(np.matrix(parser.get_numerical_csv()).T)

matrix_for_correlation = np.array(parser.get_numerical_csv(), dtype=float).T

# 'Area','GDP','Inflation','Life.expect','Military','Pop.growth','Unemployment'
matrix_for_correlation_with_keys = {
    'Area': matrix_for_correlation[0],
    'GDP': matrix_for_correlation[1],
    'Inflation': matrix_for_correlation[2],
    'Life.expect': matrix_for_correlation[3],
    'Military': matrix_for_correlation[4],
    'Pop.growth': matrix_for_correlation[5],
    'Unemployment': matrix_for_correlation[6]
}

df = pd.DataFrame(matrix_for_correlation_with_keys, columns=[
                  'Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment'])

correlation_matrix = df.corr()
# If you want to show heatmap:
# sn.heatmap(correlation_matrix, annot=True)
# plt.show()

covariance_matrix = np.cov(matrix_for_correlation)

autovals_corr, autovecs_corr = np.linalg.eig(correlation_matrix)
autovals_cov, autovecs_cov = np.linalg.eig(covariance_matrix)

# PCA
n_components = 3
pca = PCA(n_components=n_components)
pca.fit(matrix_for_correlation)
print('prev', matrix_for_correlation)
X_new = pca.transform(matrix_for_correlation)

print(X_new)