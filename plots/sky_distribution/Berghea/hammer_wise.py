"""

http://matplotlib.org/basemap/users/hammer.html

"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

from astropy.io import ascii


# lon_0 is central longitude of projection.
# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='hammer',lon_0=0,resolution='c')

# draw parallels and meridians.
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,420.,60.))



path = '/cos_pc19a_npr/data/WISE/W4/WISE_W4_W4SNRge3_W4MPROlt4.0_nohdr.tbl'

cols = ['designation', 'ra', 'dec', 'sigra', 'sigdec', 'w1mpro', 'w1sigmpro', 'w1snr', 'w2mpro', 'w2sigmpro', 'w2snr', 'w3mpro', 'w3sigmpro', 'w3snr', 'w4mpro', 'w4sigmpro', 'w4snr', 'w4rchi2']

tbl = ascii.read(path)

ra = tbl['ra']
dec = tbl['dec']


x, y = m(ra, dec)
crap = m.scatter(x,y, 10, marker='o', color='k')


plt.title("Hammer Projection")
plt.show()
