#!/usr/bin/env

"""

"""

import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd 


# The data directory PATH
data_dir = "/cos_pc19a_npr/data/WISE/W4/"

# The data directory FILENAME
data_file="WISE_W4_W4SNRge3_W4MPROlt4.0_nohdr.tbl"

data_in = data_dir+data_file


cols = ['designation', 'ra', 'dec', 'sigra', 'sigdec', 'w1mpro', 'w1sigmpro', 'w1snr', 'w2mpro', 'w2sigmpro', 'w2snr', 'w3mpro', 'w3sigmpro', 'w3snr', 'w4mpro', 'w4sigmpro', 'w4snr', 'w4rchi2']

## If using a file *WITH* a header
# df = pd.read_table(data_in, header=54) 

data = pd.read_table(data_in) 

d = pd.DataFrame(data, columns=cols)

##
print(list(data.columns.values))

## 
print(type(data))


