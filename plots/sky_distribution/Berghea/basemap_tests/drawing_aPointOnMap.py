"""

http://basemaptutorial.readthedocs.io/en/latest/basic_functions.html

"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='ortho', lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

## Drawing a point in a map is usually done using the plot method:

x, y = map(0, 0)
map.plot(x, y, marker='D',color='m')


plt.savefig('the_PointOnMap.png')
