import math
with open("uni.dat","r") as f1:
    with open("V.dat","w") as f2:
        for line in f1:
            if(1-float(line)>0):
                a=str({-2*math.log(1-float(line))})
                b=''
                for x in a:
                    if ord(x) in range(48,58) or ord(x)==46:
                        b+=x
                f2.write(b)
                f2.write("\n")