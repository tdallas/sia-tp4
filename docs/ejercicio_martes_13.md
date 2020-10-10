# 1: ¿Cuántas variables tiene el conjunto de datos?¿Cuántos registros? ¿Cuáles son las variables?
El conjunto tiene 8 variables, 29 registros.
Las variables son: Country (ESTA NO ES NUMERICA), Area, GDP, Inflation, Life.expect, Military, Pop.growth, Unemployment

# 2: Realizar un gráfico boxplot de todas las variables numéricas juntas. Y lo mismo para las variables estandarizadas.

# 3: Calcular la matriz de covarianzas y la matriz de correlaciones. ¿Qué dimensión tiene cada una?
7x7, ambas, solo se usaron los valores numericos, es decir el primer vector columna se omitó
# 4: Calcular los autovalores y autovectores de las matrices. 
corr:
autovals: [3.22716568 1.18712341 1.06319053 0.45784862 0.12564189 0.16867389
 0.77035598] 
autovecs: [[ 1.24873902e-01 -1.72872202e-01  8.98296740e-01 -3.24016926e-01
  -6.66428246e-02  1.90118083e-01  4.48503976e-02]
 [-5.00505858e-01 -1.30139553e-01  8.39557607e-02  3.90632444e-01
   3.97408435e-01  6.38657073e-01 -8.42554739e-02]
 [ 4.06518155e-01 -3.69657243e-01  1.98194675e-01  6.89500539e-01
   2.26700295e-01 -3.23867263e-01  1.64685649e-01]
 [-4.82873325e-01  2.65247797e-01  2.46082460e-01 -1.01786561e-01
   5.07031305e-01 -6.06434187e-01  2.67714373e-02]
 [ 1.88111616e-01  6.58266888e-01  2.43679433e-01  3.68147581e-01
  -1.37309597e-01  3.55960680e-02 -5.62374796e-01]
 [-4.75703554e-01  8.26219831e-02  1.63697207e-01  3.47867772e-01
  -6.71146682e-01 -1.20855625e-01  3.92462767e-01]
 [ 2.71655820e-01  5.53203705e-01  5.00135736e-04  1.01587422e-02
   2.44662434e-01  2.59704965e-01  7.01967912e-01]]
cov:
autovals: [2.74071191e+10 2.06245544e+08 1.61367175e+01 5.36835095e+00
 7.77196831e-01 5.58578271e-01 5.81146240e-02]
autovecs: [[-9.99925260e-01 -1.22259664e-02 -1.15907007e-06  8.76398393e-07
  -2.55643002e-06 -4.76693481e-07 -8.23249955e-08]
 [ 1.22259664e-02 -9.99925232e-01 -1.39237702e-04  1.91123837e-04
  -2.04259624e-05  2.09914170e-05  1.77027887e-05]
 [-2.70756484e-06  4.40513295e-05  4.07576923e-02  3.47331165e-01
   9.32437955e-01  8.17542177e-02  3.96935686e-02]
 [ 4.31861069e-07 -1.56500769e-04 -1.77866306e-01 -9.16473235e-01
   3.47617660e-01 -2.32240281e-02  8.40414667e-02]
 [-4.93639942e-07  1.52277397e-05 -3.84545055e-02 -5.18473040e-02
  -6.03896767e-02  9.88353166e-01 -1.23871768e-01]
 [ 2.71135309e-07 -2.64010831e-05 -3.70396563e-02 -5.22010104e-02
   7.39244808e-02 -1.23430438e-01 -9.87523780e-01]
 [-7.34965897e-07  1.72410271e-04 -9.81759483e-01  1.84457978e-01
  -2.46917191e-02 -2.64544720e-02  2.85310608e-02]]

# 5: Realizar la transformación de Componentes principales utilizando la librería que quieran. Informar todos los resultados que devuelve el método e interpretarlos. 

# 6: Analizar la primer componente principal. ¿Cuáles son las cargas de esta componente?