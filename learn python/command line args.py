from sys import argv
a,b,c=argv
print(a,b,c)
print(20+int(c))
# now the first arguement will always the name of the python script i.e
#a is the script name and we can only give two command line args which are
#b and c. so rather we can write script,first,second=argv
#now this method is used to take input from command line and the input is
# always a string
#if you dont give pass any arguement, it will say that only one value is unpacked i.e the script one

