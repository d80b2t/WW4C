#!/usr/bin/env
"""

"""

from __future__ import division
from numpy.random import randn
from pandas import DataFrame, Series
from scipy.stats import gaussian_kde

import os
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


path = '/cos_pc19a_npr/data/WISE/W4/WISE_W4_W4SNRge3_W4MPROlt4.0_nohdr.tbl'


cols = ['designation', 'ra', 'dec', 'sigra', 'sigdec', 'w1mpro', 'w1sigmpro', 'w1snr', 'w2mpro', 'w2sigmpro', 'w2snr', 'w3mpro', 'w3sigmpro', 'w3snr', 'w4mpro', 'w4sigmpro', 'w4snr', 'w4rchi2']

## If using a file *WITH* a header
# df = pd.read_table(data_in, header=54) 

## "Trick" is to use the  delimiter='\s+'  option
data = pd.read_table(path, delimiter='\s+')

## Could do just this...
ra = data['ra']
dec = data['dec']

w1mpro = data['w1mpro']
w2mpro = data['w2mpro']
w3mpro = data['w3mpro']
w4mpro = data['w4mpro']

w1snr = data['w1snr']
w2snr = data['w2snr']
w3snr = data['w3snr']
w4snr = data['w4snr']
## ... and then plot from there, or,

#fig, ax = plt.subplots()
#ax.scatter(ra, dec, edgecolor='')
plt.scatter(ra, dec, edgecolor='', label='WISE w4')
plt.show()
plt.xlabel('Right Ascension (J2000)')
plt.ylabel('Declination (J2000)')


## Will do this...
# df = pd.DataFrame(data, columns=['ra', 'dec'])
## or better yer..
df = pd.DataFrame(data, columns=cols)



## Now we're getting into it... ;-)

##
##  gridsize  controls the number of hexagons in the x-direction
##
df.plot.hexbin(x='ra', y='dec', gridsize=25)
#df.plot.hexbin(x='ra', y='dec', C='z', reduce_C_function=np.max, gridsize=25)
##df.plot.hexbin(x='a', y='b', C='z', reduce_C_function=np.max, gridsize=25)


# fig, ax = plt.subplots()
# ax.scatter(x, y, c=z, s=50, edgecolor='')
# plt.show()


##
## This is pretty cool.. ;-)
##
## http://matplotlib.org/examples/shapes_and_collections/scatter_demo.html
##
##
