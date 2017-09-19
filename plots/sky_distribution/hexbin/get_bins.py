
import numpy as np
import math
import matplotlib.pyplot as plt
from astropy.io import ascii

def generate_data(n):
    """Make random, correlated x & y arrays"""
    points = np.random.multivariate_normal(mean=(0,0),
        cov=[[0.4,9],[9,10]],size=int(n))
    return points

if __name__ =='__main__':

    ## Path and file of some WISE W4 data
    path =   '/cos_pc19a_npr/data/WISE/W4/W4SNRge3/'
    filename = 'WISE_W4SNRge3_and_W4MPRO_lt_6.0_RADecl_nohdr.dat'
    datafile= path+filename
    data = ascii.read(datafile)  

    color_map = plt.cm.Spectral_r
    n = 1e4
    #points = generate_data(n)
    points = np.array([data['ra'], data['dec']])

    #xbnds = np.array([-20.0,20.0])
    #ybnds = np.array([-20.0,20.0])
    xbnds = np.array([  0.0,360.0])
    ybnds = np.array([-90.0,90.0])
    extent = [xbnds[0],xbnds[1],ybnds[0],ybnds[1]]

    fig=plt.figure(figsize=(10,9))
    ax = fig.add_subplot(111)
    #x, y = points.T  # if from generate_data(n)
    x, y = points     # if Ra,dec
    # Set gridsize just to make them visually large
    gsize = 90
    image = plt.hexbin(x,y,cmap=color_map,
                       gridsize=gsize,extent=extent,mincnt=1,bins='log')
    # Note that mincnt=1 adds 1 to each count
    counts = image.get_array()
    ncnts = np.count_nonzero(np.power(10,counts))
    verts = image.get_offsets()
    #for offc in range(verts.shape[0]):
     #   binx,biny = verts[offc][0],verts[offc][1]
        #if counts[offc]:
            #plt.plot(binx,biny,'k.',zorder=100)
    ax.set_xlim(xbnds)
    ax.set_ylim(ybnds)
    plt.grid(True)
    cb = plt.colorbar(image,spacing='uniform',extend='max')
    plt.show()
