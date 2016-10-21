# example showing how to plot scattered data with hexbin.
from numpy.random import uniform
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

# create north polar stereographic basemap
m = Basemap(lon_0=270, boundinglat=20, projection='npstere',round=True)
#m = Basemap(lon_0=-105,lat_0=40,projection='ortho')

# number of points, bins to plot.
npts = 50000
bins = 30

# generate random points on a sphere,
# so that every small area on the sphere is expected
# to have the same number of points.
# http://mathworld.wolfram.com/SpherePointPicking.html
u = uniform(0.,1.,size=npts)
v = uniform(0.,1.,size=npts)
lons = 360.*u
lats = (180./np.pi)*np.arccos(2*v-1) - 90.
# toss points outside of map region.
lats = np.compress(lats > 20, lats)
lons = np.compress(lats > 20, lons)
# convert to map projection coordinates.
x1, y1 = m(lons, lats)
# remove points outside projection limb.
x = np.compress(np.logical_or(x1 < 1.e20,y1 < 1.e20), x1)
y = np.compress(np.logical_or(x1 < 1.e20,y1 < 1.e20), y1)
# function to plot at those points.
xscaled = 4.*(x-0.5*(m.xmax-m.xmin))/m.xmax
yscaled = 4.*(y-0.5*(m.ymax-m.ymin))/m.ymax
z = xscaled*np.exp(-xscaled**2-yscaled**2)


# make plot using hexbin
fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(122)
CS = m.hexbin(x,y,C=z,gridsize=bins,cmap=plt.cm.jet)
# draw coastlines, lat/lon lines.
m.drawcoastlines()
m.drawparallels(np.arange(0,81,20))
m.drawmeridians(np.arange(-180,181,60))
m.colorbar(location="bottom",label="Z") # draw colorbar
plt.title('hexbin', fontsize=20)


# use histogram2d instead of hexbin.
ax = fig.add_subplot(121)

# remove points outside projection limb.
bincount, xedges, yedges = np.histogram2d(x, y, bins=bins)
mask = bincount == 0

# reset zero values to one to avoid divide-by-zero
bincount = np.where(bincount == 0, 1, bincount)
H, xedges, yedges = np.histogram2d(x, y, bins=bins, weights=z)
H = np.ma.masked_where(mask, H/bincount)

# set color of masked values to axes background (hexbin does this by default)
palette = plt.cm.jet
palette.set_bad(ax.get_axis_bgcolor(), 1.0)
CS = m.pcolormesh(xedges,yedges,H.T,shading='flat',cmap=palette)

# draw coastlines, lat/lon lines.
m.drawcoastlines()
m.drawparallels(np.arange(0,81,20))
m.drawmeridians(np.arange(-180,181,60))

m.colorbar(location="bottom",label="Z") # draw colorbar
plt.title('histogram2d', fontsize=20)

plt.gcf().set_size_inches(18,10)
plt.show()
