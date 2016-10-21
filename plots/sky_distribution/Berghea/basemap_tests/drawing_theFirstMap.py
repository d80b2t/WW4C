"""

http://basemaptutorial.readthedocs.io/en/latest/first_map.html

"""


## The first two lines include the Basemap library and
## matplotlib. Both are necessary
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


## The map is created using the Basemap class, which has many
## options. Without passing any option, the map has the Plate Carrée
## projection centered at longitude and latitude = 0
map = Basemap()


## After setting the map, we can draw what we want. In this case, the
## coast lines layer, which comes already with the library, using the
## method drawcoastlines()
map.drawcoastlines()


## Finally, the map has to be shown or saved. The methods from
## mathplotlib are used. In this example, plt.show() opens a window to
## explore the result. plt.savefig(‘file_name’) would save the map
## into an image.

#plt.show()
plt.savefig('test.png')
