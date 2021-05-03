import geopandas as gpd
import matplotlib.pyplot as plt

# Importing an ESRI Shapefile and plotting it using GeoPandas
districts = gpd.read_file(r'C:\Users\josecal\Documents\Python\Introduction to Geopandas\Introduction to Geopandas\Introduction to GeoPandas\Shapefiles\districts.shp')
#districts.plot(cmap = 'hsv', edgecolor = 'black', column = 'district')
#districts.plot(color='red',edgecolor = 'blue')
#districts.plot(cmap = 'winter', edgecolor = 'black', column = 'district')

#area_of_interest = gpd.read_file(r'C:\Users\josecal\Documents\Python\Introduction to Geopandas\Introduction to Geopandas\Introduction to GeoPandas\Shapefiles\area_of_interest.shp')
#area_of_interest.plot()

#atms = gpd.read_file(r'C:\Users\josecal\Documents\Python\Introduction to Geopandas\Introduction to Geopandas\Introduction to GeoPandas\Shapefiles\atms.shp')
#atms.plot()

# # Plot the figures side by side 
#fig, (ax1, ax2) = plt.subplots(nrows= 2, figsize=(10,8))
#districts.plot(ax = ax1, cmap = 'hsv', edgecolor = 'black', column = 'district')
#area_of_interest.plot(ax = ax2, color = 'green')

# # Plotting multiple layers
#fig, ax = plt.subplots(figsize = (10,8))
#districts.plot(ax = ax, cmap = 'hsv', edgecolor = 'black', column = 'district')
#area_of_interest.plot(ax = ax, color = 'none', edgecolor = 'black')
#atms.plot(ax = ax, color = 'black', markersize = 14)

# Reprojecting GeoPandas GeoDataFrames
#fig, ax = plt.subplots(figsize = (8,6))
#districts = districts.to_crs(epsg = 32629)
#districts.plot(ax = ax, cmap = 'hsv', edgecolor = 'black', column = 'district')
#area_of_interest = area_of_interest.to_crs(epsg = 32629)
#area_of_interest.plot(ax = ax, color = 'none', edgecolor = 'black')

# Intersecting Layers
#districts_in_aoi = gpd.overlay(districts, area_of_interest, how = 'intersection')
#districts_in_aoi.plot(edgecolor = 'red')

# Calculating the areas of the intersected layer 
#districts_in_aoi['area'] = districts_in_aoi.area/1000000

# Exporting GeoPandas GeoDataFrames into an ESRI Shapefile
#districts_in_aoi.to_file('districts_within_aoi.shp', driver = "ESRI Shapefile")



















