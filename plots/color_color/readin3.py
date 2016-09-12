#!/usr/bin/env

"""

"""
from __future__ import division
from numpy.random import randn
from pandas import DataFrame, Series
from scipy.stats import gaussian_kde
from astropy.table import Table, Column

import os
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


path = '/cos_pc19a_npr/data/WISE/W4/WISE_W4_W4SNRge3_W4MPROlt4.0_nohdr.tbl'

tdata = Table.read(path,format='ascii')
firstcol = tdata.columns[0].data

from astropy.io import ascii
tdata = ascii.read(path)
firstcol = tdata.columns[0].data
