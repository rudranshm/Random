from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import math
import mpmath
def Q(x):
	return mpmath.erfc(x/math.sqrt(2))/2
def P(x):
    return Q(x)
a=np.linspace(0,10,50)
p=np.loadtxt("Pgen.dat",dtype="double")  
simlen = int(1e4) 
vec_T_pdf = np.vectorize(P)
# plt.subplot(211)
# plt.semilogy(a,p,'o')
# plt.semilogy(a,vec_T_pdf(a))
# plt.subplot(212)
plt.plot(a,p,'o')
plt.plot(a,vec_T_pdf(a))
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Empirical","Theoretical"])
plt.show()
