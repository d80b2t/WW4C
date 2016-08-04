"""
https://healpy.readthedocs.io/en/latest/tutorial.html

Healpy tutorial
Creating and manipulating maps
Maps are simply numpy arrays, where each array element refers to a location in the sky as defined by the Healpix pixelization schemes (see the healpix website).

Note: Running the code below in a regular Python session will not display the maps; it’s recommended to use IPython:

$ ipython
...then select the appropriate backend display:

>>> %matplotlib inline # for IPython notebook
>>> %matplotlib qt     # using Qt (e.g. Windows)
>>> %matplotlib osx    
"""

matplotlib osx

import numpy as np
import healpy as hp

# The resolution of the map is defined by the NSIDE parameter. 
NSIDE = int(32)


# The nside2npix() function gives the number of pixel NPIX of the map:
m = np.arange(hp.nside2npix(NSIDE))

# Healpix supports two different ordering schemes, RING or NESTED.  By
# default, healpy maps are in RING ordering.
hp.mollview(m, title="Mollview image RING")

# In order to work with NESTED ordering, all map related functions
# support the nest keyword, for example:
hp.mollview(m, nest=True, title="Mollview image NESTED")


##
##  READING AND WRITING MAPS TO FILE:
##
# Maps are read with the read_map() function:
# wmap_map_I = hp.read_map('../healpy/test/data/wmap_band_imap_r9_7yr_W_v4.fits')
wmap_map_I = hp.read_map('wmap_band_imap_r9_7yr_W_v4.fits')


# By default, input maps are converted to RING ordering, if they are in NESTED ordering. You can otherwise specify nest=True to retrieve a map is NESTED ordering, or nest=None to keep the ordering unchanged.

# By default, read_map() loads the first column, for reading other columns you can specify the field keyword.

# write_map() writes a map to disk in FITS format, if the input map is a list of 3 maps, they are written to a single file as I,Q,U polarization components:
hp.write_map("my_map.fits", wmap_map_I)


##
##  V I S U A L I Z A T I O N
## 
# Mollweide projection with mollview() is the most common visualization tool for HEALPIX maps. It also supports coordinate transformation:

hp.mollview(wmap_map_I, coord=['G','E'], title='Histogram equalized Ecliptic', unit='mK', norm='hist', min=-1,max=1, xsize=2000)

## coord does galactic to ecliptic coordinate transformation, norm=’hist’ sets a histogram equalized color scale and xsize increases the size of the image. graticule() adds meridians and parallels.
hp.graticule()

# gnomview() instead provides gnomonic projection around a position specified by rot:
hp.gnomview(wmap_map_I, rot=[0,0.3], title='GnomView', unit='mK', format='%.2g')

# mollzoom() is a powerful tool for interactive inspection of a map, it provides a mollweide projection where you can click to set the center of the adjacent gnomview panel.

