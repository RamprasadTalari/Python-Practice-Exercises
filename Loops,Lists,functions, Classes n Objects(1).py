#!/usr/bin/env python
# coding: utf-8

# # Exercise 1- While Loop
# 
# """Create ` * **
# 
# ` this shape with print and while loop statements"""

# In[1]:


i = 0
while i < 6:
    if i == 0 or i ==3:
        print("`")
    else:
        print("*"* i,end=(" "))
    i +=1


# # Exercise 2 - For Loop
# 
# """Create
# *
# ***
# *****
# this shape with print, for loop, if and continue statements"""

# In[2]:


for i in range(6):
    if i % 2 == 0:
        continue
    print("*" * i)


# # Exercise 3 - For Loop
# 
# """Check if it is time for "coffee break" if it is just break
# To do that lets iterate through given list don't change the "COFFEE BREAK" statement.
# just find another way to do it'''
# 
# """todo = ["exercise1", "exercise2", "exercise3","coffee break" ,"exercise4","exercise5","exercise6"]
#     for x in todo:
#   if x._ == "COFFEE BREAK":
#         print(x)
#         break"""

# In[3]:


To_do = ["class","class2","COFFE_BREAK","class3"]
for break1 in range(len(To_do)):
    if To_do[break1] == "COFFE_BREAK":
        print("its a break")
        break  


# # Exercise 4 - For Loop
# """Iterate each elements of 'list1,tuple1,set1' and print them out
# For the 'dict1' iterate all elements but only print the ones who are living on land in the form of 'x lives in y' 
# """

# In[4]:


list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

for list_1 in range(len(list1)):
    
    print(type(list1),list1[list_1], end=(" "))
    
print(" ")
    
for tuple_1 in range(len(tuple1)):
    
    print(type(tuple1),tuple1[tuple_1], end=(" "))
print(" ")

    
for set_1 in set1:
    
    
    print(type(set1),set_1, end=(" "))

print(" ")
for dict_1 in dict1:
    if dict1[dict_1] == "land":
        print("--dict_keys  -----> ",dict_1,end=(""))


# # Data structures
# """Remember list,set,dictionary are mutable and tuple is immutable list,tuple elements can be reached by index
#  for dictionary it is not an option to reach by index the element key has to be known to reach
# and for set the items cannot be reached directly but it is possible to iterate."""
# 
# """ 1.print the lengths of list1,tuple1,set1,dict1
#  2.print the first element of list1 and tuple1
#  3.print the value of lion key of dict1
#  4.change the 2nd position element of list1 to "rabbit"
#  5.try to change the 2nd position element of the tuple to "rabbit" and explain what happened.
#  6.add "monkey" to list1
#  7.remove "rabbit" from list1
#  8.in dict1 the number of feet is written as value to each animal the fixh has wrong value just fix it."""
# 

# In[5]:


list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}

print("1 :",len(list1),len(tuple1),len(set1),len(dict1))
print("2 : ", list1[0],tuple1[0])
print("3 :" , dict1["lion"])
list1[1] ="rabbit"
print("4 :", list1)
try:
    tuple1[1]="rabbit"
except:
    print("5 : cannot update because it is immutable" )

list1.append("monkey")    
print("6 : ", list1)

list1.remove("rabbit")
print("7 :", list1)

dict1["fish"] = 0
print("8 :" , dict1)


# # Exercise 1 - Functions
# """ To create functions in python we start with def word and after it the name of function comes with without parameters example is here
# 
# def hello():
# print("hello")
# Now you create a function named goodbye without parameters which prints good bye"""

# In[6]:


def goodbye():
    print("good bye")
goodbye()


# # Exercise 2 - Functions
# """Inside the parenthesis variables can be used those variables as known as parameters of the function provides control inside the function example is here
# 
# def hello(name):
# print(f"hello {name}")
# Now you create a function named goodbye with a parameter name and say 'Good bye Adam' """
# 

# In[7]:


def gooodbye(name):
    print("good bye---->",name)
gooodbye("Ram")


# # Exercise 3 - Functions
# """ Let's see what is your user name on your computer
# to do that we are going to use os module which is a built in module in python
# and has many built in functions in it
# 
# to be able to use os functions
# import os then call getlogin method of the module
# then assign the output to user variable and print the user"""
# 

# In[8]:


import os
def user():
    return os.getlogin()
user()


# # Exercise 4 - Functions
# 
# """Now create a function for John Doe and his family that greets every one in the family.
# Since it will usually John Doe the name and surname parameter must be defaulted
#  and when someone else comes it has to greet the new comer with name surname parameters which were overwritten. Make it possible.
#  The function have to print "Hello John Doe" where John and Doe is parametric
#  Greet each our John first then the people in the list with for loop and the function
#  What you have to use
# 
#  for loop
#  function
#  string operation
#  list index
#  Output format
# 
#  Hello John Doe!
#  Hello Tristram Mcbride!
#  Hello Baldwin Preston!
#  Hello Wally Collins!"""
# 

