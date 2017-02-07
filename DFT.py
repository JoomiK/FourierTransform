"""Functions for taking discrete data and transforming between 
Cartesian and Fourier space via the Fourier matrix"""

from numpy import arange, transpose, sin, cos, pi, inner, real, imag, e
from pylab import *

def F(n):
	"""Function to generate the Fourier matrix (n by n)"""
    w = e**(2*pi*1j/n)   
    a = arange(n).reshape(1,n)
    a = a*transpose(a)
    m = w**a
    return(m/float(n))

def DFT(data):
	"""Transform a set of discrete data from Cartesian space to Fourier space"""
    n = len(data)
    freqs = inner(data,F(n))    
    re_freqs = real(freqs)
    im_freqs = imag(freqs)
    return([re_freqs,im_freqs])

def inverse_DFT(data):
	"""Transform a set of discrete data from Fourier space to Cartesian space"""
    n = len(data)
    freqs = inner(data,np.conjugate(F(n)*float(n)))  
    re_freqs = real(freqs)
    im_freqs = imag(freqs)
    return([re_freqs, im_freqs])

"""Plot the data"""
n = 1000
x = arange(n)
y = sin(100*x)+sin(10*x)+sin(200*x)+sin(50*x+3)+x/10000
plot(DFT(y)[0])
plot(DFT(y)[1])
show()

