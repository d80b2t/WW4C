

"""

http://www.astropy.org/astropy-tutorials/plot-catalog.html

"""


import numpy as np

## Set up matplotlib and use a nicer set of plot parameters
#%config InlineBackend.rc = {}
import matplotlib
#matplotlib.rc_file("../../templates/matplotlibrc")
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
#%matplotlib inline

from astropy.io import ascii


path = '/cos_pc19a_npr/data/WISE/W4/WISE_W4_W4SNRge3_W4MPROlt4.0_nohdr.tbl'

cols = ['designation', 'ra', 'dec', 'sigra', 'sigdec', 'w1mpro', 'w1sigmpro', 'w1snr', 'w2mpro', 'w2sigmpro', 'w2snr', 'w3mpro', 'w3sigmpro', 'w3snr', 'w4mpro', 'w4sigmpro', 'w4snr', 'w4rchi2']

tbl = ascii.read(path)

## In [14]: type(tbl)
## Out[14]: astropy.table.table.Table

w1 = tbl['w1mpro']
w2 = tbl['w2mpro']
w3 = tbl['w3mpro']
w4 = tbl['w4mpro']