# In[23]:


name = []
surname = []

def greet(name,surname):
    
    print("Hello :" ,name1,sur)
    
n = int(input( " number of people : "))
for i in range(0,n):
    count_name = input()
    count2_sur = input()
    name.append(count_name)
    surname.append(count2_sur)
    name1 = str(name[i])
    sur = str(surname[i])
    
    greet(name1,sur)


# # Exercise 5 - Functions
# ''' Import random function
#  Create a function random_list_summer creates n elemented list with min value = -100 max value = 100 it has to print the list first and sum all the elements of it default element number is 15
#  Don't forget to call the function
#  for some features and functions you might have to search on the internet do it don't lose your courage'''
# 

# In[24]:


import random

def  random_list_summer(n):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(-100,100))
        
    return rand_list[0],sum(rand_list),rand_list


random_list_summer(15)


# # Exercise 6 - Functions
# """Implement Fibonacci sequence as recursive function and print first 5 elements."""

# In[13]:


def fibo_val(n):
    if n <= 1:
        return n
    else:
        return(fibo_val(n-1) + fibo_val(n-2))
        


fibo = input("enter a fibonocci value : ") 
for i in range(int(fibo)):
    print(fibo_val(i))
    


# # Exercise 7 - Functions
# """Create a lambda function that returns 2nd power of given number if its even
# and run it on the given list
# then print the result to the screen"""

# In[14]:


my_list= [*range(5)] 
def lam_fun(i):
    return lambda a : a ** i 
        

n = int(input("enter num of values : "))
list_1 = []
for i in range(n):
    if i%2 == 0:
        lam = lam_fun(n)
        list_1.append(lam(i))
print(list_1)


# # Classes and Object

# # Exercise 1- Classes and Object

# In[6]:


# Let's create Animal class and then create the animal object that runs and having 4 legs

# create animal object with leg count when created print "Animal object was created"
# and then call runs method of it and it prints "Running started" 


class Animal( ):
    def __init__(self,leg_count):
        print("object is created ")
        self.leg_count = leg_count
    def run(self):
        print("started running")
        
animal = Animal(4)
animal.run()
    
    


# # Exercise 2- Classes and Object

# In[2]:


# Now continue with the Animal class we had used before

# Add a method to count the legs count_legs which prints the number of legs

# Add a method to count the legs return_legs which returns the number of legs

# print number of legs directly from number_of_legs variable of the object



"""class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self.number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self.number_of_legs}")"""

class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self.number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self.number_of_legs}")
    
    def return_legs(self):
        return self.number_of_legs

animal = Animal(4)
print(animal.runs())
print(animal.count_legs())
print(animal.return_legs())
print(animal.number_of_legs)
    


# # Exercise 3- Classes and Object

# In[4]:


# Again let's keep talking on Animal class we have.
# with 3 methods we just reached the number of legs
# to prevent direct interacting with the class variables
# most of the other programming languages have encapsulation.
# But in python we don't have it instead we use _ prefix for it as convention
# it is also same for the methods

# _legs this shows us not to touch this variable its up to you if you want to change it you can but _ asks you politely not to do it.

# Change the number_of_legs to conventional private variable and call from another method



"""class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self.number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self.number_of_legs}")

    def return_legs(self):
        return self.number_of_legs
        
animal= Animal(4)
animal.count_legs()
print(animal.return_legs())
print(animal.number_of_legs)"""


class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self.number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self.number_of_legs}")
    
    def return_legs(self):
        return self.number_of_legs

animal = Animal(4)
print(animal.runs())
print(animal.count_legs())
print(animal.return_legs())
print(animal.number_of_legs)


# # Exercise 4- Classes and Object

# In[5]:


# Let's inherit Dog class from Animal add name(private) attribute to Dog class and then bark method to print woof woof

# print name_of_dog make it bark count the legs

class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self._number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self._number_of_legs}")

    def return_legs(self):
        return self._number_of_legs
        
animal= Animal(4)
animal.count_legs()
print(animal.return_legs())
print(animal._number_of_legs)

class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self._number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self._number_of_legs}")

    def return_legs(self):
        return self._number_of_legs
class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,4)
        self._name = name
        
    def bark(self):
            print("bow bow")
        
animal= Animal(4)
animal.count_legs()
print(animal.return_legs())
print(animal._number_of_legs)

dog = Dog("Alex")
dog.bark()

