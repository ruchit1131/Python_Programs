x=b"hello"
print(x)
for i in range(2,10):
    print (i)

for i in "abcde":
    print (i)

print("i" in "drink") #True

print("i" in "drunk") #False

#for "i" in "gif":
#    print("This is printed") Error can't assign to literal


#for 2 in range(4):
#    print("This is also printed") Error cant assign to literal

#for 3==3:
#    print(True) in valid syntax

'''for i in (1,2,3,4,5,6):
    print(i)

for i in {"a":1,"b":2,"c":3}:
    print(i)
    print({"a":1,"b":2,"c":3}[i])

>>> a = 500
>>> b = 500
>>> a == b
True
>>> a is b
False
That's pretty much what we expected: a and b have the same value,
but are distinct entities. But what about this?

>>> c = 200
>>> d = 200
>>> c == d
True
>>> c is d
True
This is inconsistent with the earlier result. What's going on here?
It turns out the reference implementation of Python
caches integer objects in the range -5..256 as singleton instances
for performance reasons. Here's an example demonstrating this:

>>> for i in range(250, 260): a = i:
        print "%i: %s" % (i, a is int(str(i)));
... 
250: True
251: True
252: True
253: True
254: True
255: True
256: True
257: False
258: False
259: False
This is another obvious reason not to use is: the behavior is left
up to implementations when you're erroneously using it for value equality.'''


'''Type Description Example
True; True boolean value.; True or False == True
False; False boolean value.; False and True == False
None; Represents ”nothing” or ”no value”.; x = None
bytes; Stores bytes, maybe of text, PNG, file, etc.; x = b"hello"
strings; Stores textual information.; x = "hello"
numbers; Stores integers.; i = 100
floats; Stores decimals.; i = 10.389
lists; Stores a list of things.; j = [1,2,3,4]
dicts; Stores a key=value mapping of things.; e = {'x': 1, 'y': 2}'''


