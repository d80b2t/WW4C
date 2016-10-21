"""

http://www.uvm.edu/~jbagrow/dsv/heatmap_basemap.html


"""


import csv
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


# load earthquake epicenters:
# http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.csv
lats, lons = [], []
with open('earthquake_data.csv') as f:
    reader = csv.reader(f)
    next(reader) # Ignore the header row.
    for row in reader:
        lat = float(row[1])
        lon = float(row[2])
        # filter lat,lons to (approximate) map view:
        if -130 <= lon <= -100 and 25 <= lat <= 55:
            lats.append( lat )
            lons.append( lon )


# Use orthographic projection centered on California with corners
# defined by number of meters from center position:
m  = Basemap(projection='ortho',lon_0=-119,lat_0=37,resolution='l',\
             llcrnrx=-1000*1000,llcrnry=-1000*1000,
             urcrnrx=+1150*1000,urcrnry=+1700*1000)
m.drawcoastlines()
m.drawcountries()
m.drawstates()
 

    
# ######################################################################
# bin the epicenters (adapted from 
# http://stackoverflow.com/questions/11507575/basemap-and-density-plots)

# compute appropriate bins to chop up the data:
db = 1 # bin padding
lon_bins = np.linspace(min(lons)-db, max(lons)+db, 10+1) # 10 bins
lat_bins = np.linspace(min(lats)-db, max(lats)+db, 13+1) # 13 bins
    
density, _, _ = np.histogram2d(lats, lons, [lat_bins, lon_bins])

# Turn the lon/lat of the bins into 2 dimensional arrays ready
# for conversion into projected coordinates
lon_bins_2d, lat_bins_2d = np.meshgrid(lon_bins, lat_bins)

# convert the bin mesh to map coordinates:
xs, ys = m(lon_bins_2d, lat_bins_2d) # will be plotted using pcolormesh
# ######################################################################



# define custom colormap, white -> nicered, #E6072A = RGB(0.9,0.03,0.16)
cdict = {'red':  ( (0.0,  1.0,  1.0),
                   (1.0,  0.9,  1.0) ),
         'green':( (0.0,  1.0,  1.0),
                   (1.0,  0.03, 0.0) ),
         'blue': ( (0.0,  1.0,  1.0),
                   (1.0,  0.16, 0.0) ) }
custom_map = LinearSegmentedColormap('custom_map', cdict)
plt.register_cmap(cmap=custom_map)


# add histogram squares and a corresponding colorbar to the map:
plt.pcolormesh(xs, ys, density, cmap="custom_map")

cbar = plt.colorbar(orientation='horizontal', shrink=0.625, aspect=20, fraction=0.2,pad=0.02)
cbar.set_label('Number of earthquakes',size=18)
#plt.clim([0,100])


# translucent blue scatter plot of epicenters above histogram:    
x,y = m(lons, lats)
m.plot(x, y, 'o', markersize=5,zorder=6, markerfacecolor='#424FA4',markeredgecolor="none", alpha=0.33)
 
    
# http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.drawmapscale
m.drawmapscale(-119-6, 37-7.2, -119-6, 37-7.2, 500, barstyle='fancy', yoffset=20000)
    
    
# make image bigger:
plt.gcf().set_size_inches(15,15)

plt.show()
