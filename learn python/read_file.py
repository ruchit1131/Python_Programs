#Usually, command-line arguments are options for the program whereas
#sandard input are data to be processed. Sometimes, you can use one or the other and do the same thing, sometimes not.
from sys import argv
script,filename=argv
txt=open(filename)
#makes the file object
print(f"Here is your file {filename}:")
print(txt.read())
print("Type the filename again")
file_again=input('>>')
txt_again=open(file_again)
print(txt_again.read())
