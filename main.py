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

# Display both shapefiles together
fig, ax = plt.subplots(1)
cities.plot(ax=ax, cmap = 'rainbow', column = 'NAME_4')
AOI.plot(ax=ax, facecolor = 'yellow')
plt.title('Belgian Cities with AOI Plot')
plt.show()

# Intersecting
cities_in_AOI = gpd.overlay(cities, AOI, how = 'intersection')
cities_in_AOI.plot(figsize = (10,10),cmap='jet')
# Assigning a new column - Area
cities_in_AOI['Area(km2)'] = cities_in_AOI.area/1000000

plt.title('Intersected Cities within Area of Interest (AOI)')
plt.show()

# Save the geodataframe to a .shp (Shapefile)
cities_in_AOI.to_file('./Shapefiles/intersected_cities.shp')