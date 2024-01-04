import geopandas as gpd 
import matplotlib.pyplot as plt

# Importing and plotting the cities shapefile 
cities = gpd.read_file('./Shapefiles/belgian_cities.shp')
cities.plot()
plt.title('Default Cities Shapefile Plot')
plt.show()

cities.plot(cmap='jet', column='NAME_4', figsize=(15, 15))
plt.title('Cities Shapefile Plot with Custom Styling')
plt.show()