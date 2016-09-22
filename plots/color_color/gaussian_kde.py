"""



"""
##
## http://stackoverflow.com/questions/20105364/how-can-i-make-a-scatter-plot-colored-by-density-in-matplotlib
##
# Calculate the point density
xy = np.vstack([ra,dec])

## This next line just kills everything... :-/
z = gaussian_kde(xy)(xy)

# Sort the points by density, so that the densest points are plotted last
#idx = z.argsort()
#x, y, z = x[idx], y[idx], z[idx]
