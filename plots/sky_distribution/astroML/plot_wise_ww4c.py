# Author: Jake VanderPlas <vanderplas@astro.washington.edu>
# License: BSD
#   The figure is an example from astroML: see http://astroML.github.com
import numpy as np
from matplotlib import pyplot as plt

from astroML.datasets import fetch_nasa_atlas

path='/cos_pc19a_npr/data/WISE/W4/'
file='WISE_W4_DetBitge8_RADeclsorted.tbl'
datafile = path+file
#data = fetch_nasa_atlas()

data = ascii.read(datafile, delimiter=" ")



#------------------------------------------------------------
# plot the RA/DEC in an area-preserving projection

RA = data['RA']
DEC = data['DEC']

# convert coordinates to degrees
RA -= 180
RA *= np.pi / 180
DEC *= np.pi / 180

ax = plt.axes(projection='mollweide')
plt.scatter(RA, DEC, s=1, c=data['Z'], cmap=plt.cm.copper,
            edgecolors='none', linewidths=0)
plt.grid(True)

plt.title('NASA Atlas Galaxy Locations')
cb = plt.colorbar(cax=plt.axes([0.05, 0.1, 0.9, 0.05]),
                  orientation='horizontal',
                  ticks=np.linspace(0, 0.05, 6))
cb.set_label('redshift')

