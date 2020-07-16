from time import sleep
j=0
while(1):
    for i in range(1,4):
        print " "*j,
        print "*"*i
    j=j+3
    sleep(.3)
