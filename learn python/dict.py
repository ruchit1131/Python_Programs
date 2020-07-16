stuff={"name":"zed","age":39,"height":74}
print(stuff['name'])
stuff['city']="JD"
print(stuff)

stuff[1]="wow"
stuff[2]="neato"

print(stuff)

del stuff[1]
del stuff[2]

print(stuff)

list=list(stuff)#will print only the keys
print(list)
lis=stuff.items()
print(lis)# will print keys and values coupled in a tuple
#now we can iterate in dictionary in two ways:

for i in stuff:
    print(i,stuff[i])
    
#or

for i,j in stuff.items():
    print(i,j)
    
#this is running for loop for two values
#EG:
list=[[1,2,3],[4,5,6],[7,8,9]]
for i, j, k in list:
    print(i,j,k,i+j+k)
#notthis , in print statement automatically gives a white space
    print("hello","hi")


'''What is the difference between a list and a dictionary? A list is for an ordered list of items. A dictionary
(or dict) is for matching some items (called ”keys”) to other items (called ”values”).
What would I use a dictionary for? When you have to take one value and ”look up” another value. In
fact, you could call dictionaries ”look up tables.”
What would I use a list for? Use a list for any sequence of things that need to be in order, and you only
need to look them up by a numeric index.
What if I need a dictionary, but I need it to be in order? Take a look at the collections.OrderedDict
data structure in Python. Search for it online to find the documentation.'''
