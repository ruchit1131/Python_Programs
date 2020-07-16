li=[3,4,5,6,7,2,9,5,57,34,67,342,8634,0]
j=0
for i in range(len(li)-1):
    for j in range(0,len(li)-i-1):
        if(li[j]<li[j+1]):
            a=li[j+1]
            li[j+1]=li[j]
            li[j]=a
print li[0]
			
