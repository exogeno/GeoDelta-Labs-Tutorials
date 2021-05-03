import geopandas as gpd 
import matplotlib.pyplot as plt 
import pandas as pd
from shapely.geometry import Point

SA1 = gpd.read_file(r'C:\Users\josecal\Documents\Python\10 GeoPandas Applications\10 GeoPandas Applications\10 Applications of GeoPandas\Study_Area_1.shp')
SA2 = gpd.read_file(r'C:\Users\josecal\Documents\Python\10 GeoPandas Applications\10 GeoPandas Applications\10 Applications of GeoPandas\Study_Area_2.shp')
river = gpd.read_file(r'C:\Users\josecal\Documents\Python\10 GeoPandas Applications\10 GeoPandas Applications\10 Applications of GeoPandas\river.shp')

fig, ax = plt.subplots()
SA1.plot(ax=ax, color='blue', edgecolor='black')
SA2.plot(ax=ax, color='none', edgecolor='black')
river.plot(ax=ax)

#1 Intersection of Polygons
intersection = gpd.overlay(SA1, SA2, how = 'intersection')
intersection.plot()

#Union of Polygons
union = gpd.overlay(SA1, SA2, how = 'union')
union.plot()

#Symmetric Difference of Polygons
sd = gpd.overlay(SA1, SA2, how = 'symmetric_difference')
sd.plot()

#Difference of Polygons
difference = gpd.overlay(SA1, SA2, how = 'difference')
difference.plot()

difference2 = gpd.overlay(SA2, SA1, how = 'difference')
difference2.plot()

#Dissolve
union = gpd.overlay(SA1, SA2, how = 'union')
union.plot()
union['common_column']=1
dissolve_sa=union.dissolve(by='common_column')
dissolve_sa.plot()

##Buffer
river.crs
#Reprojecting the river GeoPandas GeoDataFrame into a Projected CRS
river_projected = river.to_crs(epsg=24547)
river.plot()
river_projected.plot()
type(river_projected)
type(river_projected['geometry'])
buffer_500m=river_projected['geometry'].buffer(distance=500)
buffer_500m.plot(figsize=(7,7))

#Obtain the centroid
union = gpd.overlay(SA1, SA2, how = 'union')
union.plot(edgecolor='black')
centroid = union['geometry'].centroid
centroid.plot()

fig1, ax1 = plt.subplots()
union.plot(ax=ax1, color='blue', edgecolor='black')
centroid.plot(ax=ax1, color='black')

airports_data = pd.read_csv('us_airports.csv')
airports_data.head(10)
airports_data.columns
geometry = [Point(xy) for xy in zip (airports_data['LONGITUDE'],airports_data['LATITUDE'])]

type(geometry)
geometry

# Importing the states ESRI Shapefile of the USA 
us_states = gpd.read_file('us_states.shp')
us_states.plot()
us_states.crs

airports_us = gpd.GeoDataFrame(airports_data, geometry = geometry, crs = us_states.crs)
airports_us.plot()

state_names_codes = pd.read_csv('state names and codes.csv')

#Renaming the column heading
airports_us.rename(columns = {"STATE":"state_code"}, inplace = True)

#Join attributes
airports_us = airports_us.merge(state_names_codes, on = 'state_code')

# Spatial Join
airports_us = airports_us[['AIRPORT', 'geometry']]

fig, ax = plt.subplots(figsize = (8,8))
us_states.plot(ax = ax, color = 'blue', edgecolor = 'black')
airports_us.plot(ax=ax, markersize = 2, color = 'green')

airports_us = gpd.sjoin(airports_us, us_states, how  = 'inner', op = 'intersects')









