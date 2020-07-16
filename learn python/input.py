#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("how old are you", end=' ')
age=input()


# In[2]:


weight=input("Your weight is\n")


# In[3]:


print(age+weight)
name=input("your name:")
print(name)


# In[4]:


#to convert the value to int use int() 
age=int(input("your age"))


# In[22]:


print(f"you will die in {'age of '+str(age)} years") #since we are already using double quotes, we have to use single quotes in {}


# In[24]:


x=float(input("how much is a shake?"))


# In[25]:


print(x)


# In[28]:


print("my name is "+input())


# In[29]:


z=input()
y=input()
print(z+y)


# In[30]:


from sys import argv


# In[33]:


name,roll_no,college=argv
print(name,roll_no,college)
#from now on make programs in notepad or any editor


# In[ ]:




