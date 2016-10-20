

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

from astropy.io import ascii

## http://matplotlib.org/basemap/users/examples.html

map = Basemap(projection='ortho',lat_0=0,lon_0=0,resolution='l')
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,10))




path = '/cos_pc19a_npr/data/WISE/W4/WISE_W4_W4SNRge3_W4MPROlt4.0_nohdr.tbl'

cols = ['designation', 'ra', 'dec', 'sigra', 'sigdec', 'w1mpro', 'w1sigmpro', 'w1snr', 'w2mpro', 'w2sigmpro', 'w2snr', 'w3mpro', 'w3sigmpro', 'w3snr', 'w4mpro', 'w4sigmpro', 'w4snr', 'w4rchi2']

tbl = ascii.read(path)

ra = tbl['ra']
dec = tbl['dec']


#x, y = map(wiseagn.ra, wiseagn.dec)
x, y = map(ra, dec)

crap = map.scatter(x,y, 10, marker='o', color='k')

plt.show()
