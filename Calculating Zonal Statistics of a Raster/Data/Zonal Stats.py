import geopandas as gpd
import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist
import rasterstats
import matplotlib.pyplot as plt
import pandas as pd

# Read the districts shapefile 
districts = gpd.read_file(r'districts.shp')

# Read the rainfall raster of 2020-04-15
rf = rasterio.open(r'2020-4-15.tif', mode = 'r')
show(rf)

# Plotting the raster and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rf, ax = ax1, title = 'Rainfall')
districts.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow')
show_hist(rf, title = 'Histogram', ax = ax2)
plt.show()
type(rf)

# Assign raster values to a numpy nd array
rainfall_array = rf.read(1)
rf.meta
affine = rf.transform

# Calculating the zonal statistics 
avg_rf  = rasterstats.zonal_stats(districts, rainfall_array, affine = affine,
                                      stats = ['mean'], 
                                      geojson_out = True)
type(avg_rf)
# Extracting the average rainfall data from the list
avg_rainfall = []
i = 0

while i < len(avg_rf):
    avg_rainfall.append(avg_rf[i]['properties'])
    i = i + 1 

# Transfering the infromation from the list to a pandas DataFrame

avg_rf_portugal = pd.DataFrame(avg_rainfall)
print(avg_rf_portugal)

avg_rf_portugal.plot(x='NAME_1', y ='mean', kind = 'bar', title = 'Average Rainfall on 2020 April 15')










