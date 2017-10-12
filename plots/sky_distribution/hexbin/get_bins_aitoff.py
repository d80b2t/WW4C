'''
Original code based on::
https://stackoverflow.com/questions/12951065/get-bins-coordinates-with-hexbin-in-matplotlib

'''

import numpy as np
import math
import matplotlib.pyplot as plt
from astropy.io import ascii

## Path and file of some WISE W4 data
path =   '/cos_pc19a_npr/data/WISE/W4/W4SNRge3/'
filename = 'WISE_W4SNRge3_and_W4MPRO_lt_6.0_RADecl_nohdr.dat'
datafile= path+filename
wise = ascii.read(datafile)  
#points = np.array([data['ra'], data['dec']])

ra = np.linspace(-np.pi/2.,np.pi/2.,1000)
dec = np.sin(ra)*np.pi/2./2.
points = np.array([ra, dec]) 

fig = plt.figure(figsize=(6, 4), dpi=200, facecolor='w', edgecolor='k')
plt.subplot(111, projection="aitoff")

color_map = plt.cm.Spectral_r
x, y = points     
gsize = 45 #*2 * 2 * 2
image = plt.hexbin(x,y,cmap=color_map,
                   gridsize=gsize,mincnt=1,bins='log')

plt.xlabel('Right Ascension (J2000) / deg')
plt.ylabel(r'Declination (J2000) / deg')
plt.grid(True)
cb = plt.colorbar(image, spacing='uniform', extend='max')
plt.show()


