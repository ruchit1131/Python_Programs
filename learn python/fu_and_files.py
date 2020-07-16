from sys import argv

script, input_file=argv

def print_all(f):
    print(f.read())
    f.seek(0)
    

def print_line(line_no , f):
    a=''
    for i in range(line_no):
        a=f.readline()
    print(a)#or print(f.readlines()[line_no+1])
    f.seek(0)
current_file=open(input_file)
no_of_lines=len(current_file.readlines())#readlines return all lines as a list ****AND THE FILE POINTER IS EOF****
#IF WE DONT USE seek(0) then it will first return empty string
current_file.seek(0)
while(True):
    print("Choose option: \n1. Print whole file\n2. Print a line\n3.Exit")
    ans=input()
    if ans=="1":
        print_all(current_file)
        continue
    if ans=="2":
        line_no=int(input(f"Enter the line no. less than or equal to {no_of_lines}:"))
        if line_no>no_of_lines:
                          print("Out of bounds.")
                          continue
        else: print_line(line_no,current_file)
        continue

    if ans=="3":
        current_file.close()
        exit()

    
                        
        

