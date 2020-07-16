import math
b= raw_input("enter the string:")
c=''
for i in b:
    if(i is ' '):
        continue
    c=c+i
z=math.sqrt(len(c))
print c
print z
floor=int(z)
print floor
ceil=float(len(c))/floor
if(ceil != int(ceil)):
    ceil=int(ceil+1)
ceil=int(ceil)
print ceil
k=0
name=''
namef=''
for z in range(ceil):
    k=z
    for j in range(ceil):
        if(k<len(c)):
            name=name + c[k]
            k=k+ceil
    if(z == 0):
        namef=namef +name
        name=''
    else:
        namef=namef+" "+name
        name=''
    
print namef
        




