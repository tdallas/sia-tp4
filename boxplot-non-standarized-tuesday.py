from data_parser import DataParser
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

parser = DataParser('europe.csv')

matrix_non_standarized = parser.get_numerical_csv()
data_non_standarized = []
data_non_standarized.extend(matrix_non_standarized[0])
data_non_standarized.extend(matrix_non_standarized[1])
data_non_standarized.extend(matrix_non_standarized[2])
data_non_standarized.extend(matrix_non_standarized[3])
data_non_standarized.extend(matrix_non_standarized[4])
data_non_standarized.extend(matrix_non_standarized[5])
data_non_standarized.extend(matrix_non_standarized[6])

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

## Custom x-axis labels
ax.set_xticklabels(['Variables no estandarizadas'])

## add patch_artist=True option to ax.boxplot() 
## to get fill color
bp = ax.boxplot(data_non_standarized, patch_artist=True)

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

plt.tight_layout()
plt.show()