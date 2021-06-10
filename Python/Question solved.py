#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Q. 1 Write a program that asks user to enter a Color/Fruit/Animal name and it should tell which category belongs to , like its is a fruit or color or Animal
Colors = ["Yellow","Green","White","Black"]

Fruits=["Apple","Papaya","Mango","Orange"]

Animals=["Tiger","Lion","Deer","Zebra"]

a=input("Enters the name of Color/Fruits/Animals: ")

if a in Colors:
    print("Enter name belong to: Colors")
elif a in Fruits:
    print("Enter name belong to: Fruits")
elif a in Animals:
    print("Enter name belong to: Animals")
else:
    print("Not belonging to any categories")


# In[7]:


# Q2. Write a program that asks user to enter two items and it tells you if they both are in same category or not. For example if I enter yellow and Black, it will print "Both are colors" but if I enter yellow and Tiger it should print "They don't belong to same category"
Colors = ["Yellow","Green","White","Black"]

Fruits=["Apple","Papaya","Mango","Orange"]

Animals=["Tiger","Lion","Deer","Zebra"]

a=input("Enters the First name of Color/Fruits/Animals: ")
b=input("Enters the Second name of Color/Fruits/Animals:")
if (a in Colors) and (b in Colors):
    print("Enter name belong to same categories: Both are Colors")
elif (a in Fruits) and (b in Fruits):
    print("Enter name belong to same categories: Both are Colors")
elif (a in Animals)and (b in Animsls):
    print("Enter name belong to same categories: Both are Animals")
else:
    print("Both are not from same categories")


# In[50]:


#Q3. Write a python program that can tell you if your grade score good or not . Normal Score range is 40 to 60.

a=float(input("Enter the student Score: "))

if a<30:
    print("Student scored\t", a,"\t","Fail")
elif (a>=30) and (a<=100):
    print("Student scored\t", a,"\t","PASS")


# In[37]:


# Q4 Write a Python program to find those numbers which are divisible by 7 and multiple of 5, for any range.
x=int(input("Enter Start Number: "))
y=int(input("Enter End Number: "))
a=range(x,y)
for i in a:
    if (i%7==0)and (i%5==0):
        print(i)


# In[60]:


#Q. 5 Print square of all numbers between 10 to 20.

x=int(input("Enter Start Number: "))
y=int(input("Enter End Number: "))
a=range(x,y)
e=0
s=0
for i in a:
    if type(i)==int:
        if i%2==0:
            e=i**2
            print("Squre of even number: ",i, "=",e)
        else:
            s=i**2
            print("squre of Odd Number: ",i, "=",s)


# In[ ]:




