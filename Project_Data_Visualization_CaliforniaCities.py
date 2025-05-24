import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.available
plt.style.use('fivethirtyeight')
cities = pd.read_csv("D:\Searchalgorithms_AI\california_cities.csv")

#Extract Latd = Vi do and Longd = Kinh do
lat, long = cities['latd'], cities['longd']
population, area = cities['population_total'], cities['area_total_km2']
plt.figure(figsize=(8,6))
#Plot using Pyplot API
plt.scatter(long, lat, c = np.log10(population), cmap = 'viridis', s = area, linewidths=0, alpha = 0.5)
plt.axis('equal')
plt.xlabel('longtitude')
plt.ylabel('lattitude')
plt.colorbar(label = 'log$_{10}$(population)')
plt.clim(3, 7)
plt.title("California Cities : Population and Area Distribution")
# Create a legend for cities'sizes
area_range = [50, 100, 300, 500]
for area in area_range :
    plt.scatter([],[],s=area, c='k', alpha=0.4,
                label=str(area) + 'km$^2$')
plt.legend(scatterpoints = 1, labelspacing = 1, title = 'City Area')

plt.show()
