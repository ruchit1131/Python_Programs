#this function can take many arguments
def print_two(*args):#define a function and the *args puts the arguements in a list
    arg1,arg2=args
    print(f"arg1:{arg1+2},arg2:{arg2+'s'}")

# one or two arguements only
def print_2(arg1,arg2):
    print(f"arg1:{arg1}.arg2:{arg2}")

def print_none():
    print("none")

print_two(2,"2")
print_2(2,"s")
print_none()
#if the argument passed is int then int will be there and if
#string then string will be stored in the varible
#it is bad to have global variables with the same name as function variable
#global variables are declared globally
