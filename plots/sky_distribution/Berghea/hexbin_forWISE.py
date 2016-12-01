

import numpy as np
from numpy.random import uniform

from astropy.io import ascii

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


m = Basemap(projection='hammer', lon_0=0, resolution='c')


path = '/cos_pc19a_npr/data/WISE/W4/WISE_W4_W4SNRge3_W4MPROlt4.0_nohdr.tbl'
cols = ['designation', 'ra', 'dec', 'sigra', 'sigdec', 'w1mpro', 'w1sigmpro', 'w1snr', 'w2mpro', 'w2sigmpro', 'w2snr', 'w3mpro', 'w3sigmpro', 'w3snr', 'w4mpro', 'w4sigmpro', 'w4snr', 'w4rchi2']
tbl = ascii.read(path)

ra = tbl['ra']
dec = tbl['dec']

"""
In [11]: ra.m
ra.max   ra.mean  ra.meta  ra.min   ra.more  

In [11]: ra.min
Out[11]: <function Column.min>

In [12]: print(ra.min)
<built-in method min of Column object at 0x10ae41ac8>

In [13]: print(ra.min())
0.0019758
"""


x = ra
y = dec

xmin = x.min()
xmax = x.max()
ymin = y.min()
ymax = y.max()

plt.title("376857 points with WISE W4<4.0 mag")
plt.subplots_adjust(hspace=0.5)

plt.subplot(121)
plt.hexbin(x, y, cmap=plt.cm.YlOrRd_r)
plt.axis([xmin, xmax, ymin, ymax])
plt.title("Hexagon binning")
cb = plt.colorbar()
cb.set_label('counts')

plt.subplot(122)
plt.hexbin(x, y, bins='log', cmap=plt.cm.YlOrRd_r)
plt.axis([xmin, xmax, ymin, ymax])
cb = plt.colorbar()
cb.set_label('log10(N)')


#plt.show()
#plt.savefig('hexbin_forWISE_temp.png')

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('hexbin_forWISE_temp.png', dpi=100)
