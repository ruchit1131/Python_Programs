#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("i am", 20, "years old.")


# In[4]:


my_age=20
my_name='ruchit'
print(f"my name is {my_name} and my age is {my_age}") # a smalln f before the string for string formatting


# In[5]:


print(round(1.6789))


# In[6]:


print(round(1.45))


# In[8]:


print (round(1.5))


# In[10]:


print (round(2.5))#round function is used to round off digits


# In[93]:


x=f"there are {80-my_age} years more to\n live"


# In[94]:


print(x)


# In[15]:


print(f"i said {x}")


# In[22]:


b= "isnt that joke funny {}"


# In[95]:


print(b.format("\nnope"))


# In[24]:


#we can use format() function to format strings. we can add two or more formatters
#{} is used to put the value of whatever is there in the format(value). is whatever the format function returns
x="this is a good {}".format("day")


# In[25]:


print(x)


# In[27]:


y="this is a good {}"


# In[28]:


print(y.format("day"))


# In[36]:


u= "this is a {} {} and my name is {} and my  age is{} and i will live {} years more"


# In[37]:


print(u.format("good","day","RUCHIT",20,80))


# In[39]:


z="{0} {1} {2} {3}"


# In[41]:


print(z.format("my","name","is","rk"))


# In[43]:


z="{3} {2} {0} {1}"


# In[45]:


print(z.format("my","name", "is","ruchit"))


# In[46]:


t="ruchit"


# In[47]:


y=20


# In[50]:


z="my name and age are {} and {} respectively".format(t,y)


# In[74]:


print(z)
z= True
print( "is it {} that today is monday".format(z))#this is a boolean value


# In[55]:


#strings can be added
x="good "
y="day"
z=x+y


# In[56]:


print(z)


# In[64]:


y=20
print("my age is " + str(y))


# In[66]:


#* is used to print multiple times
print("Good "*3,"Very good job!")


# In[76]:


#end='' fucntion is used to end the sentence with whatever it returns
print("this is a test", end=' ')
print("this will print in the same line")


# In[77]:


print()


# In[82]:


#print("djfkd
#      dfdfdfd") this will give an error. to write as much as you want use three quotes 


# In[83]:


print("""this
will do 
wonders
wow!!!""")


# In[89]:


z='''this
will also 
do 
                                            wonders'''


# In[90]:


print(z)


# In[86]:


#\n is a new line character
print("a\nb")


# In[88]:


# other characters are: \\ \' \" \a(bell) \b(backspace) \t(tab) \f(form feed) \n(new line) 
print("a\\b")
print("a\\b")


# In[ ]:




