'''
Original code based on::
https://stackoverflow.com/questions/12951065/get-bins-coordinates-with-hexbin-in-matplotlib

My question and answers::
https://stackoverflow.com/questions/46320712/putting-matplotib-hexbin-into-an-aitoff-projection
'''

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.coordinates import SkyCoord
from astropy import units

## Path and file of some WISE W4 data
path =   '/cos_pc19a_npr/data/WISE/W4/W4SNRge3/'
filename = 'WISE_W4SNRge3_and_W4MPRO_lt_6.0_RADecl_nohdr.dat'
datafile= path+filename
data = ascii.read(datafile)

coords = SkyCoord(ra=data['ra'], dec=data['dec'], unit='degree')
ra = coords.ra.wrap_at(180 * units.deg).radian
dec = coords.dec.radian

## https://chrisalbon.com/python/set_the_color_of_a_matplotlib.html
color_map = plt.cm.Spectral_r
#color_map = plt.cm.RdYlGn
#color_map = plt.cm.Blues
#color_map = plt.cm.BrBG
#color_map = plt.cm.Greens
#color_map = plt.cm.YlOrRd
#color_map = plt.cm.spring
#color_map = plt.cm.summer
#color_map = plt.cm.autumn
#color_map = plt.cm.winter
#color_map = plt.cm.cool
#color_map = plt.cm.YlGn
#color_map = plt.cm.RdBu
#color_map = plt.cm.PuOr
#color_map = plt.cm.Oranges

fig = plt.figure(figsize=(18, 12))
fig.add_subplot(111, projection='aitoff')

## https://stackoverflow.com/questions/29368295/matplotlib-hexbin-normalize
gsize = 45 *2 * 2 * 2 
image = plt.hexbin(ra, dec, cmap=color_map, gridsize=gsize, mincnt=0, bins='log')
#image = plt.hexbin(ra, dec, cmap=color_map, gridsize=gsize, mincnt=1, bins='log')
print('\n gsize:: ', gsize, '\n')


plt.tick_params(axis='both', which='major', labelsize=16)

plt.xlabel('R.A.', fontsize=16)
plt.ylabel('Decl.', fontsize=16)

plt.grid(True)
plt.colorbar(image, spacing='uniform', extend='max')

plt.savefig("WISE_W4SNRge3_and_W4MPRO_lt_6pnt0_temp.png", transparent=True, bbox_inches='tight', pad_inches=0.2)
plt.show()
