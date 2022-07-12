from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import math
import mpmath
a=np.linspace(0,10,50)
with open ("aG.dat","w") as f1:
    for i in range(0,50):
        b=''
        for x in str(a[i]):
            if ord(x) in range(48,58) or ord(x)==46:
                b+=x
        f1.write(b)
        f1.write("\n") 