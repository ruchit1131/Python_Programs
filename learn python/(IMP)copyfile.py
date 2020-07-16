from sys import argv
from os.path import exists

script,from_file,to_file=argv
if exists(from_file)==False:
    print("The given file DNE")
    exit()


indata=open(from_file).read()

print(f"The input file is {len(indata)} bytes/characters long")

print(f"Does the output file exists? {exists(to_file)}")
if exists(to_file)==False:
    print("aborting")
    exit()

print(f"Copying from {from_file} to {to_file}")
open(to_file,'w').write(indata)

print("Alright done")
open(from_file).close()

#the already written is deleted using write. use append to append data
#open(from_file).close() will open and close the file immediatly
#open(from_file,'w').write() will open write and close the file immediately.
#This will truncate as nothin is passed in this write function
#This program can be written in a line:
#from sys import argv; spt, fr, to = argv; open(to, 'w').write(open(fr).read())
#opening and immediately reading/writing to the File Object
#(without storing a reference to that open File Object (as a variable or something))
#then with some interpreters the files are closed for you.
#In specific terms, CPython (the usual Python implementation) uses reference
#counted objects so the file close almost certainlywill happen right away.
#However, this is not necessarily true for other implementations such as IronPython or Jython.
#The problem is more significant for writes (since you're altering the file), but it still means you have an unclosed file handle until the object is reclaimed by the garbage collector.
#Many generational gcs will clear these kinds of objects (created in a scope,
#with no remaining references to it in the end of the scope) right away,
#but it can't be guaranteed. So, it's better to stick to explicit file closing to be sure.
