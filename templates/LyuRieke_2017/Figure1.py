'''

Reproducing Figure 1 of: 
"The Intrinsic Far-infrared Continua of Type-1 Quasars"
Jianwei Lyu, George H. Rieke
https://arxiv.org/abs/1704.06987v1

'''

from astropy.io import ascii

## http://docs.astropy.org/en/stable/io/ascii/
data = ascii.read("sources.dat")  
data = ascii.read(lines, format='fixed_width_two_line', delimiter='&')
data = ascii.read(lines, format='csv', fast_reader=False)

