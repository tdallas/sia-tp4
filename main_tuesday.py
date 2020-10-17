from data_parser import DataParser
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
from sklearn.covariance import EmpiricalCovariance
from sklearn.decomposition import PCA 

parser = DataParser('europe.csv')
# print(parser.get_numerical_csv())
# print(np.matrix(parser.get_numerical_csv()).T)

# matrix_for_correlation = np.array(parser.get_numerical_csv(), dtype=float).T
matrix_for_correlation = np.array(parser.get_standarized_matrix())

print('MEDIA (Tiene que tender a 0):', np.mean(matrix_for_correlation), '| STD (Tiene que tender a 1):', np.std(matrix_for_correlation))

# print('ESTANDARIZADA',parser.get_standarized_matrix())

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


covariance_matrix = np.cov(np.array(parser.get_numerical_csv()).T)
print('COV', covariance_matrix)

autovals_corr, autovecs_corr = np.linalg.eig(correlation_matrix)

print('AUTOVALS | AUTOVECS, COR')
print(autovals_corr, autovecs_corr)

autovals_cov, autovecs_cov = np.linalg.eig(covariance_matrix)

print('AUTOVALS | AUTOVECS, COV')
print(autovals_cov, autovecs_cov)

# PCA
n_components = 7
pca = PCA(n_components=n_components)
pca.fit(matrix_for_correlation.T)
X_new = pca.transform(matrix_for_correlation.T)

# print(X_new)
print('Cargas de las componentes')
print(pca.explained_variance_ratio_)

print('Cargas de primer componente principal')
print(pca.components_)

print('PCA', X_new)
print('PCA Ratio:', pca.explained_variance_ratio_)

sn.heatmap(correlation_matrix, annot=True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
