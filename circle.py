import matplotlib.pyplot as plt
import numpy as np
li=[x/20.0 for x in range(-400,400)]
li2=[float(np.sqrt(400-((x/20.0
                         )**2))) for x in range(-400,0)]
li3=[x/20.0 for x in range(400,-400,-1)]
print (li3)
li4=[float(np.sqrt(400-((x/20.0)**2))) for x in range(0,400)]
li5=[np.negative(float(np.sqrt(400-((x/20.0)**2)))) for x in range(400,0,-1)]
li6=[np.negative(float(np.sqrt(400-((x/20.0)**2)))) for x in range(0,-400,-1)]
for i in li3:
    li.append(i)
for i in li4:
    li2.append(i)
for i in li5:
    li2.append(i)
for i in li6:
    li2.append(i)
print (li2)
plt.plot(li,li2)
plt.show()
    

