import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt



maxrange=50
maxlim=4.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
h = 2*maxlim/(maxrange-1)
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('uni.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
# for i in range(0,maxrange-1):
# 	test = (err[i+1]-err[i])/(x[i+1]-x[i])
# 	pdf.append(test) #storing the pdf values in a list


def uni_cdf(x):
	if(x<=0):
			x=0
	elif(x>1):
		x=1
	return x
    
Y = []
for i in range(len(x)):
	Y.append(uni_cdf(x[i]))

plt.plot(x,err,'o')
plt.plot(x,Y)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical","Theoretical"])

#if using termux
#plt.savefig('../figs/uni_pdf.pdf')
#plt.savefig('../figs/uni_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
#else
plt.show()