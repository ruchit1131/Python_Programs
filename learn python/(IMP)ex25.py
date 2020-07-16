#This file is a module and all its functions can be imported by using import (name of file)
#the functions can be accessed by e.g. (name of file).break_words("abc hdjk hdj eie")
#or only a function can be accessed by from (name of file) import (name of function) OR to import all functions 
#from (name of file) import *
def break_words(stuff):
    words=stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word=words.pop(0)
    print(word)

def print_last_word(words):
    word=words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words= break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
'''Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: C:/Users/Ruchit/Documents/Learn Python the hard way/ex25.py ====
>>> import ex25
>>> sentence="all good things come to those who wait"
>>> words=ex25.break_words(sentence)
>>> words
['all', 'good', 'things', 'come', 'to', 'those', 'who', 'wait']
>>> sorted_words=ex25.sort_words(words)
>>> sorted_words
['all', 'come', 'good', 'things', 'those', 'to', 'wait', 'who']
>>> ex25.print_first_word(words)
all
>>> ex25.print_last_word(words)
wait
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> ex25.print_first_word(sorted_words)
all
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait']
>>> ex25.print_first_and_last(sentence)
all
wait
>>> ex25.print_first_and_last_sorted(sentence)
all
who
>>> '''

'''Triple quotes are treated as regular strings with the exception that they can span multiple lines.
By regular strings I mean that if they are not assigned to a variable they will be immediately
garbage collected as soon as that code executes. hence are not ignored by the interpreter in the same way that #a comment is.'''
#Python documentation strings (or docstrings) provide a convenient way of
#associating documentation with Python modules, functions, classes, and methods.
#The docstrings are declared using “””triple double quotes””” just below the class,
#method or function declaration. All functions should have a docstring.
#Example
'''
def my_function(arg1): 
    """ 
    Summary line. 
  
    Extended description of function. 
  
    Parameters: 
    arg1 (int): Description of arg1 
  
    Returns: 
    int: Description of return value 
  
    """
  
    return arg1 
  
print my_function.__doc__ 


Output:

    Summary line.
    Extended description of function.
    Parameters:
    arg1 (int): Description of arg1

    Returns:
    int: Description of return value
'''
#we can also get docstrings by using help function
#e.g help((IMP)ex25) and also help((IMPex25.break_words)
The docstrings are declared using “””triple double quotes””” just below the class,
#method or function declaration.


#funtion returns None when there is nothing to return