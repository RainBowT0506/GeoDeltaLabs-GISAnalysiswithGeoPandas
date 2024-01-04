import geopandas as gpd 
import matplotlib.pyplot as plt

# Importing and plotting the cities shapefile 
cities = gpd.read_file('./Shapefiles/belgian_cities.shp')
cities.plot()
plt.title('Belgian Cities Plot - Default')
plt.show()

cities.plot(cmap='jet')
plt.title('Belgian Cities Plot - Colormap (jet)')
plt.show()


cities.plot(cmap='jet', column='NAME_4', figsize=(10, 10))
plt.title('Belgian Cities Plot - Column (NAME_4) and Colormap (jet)')
plt.show()

# Importing and plotting AOI shapefile
AOI = gpd.read_file('./Shapefiles/area_of_interest_.shp')
AOI.plot()
plt.show()