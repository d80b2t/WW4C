"""

http://basemaptutorial.readthedocs.io/en/latest/first_map.html

"""

## The first two lines include the Basemap library and
## matplotlib. Both are necessary
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

## Changing the projection is easy, just add the projection argument
## and lat_0 and lon_0 to the Basemap contructor.
map = Basemap(projection='ortho', lat_0=0, lon_0=0)

## Even with the new projection, the map is still a bit poor, so let’s
## fill the oceans and continents with some colors The methods
## fillcontinents() and drawmapboundary() will do it:

map.drawcoastlines()

## Fill the globe with a blue color 
map.drawmapboundary(fill_color='aqua')

## Fill the continents with the land color
map.fillcontinents(color='coral',lake_color='aqua')




plt.savefig('theSecondMap_temp.png')
