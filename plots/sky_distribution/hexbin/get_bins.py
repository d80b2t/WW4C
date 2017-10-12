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
data = ascii.read(datafile)  

color_map = plt.cm.Spectral_r
points = np.array([data['ra'], data['dec']])

xbnds = np.array([  0.0,360.0])
ybnds = np.array([-90.0,90.0])
extent = [xbnds[0],xbnds[1],ybnds[0],ybnds[1]]

#fig=plt.figure(figsize=(10,9))
fig = plt.figure(figsize=(6, 4), dpi=200, facecolor='w', edgecolor='k')
#plt.subplot(111, projection="aitoff")

ax = fig.add_subplot(111)
##x, y = points.T  # if from generate_data(n)
x, y = points     # if Ra,dec

# Set gridsize just to make them visually large
gsize = 45 #*2 * 2 * 2
image = plt.hexbin(x,y,cmap=color_map,
    gridsize=gsize,extent=extent,mincnt=1,bins='log')
# Note that mincnt=1 adds 1 to each count

counts = image.get_array()
ncnts = np.count_nonzero(np.power(10,counts))
verts = image.get_offsets()
## This puts those "frog's egg" type dots on the plot (yuck!) 
#for offc in range(verts.shape[0]):
#    binx,biny = verts[offc][0],verts[offc][1]
 #   if counts[offc]:
  #      plt.plot(binx,biny,'k.',zorder=100)

ax.set_xlim(xbnds)
ax.set_ylim(ybnds)
plt.xlabel('Right Ascension (J2000) / deg')
plt.ylabel(r'Declination (J2000) / deg')

plt.grid(True)
cb = plt.colorbar(image, spacing='uniform', extend='max')
#plt.show()

#plt.savefig("WISE_W4SNRge3_and_W4MPRO_lt_6pnt0_temp.svg", transparent=True, bbox_inches='tight', pad_inches=0)
plt.savefig("WISE_W4SNRge3_and_W4MPRO_lt_6pnt0_temp.png", transparent=True, bbox_inches='tight', pad_inches=0)
plt.savefig("WISE_W4SNRge3_and_W4MPRO_lt_6pnt0_temp.pdf", dpi=400, transparent=True, bbox_inches='tight', pad_inches=0)
plt.show()

