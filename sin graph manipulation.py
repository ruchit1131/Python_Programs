import matplotlib.pyplot as plt
import numpy as np
k=0
li=[]
li2=[]
flag=1
j=0
while(j<3600):
    k=j%360
    if(k<90 or (k>=180 and k<270)):
        li.append(j)
        li2.append(np.sin(np.deg2rad(k)))
    else:
        li.append(j)
        li2.append(0)
    j=j+1
plt.plot(li,li2)
plt.show()
        
    
