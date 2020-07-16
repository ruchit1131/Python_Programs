a="a,c,b,d,e,f,g,h,i"

b=a.split(',')# split the string into ',' seperated values

print(b)# prints a list

print(b[1])
print(b[-1])
print(b.pop())
print(' '.join(b))
print(','.join(b[::2]))
