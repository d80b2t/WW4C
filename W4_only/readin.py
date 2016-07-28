'''

Basic python script to read-in the W4_only.dat data and do interesting 
things with it...

'''


import astropy.io.ascii as ascii
from astropy import coordinates as coord
from astropy import units as u

from matplotlib import pyplot as plt
import numpy as np
from math import *


mdata=ascii.read('W4_only.dat')  

# Just want to convert RA, Decl. into 
# https://astropy.readthedocs.org/en/v0.2.1/coordinates/index.html
# 
