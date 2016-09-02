
"""
From:
http://pandas.pydata.org/pandas-docs/version/0.18.1/basics.html

"""

import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd 


index = pd.date_range('1/1/2000', periods=8)

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=['A', 'B', 'C'])

wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],  major_axis=pd.date_range('1/1/2000', periods=5),  minor_axis=['A', 'B', 'C', 'D'])




"""
http://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html
"""


import matplotlib
matplotlib.style.use('ggplot')

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show(block=False)


df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
plt.figure(); df.plot();
plt.show(block=False)


df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
df3['A'] = pd.Series(list(range(len(df))))
df3.plot(x='A', y='B')
plt.show(block=False)


##   converting
## pandas.core.frame.DataFrame
##   to a
## numpy.ndarray
 
