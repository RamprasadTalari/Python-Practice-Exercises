#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Variables Exercise -1 
#Create a firstName variable and assign the value Mario to it.

firstName = 'Mario'
print(firstName)


# In[2]:


# Variables Exercise -2
#Create an age variable and assign the value 25 to it.

age = 25
print(age)


# In[3]:


# Variables Exercise -3
#Create a sentence variable and assign the value Hello, I'm Mario! to it without using double quotes.

sentence =  '''Hello, I'm Mario!'''
print(sentence)





# In[4]:


# Variables Exercise -4
# Create an amount variable and assign a float value to it.

amount = float(4.5)
print(amount)


# In[5]:


# Variables Exercise -5
#Create a set of 3 variables and assign True as value of each one.

a = True
b = True
c = True

print(a,b,c)


# In[6]:


# Variables Exercise -6
#Remove the illegal characters in the variable 1my-first2_Name = 'Mario'.

my_first2_Name = 'Mario'
print(my_first2_Name)


# In[7]:


# Variables Exercise -7
# Write single quotes or double quotes correctly


print('''Hi,
my name is
John Doe
python''')


# In[8]:


# Variables Exercise -8
#Create 3 different variables and assign 3 different values. Write only one operation. Print them on terminal


a,b,c = 1,2,3

print(a+b+c)

a,b,c = 1,2,3

print(a,b,c)


# In[9]:


# Variables Exercise -9

# Swap the value of the variables


a = 12
b = 'Hello'

c=a
a=b
b=c
print(a,b)


# In[10]:


# Variables Exercise -10

# Print the length of each variable.

hello = 'Hello!'
name = 'Jhon Doe'
age = '40'

print(len(hello),len(name),len(age))


# In[11]:


# Variables Exercise -11

# Modify the variables as suggested
a = 'hello' #capitalize
b = 'tom' #uppercase
c = 'LAURA' #lowercase


question = 'How are you' #change o in e
age_question = 'How old are you?' #use the correct method to create a string for each word
print(a, b, c, question, age_question)




print(a.capitalize())
print(b.upper())
print(c.lower())

print(question.replace("o","e"))
print(age_question.split())
print(a.capitalize(),b.upper(),c.lower(),question.replace("o","e"),age_question.split())


# In[12]:


# Variables Exercise -12

#Create two variables called name and age.
#Then create a variable called hello and print the name and the age. Use the formatted string literal.

name = 'Ram'
age = 26
hello = 'hello'
print(f"Hello!, I am {name}, and my age is {age}")


# In[13]:


# Operators Exercise -1

# Insert the appropriate logical operator in order to print False

print(False >True)


# In[14]:


# Operators Exercise -2

#Change the logical operators in order to print True
# print(False and (0 != 0 or True)) # Should print True


print(False or (0 != 0 or True))


# In[15]:


# Operators Exercise -3

#Print the rest of the 5/2 division

print(5%2)



# In[16]:


# Operators Exercise -4

# Insert the appropriate logical operator in order to print True.

# print(not ("testing" == "testing" ... "Mario" == "Cool Guy")) # Should print True

print(not ("testing" == "testing" > "Mario" == "Cool Guy"))


# In[17]:


# Operators Exercise -5

# Initialize and print the sentence variable using the appropriate operators.
# print(sentence) # Should print "Mario Rossi"

firstName ="Mario"
lastName ="Rossi"

sentence = firstName +' '+ lastName

print(sentence)


# In[18]:


# Operators Exercise -6

# Check if "Nike" is in brands array using the appropriate logical operator

# print("Nike" ... brands) # Should print True

brands = ["Adidas", "Nike"]
print("Nike" in brands)


# In[19]:


# Operators Exercise -7

# print("Reebok" ... brands) # Should print True

brands = ["Adidas", "Nike"]

print("Reebok" not in brands)


# In[20]:


# Methods Exercise -1

# With type command you can see the type of a variable in python 
# eg: type(1) print each components type with this way you can see most significant data types in python

print(type("Hello World"))
print(type(True))
print(type(False))
print(type(33))
print(type(24.5))
print(type(4+1j))
print(type(4j))
print(type(["lion", "monkey", "dog","fish"]))
print(type(("lion", "monkey", "dog","fish")))
print(type({"name" : "John", "surname" : "Doe", "age":22}))
print(type({"lion", "monkey", "dog","fish"}))


# In[21]:


# Methods Exercise -2

# the number types can be converted to each other wit the int() float() complex() methods
# also float numbers can be rounded with the method round()

# convert num1 to float and assign to itself
# convert num2 to int and assign to itself
# convert num3 to complex and assign to itself
# use round method for num4 and assign to itself
# use round method for num5 and assign to itself
# print them all
# print their types

num1 = 1.3
num2 = 2.3
num3 = 1j 
num4 = 1.4 
num5 = 1.5

num1=float(num1)
num1
num2=int(num2)
num2
num3=complex(num3)
num3
num4=round(num4)
num4
num5=round(num5)
num5
print(num1,num2,num3,num4,num5)
print(type(num1),type(num2),type(num3),type(num4),type(num5))


# In[22]:


# Methods Exercise -3

# to convert a number to string we can use str() function this is called casting

# cast num1 to string and assign to num1_str
# check the length of the string
# get the third element of string (the one in the 3rd order)
# get the 3-5 elements of string (both inclusive) by string slicing
# check if num2 in string (cast if necessary)
# check if num3 in string (cast if necessary)
# concatenate 0 to the string from left and assign to string_with_0
# get the characters of string_with_0 from start to position 4 (end point exclusive)
# get the characters of string_with_0 from position 5 until the end
# use negative indexing to reach the "567" string_with_0


num1 = 1122334455666
num1_str = str(num1)
num1_str

len(num1_str)

num1_str[2:3]

num1_str[3:6]

if '2' in num1_str:
    print('its true')
    
if '3' in num1_str:
    print('its true')
    
    
string_with_0 = '0' + num1_str
string_with_0

string_with_0[0:4]
string_with_0[5:13]
string_with_0[-4:-1]


# In[23]:


#Conditions Exercises-1

# print if num1 or num2 is greater 

num1 = 335
num2 = 66

if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num1} is not greater than {num2}")


# In[24]:


#Conditions Exercises-2

#check if number1 is greater than number 2 and print number1 is greater than number2
#check and if number 2 is greater than number 1 and print number2 is greater than number1
#finally at the end if both conditions incorrect print number2 equals to number1

number1 = 66
number2 = 66

if number1 > number2:
    print(f"{number1} is greater than {number2}") 
elif number2 > number1:
    print(f"{number2} is greater than {number1}")
else : 
    print(f"{number2} is equals to {number1}")


# In[25]:


#Conditions Exercises-3
#Compare those 2 numbers and write X greater than Y But be sure you are making the check for all the conditions

import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)


if number1 > number2:
    if number1 == number2:
        print("It is equal")
    if  number1 >= number2:
        print("It is greater than or equal")
    if  number1 <= number2:
        print("It is less than or equal")
    if  number1 != number2:
        print("It is not equal")
else:
    print(f"{number1} is lesser than {number2}")


# In[26]:


#Conditions Exercises-4


import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    if abs(number1) == abs(number2):
        print("It is equal")
    if abs(number1) >= abs(number2):
        print("It is greater than or equal")
    if abs(number1) <= abs(number2):
        print("It is less than or equal")
    if abs(number1) != abs(number2):
        print("It is not equal")
else:
    print(f"{abs(number1)} is lesser than {abs(number2)}")

