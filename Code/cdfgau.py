#Importing numpy, scipy, mpmath and pyplot
from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import math
import mpmath
def Q(x):
	return mpmath.erfc(x/math.sqrt(2))/2
def cdf(x):
	return 1 - Q(x)
x = np.linspace(-5,5,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
vec_gau_cdf = np.vectorize(cdf)
plt.plot(x.T,err,"o")
plt.plot(x.T,vec_gau_cdf(x))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Empirical","Theoretical"])
plt.show() #opening the plot window