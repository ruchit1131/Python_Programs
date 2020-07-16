#This is a module
pi=3.14156
age=20
name="Ruchit"

def add(*a):
    s=0
    for i in a:
        s+=i
    return s

print("This is a module")# This will be printed when we import Module
#even if we import only a variable or function from this Module, The print
#statement will print nevertheless
