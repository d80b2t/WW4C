'''
https://matplotlib.org/users/tight_layout_guide.html
About half-way down the page... 
'''
import numpy as np
import matplotlib.pyplot as plt

n = 30
nsq = n*n

arr = np.arange(nsq).reshape((n,n))

plt.close('all')
fig = plt.figure(figsize=(5, 4), dpi=300, facecolor='w', edgecolor='k')

ax = plt.subplot(111)
im = ax.imshow(arr, interpolation="none")

plt.tight_layout()
plt.show()
