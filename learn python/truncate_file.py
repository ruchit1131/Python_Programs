from sys import argv

script,filename=argv

print(f"We are going to erase {filename}")
print("If you dont want that hit Ctrl-C")
print("If you want that hit ENTER")

input("?")

print("Opening file")
target=open(filename,'w')

print("Truncating the file.")
target.truncate()#empties the file

print("Write 3 lines")

line1=input("line 1:")
line2=input("line2 :")
line3=input("line3 :")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#target.write(f"{line1}{line2}{line3}") can also be used
print("Andfinally we close it")
#print(target.read()) error: io.UnsupportedOperation: not readable

target.close()
#now to read the file
target=open(filename)
print(target.read())

# modes
#w for writing r for reading and a for append a+ for reading and writing
#open() opens in read mode default
