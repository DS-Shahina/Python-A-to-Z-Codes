########################## ###################################
##### Basic Data Types
# Integer -----> int ----> Whole numbers such as 3,300,200
# Floating Point ---> float ---> numbers with decimal point 3.56,2.45,76.87
# string ---> str ---> ordered sequence of characters
# lists ---> list ---> ordered sequence of objects
#  Dictionaries ---> dict ---> unordered key value pairs {'mykey':'value'}
# Tuples --> tup --> ordered immutable sequence of objects
# sets --> set ---> unorderd collections of unique objects
#  Boolean --> bool --> logical values indicating True or False
# Data type

#Integer

print(1) 

print(2+4)  #addition

print(12*3) # Multiplication 
print(12/3) # Devision

# Float

print(11.5)

x = 55.45

print(x)

type(x)

# Complex Number

print(2+3j)

type(2+3j)

# Boolean Type

type(True)

type(False)   

#b=3  
# Variable Assignment Rules
# Names cannot start with a number
# there can be no space in the name , use _ instead ex :- name_last
# can't use any of these symbols  "",<>,\,|,?,!,@,#,%,$,&,*,~, +
# It's considered best practice to use lowe case names as variable assignment
# Avoid using words that have special meaning in Pyhton like "list"

#######Strings###############
##############################################################
## Strings are sequence of characters using the syntax of either single quote
# or double quote, because strings are ordered sequence it means we can use indexing
# and slicing to grab sub sections of the string, Indexing notation uses[]
# these actions uses [] and a number index to indicate positons of what you
# wish to grab
# this is a ordered sequence of characters, then we can index it and slice it

# multiline string uses triple quote or a tripe single quote
a = """ This data has three types of flower classes: 
    Setosa, Versicolour, and Virginica. The dataset is available in the 
    scikit-learn library, or you can also download it from the UCI Machine 
    Learning Library."""
print(a)
type(a)
len(a)


# syntax of indexing of strings

#  [start:stop:step] this is called as slicing of strings

# Start is a numerical index for slice start
# stop is the index you go upto(but not included)
# step is the jump you take

#Accesing Value in Strings   
Name = "Aditya"

print(Name[0]) 

print(Name[3])

print(Name[1:4])

print(Name[-1])

print(Name[-3:-1]) # start from -3 to -1
print(len(Name))

#Update Strings 
var1 = 'Hello World!  '
print('Hello')
print("Updated String :- ", var1 + 'Python')
print("Updated String :-", var1[:6] + 'Python')

print("hello \nworld") # \n used to get new line

# String Formating 
# %s - string where % is modulus
# %d - integer
# %f - float
print("My name is %s and weight is %d kgs!" % ('Nikhil', 20.5)) # it will not take decimal value
print("My name is %s and height is %f kgs!" % ('Nikhil', 20.5))

print('This is a string {}'.format('inserted'))

print("My name is {} and my weight is {}".format('shahina',66.7))

Name = 'shahina'
Weight = 66.7
print("My name is {1} and my weight is {0}".format(Name,Weight)) # it gives index value

print('the output is {r}'.format(r = Weight))

# formatted string literals
print(f'My name is {Name} & weight is {Weight} kgs') #fstrings

type(Weight)
#Ex :1 

Name = input("Enter your name: ")
type(Name)
Weight = int(input("Enter your weight: "))
type(Weight)
Height = float(input("Enter your weight: "))
type(Height)
size = eval(input("Enter your size: "))
type(size) # for both int,complex, bool as well as float except string

#Triple Quotes

Statement = """my name is "Bahubali" and my age is "25".
I stay in Maahishmathi"""

type(Statement)
# type different statement in single line
print('''Hello How are you?'''); print("fine"); print("wbu?")

Name = 'shahina Athar'
type(Name)
print(Name)
# To make first letter capital
print(Name.capitalize()) # 1st letter of 1st word
print(Name.upper())
print(Name.lower())
print(Name.title()) # 1st letter of every word
a = 'ShAhInA'
print(a.swapcase()) # lower to upper and upper to lower

# To make string at center in given spaces
Name.center(50)
len(Name.center(50))

#Count number of occurrences of a given substring using start and end
# define string
string = "Shahina is a trainer"
substring = "i"

count = string.count(substring)
count

count = string.count("h") # or direct
count

print("The count is:", count)

# count after first 'i' and before the last 'i'
#len(string)
count = string.count(substring,8,25) # till 8 to 25 it count "i""
count

#print count
print("The count is:", count)

##Returns true if string has at least 1 character and all characters 
#are alphanumeric and false otherwise.

Num = 'shahina23' # No Space in this string
print(Num.isalnum()) # alnum is alpha numeric value

Num = "this is string examplehi 123" # space that's y false
Num.isalnum()

#This method returns true if all characters in the string are 
#alphabetic and there is at least one character, false otherwise.

Num = "Shahina" # No space & digit in this string
Num.isalpha()
Num.isalnum() # no space - true

Num = "this is string example0909090!!!" # it has space
Num.isalpha()

#This method returns true if all characters in the string are 
#digits and there is at least one character, false otherwise.

Num = "123456" # Only digit in this string
Num.isdigit()

Num = "this is string example!!!"
Num.isdigit()

#This method returns a copy of the string in 
#which all case-based characters have been lowercased.

Num = "THIS IS STRING EXAMPLE!!!";
Num.islower()
Num.isupper()
Num.lower()

#his method returns a copy of the string in which 
#all case-based characters have been Uppercase.

Num = "this is string example!!!"
Num.isupper()
Num.islower()
Num.upper()
Num[1:5].isalpha() # check index form 1 to 4
"example7876".isalnum()

Num = "this is string example0909090";
Num.isalpha()
Num[15:50].isalnum() # true- from example0909090
Num.find("is") # 2nd position
Num.index("example0909090") # index position
len(Num)
#The following example shows the usage of replace() method.

reply = "it is string example!!! is really a string"

print(reply.replace("is","was"))
print(reply.replace("is","was",1)) # 1 is represents as a 1st "is" value
print(reply.replace("is","was",2)) # both replace with was

#The following example shows the usage of split() method.
split1 = "Line1-abcdef Line2-abc \nLine4-abcd"
print(split1)
print(split1.split(' ', 1 ))# spliting only 1 time with space
print(split1.split('ab',1)) # splitting only 1 time from where 1st ab lied
print(split1.split('ab' )) # it split from ab to entire list
type(split1.split())
split1 = split1.split() # element wise indexing
print(split1.split(' ', 1 ))# spliting only 1 time with space
type(split1.split())
split1[2].isalpha()
split1[1].isalnum()

# line number 241 and 242 is string it's not convert into list till now
# if we run line number 241 & 242 after line number 243 so it will show error

###############################   List   ################################

# A list data type is given in square brackets and each element is separated by comma.

list1 = ['Sharat', '360DigiTMG', 2013, 2018]
list1 =['ssss',5,5.5,40+55j,True]
list1

#Access values in the variable using index numbers

print(list1[0])
print(list1[3])
print(list1[1:4])
len(list1) # length of the list
#functions in list data type

# Append : add  new element to the existing list
aList = [123, 'xyz', 'zara', 'abc']
aList[2]=55+40j # 2nd position replace with complex number
print(aList)
B = [2434,56]
aList.append(B)
aList

aList.append(2009) # add in last
print(aList)

#Pop : remove the elment from existing list - right to left
#Pop: accept only 1 argument

print(aList.pop()) #erase last one

print(aList)
# pop the element using index number - each time it increment and give different results
print(aList.pop(2)) 
print(aList)
print(aList.pop(2))
print(aList)
print(aList.pop(1))
print(aList)
print(aList.pop(0))
print(aList)
aList = [123, 'xyz', 'zara', 'abc',6788]
print(aList[1:4].pop()) # in indexing the last value is pop out
print(aList) # because we did'nt give amy argument to pop that's y it show like that

#Insert: insert a value using index number 
aList = [123, 'xyz', 'tommy', 'abc', 123]

aList.insert(3, 2009) # add 2009 in 3rd place
print(aList)
B = 22,55,66 # multiple element insert
aList.insert(3,B)
aList
aList.insert(3,(22,55,66)) ; aList.insert(5,B) #Multiple Insert in single time
aList
#Extend: append vs extend  
aList = [123, 'xyz', 'tommy', 'abc', 123]
bList = [2009,'beneli']

aList.extend(bList) # it extend the list
aList

bList.extend(aList)
bList

#Reverse: to reverse the given list
aList = [123, 'xyz', 'tommy', 'abc', 123]
aList.reverse()
print(aList)

#Sort: sort the given list from ascending or descending

blist = [8,99,45,33]
blist.sort() # ascending order
print(blist)
blist.sort(reverse=True) # descending order
print(blist)

#count: count the value in given list of elements
aList = [123,'xyz','zara','abc','123','zara']
print(aList.count(123))
blist = [123,'xyz','zara','abc','123','zara',['zara','abc']]
print(blist.count('zara')) # it count only 2 with parental list not 2nd list
string = "gjxhgsj"
string.count('g')

#index - position
print(aList.index('zara'))

# cocatination - adding

list1=[1,2,3]
list2=[1,2,3]

1+2
'a'+'b'

list3=list1 + list2
print(list3)

print(list1*3) # three times repeat - iterate

dir(list)

# we can delete whole list also

aList = [123, 'xyz', 'zara', 'abc']
del[aList]

##################################### Tuples ####################################
# we can concatinate but not append,extend and assigment operator or assign
## Create a tuple dataset 
tup1 = ('Street triple','Detona','Beneli', 8055)
tup2 = (1, 2, 3, 4, 5 )
tup1.extend(tup2) # error- tuple is immutable
tup1[0] = 'hjh' # not support assignment operator
# create a tuple dataset
tup1 = ()
tup1
#Create a single tuple
tup1 = (50,)
tup1 = (50)
type(tup1)

#Accessing Values in Tuples
tup1 = ('Street triple','Detona','Beneli', 8055,2+3j,False)
print(tup1[0]) # we can the find position

tup2 = (11, 12, 13, 14, 15, 16, 17 )
print(tup2[1:5]) # we can access the value

#Updating Tuples
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

#Tules are immutable
tup1[1]=40

s='sam dfg'
s[0]
s[0]='z' # string is also immutable so we can't change it
#but we can do by split
a =s.split()
a
a[0]='z'
a

# So,create a new tuple as follows - concatination
tup3 = tup1 + tup2
print(tup3)

#index, count
tup=(1,2,3,4,1,2) # index position
tup.index(1)

tup.count(2)

#Delete Tuple Elements - error - can't delete
del(tup) # whole tuple will delete
del(tup[0]) # we can not delete inside element of tuple
tup

############################## Dictionary #################################
# dictionary is mutable
#Accessing Values in Dictionary

dict1 = {'Name': 'Sharat', 'Age': 40, 'bike': 'Beneli'}

print(dict1)

print(dict1['Name'])

print(dict1['Age'])   

##Updating Dictionary
dict1 = {'Name': 'Nikhil', 'Age': 25, 'bike': 'Beneli'}

# update existing entry
dict1['Age'] = 27
dict1

# Add new entry
dict1['School'] = "DPS School"
dict1

dict1['sal'] = 50000
dict1

dict1.index("Name") # error='dict' object has no attribute 'index'

print(dict1['Age'])
print(dict1['School'])
print(dict1['sal'])

dict1.keys()
dict1.values()
dict1.items()

#Delete Dictionary Elements
dict1 = {'Name': 'Sharat', 'Age': 40, 'bike': 'Beneli'}

# remove entry with key 'Name'
del(dict1['Name'])
dict1
# delete entire dictionary
del(dict1) # whole dictiornary delete  or delete variable

# remove all entries in given dictionary
dict1.clear()
dict1

print(dict1['Age']) # delete = no shown
print(dict1['School'])

#Dictionary inside another dictionary
d = {'k':123,'k2':[8,9,10],'k3':{'inside_key':100}}
d
d['k']
d['k'] = [8,9,10]
d
d['k2']
d['k2'][1]
d['k3']['inside_key']
d['k2']= d['k'] # k value store in k2
d
c = {'k':123,'k2':(8,9,10),'k3':{'inside_key':100}} # k2 as tuple
c

############################## Sets #################################
#### sets are unordered collection of unique elements and do not allow 
# duplicate values
# Normal set is mutable, Frozen set is immutable
# A normal Set
#set' object does not support item assignment
normal_set={1,2,3}
normal_set={1,2,3,3} # it takes automatically single value if it repeats
normal_set
# addition in set
normal_set.add("d")
normal_set
# Remove from set
normal_set.remove(3)
normal_set
#Frozen set is immutable
frozen_set = set(["a","b","c","f"])
frozen_set
type(frozen_set)
# or you can define like below
frozen_set = set({"a","b","c","f"})
frozen_set
type(frozen_set)
frozen_set.add(88)
frozen_set

sets = {10,20,30,40}
sets.add(50)
sets
sets[1]=9 #error - 'set' object does not support item assignment
sets.remove(30)
sets
print(sets)
sets.append(89) # no append no extend
sets

sets = {10,20,30,40}
fr = frozenset(sets)
print(type(fr))
fr.add(50) # error - immutable
fr
fr.remove(30)  # error - immutable
fr

# converting list into set

my_list = [1,1,2,3,4,4,5,5,6,7]
my_set = set(my_list)
my_set


# find common in sets

set1 ={1,2,3}
set2 ={1,9,0}

seta = set1.intersection(set2)
seta

# converting set into list

intersection_as_list = list(seta)
print(intersection_as_list)


# Python3 program for union() function

set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {7, 8, 9, 10}

# union of two sets
print("set1 U set2 : ", set1.union(set2))

# we can store this in 1 variable
oo = set1.union(set2)
#Union of three sets
print("set1 U set2 U set3 :", set1.union(set2, set3))


####################Operators#########################3

#Arithmetic operators

#consider
a = 10
b = 20

#Addition
a + b

#subtraction
a - b

#Multiplication
a * b

#division 
a/b

#Floor Division
a//b

#Modules
b%a


#exponential
a**b 

#Comparision Operator

#It gives in bool values

a == b
 
a != b
 
a > b
 
a < b

a >= b

a <= b

#Assignment Operators

c = a+b

c

c += b  #its nothing but c = c+b
c
c -= b
c
c *= b
c
c /= b
c
c %= b
c
c **= b # 1e+20 - 10 to the power 20
c
c //= b
c

# multiple line single statement
x=(1+2
  +3+4)
x
x=1;y=2 # multiple statement single line -  assigning
x/y

print("hello");print("world") # print
x=1;y=2
x//y

x=-1;y=2
x//y #(gives output less than quotient)

#Membership Operators
# It will check that left value is a member of right value or not 

"y" in "Python"

"l" in "Python"

"p" in "Python"

"P" not in "python"

#Identity Operators
# It Check will check that left value is equal to the right value or not

"y" is "Python"

1 is 1

2 is 1

"python" is "Python"

1 is 0

1 is not 1

"hi hello"  is not  "hello hi"

################## Variables ##################### 
#Variable name should start with a letter 
#It should contain only alpha numerics
#It should not contain any other symbols except _

#Assigning Integer values to a variable 
car = 10
print(car)
type(car)

# indentation error -EOF - end of file
car 2s=20 # space - error
car_1=20
#Variable name should start with letter
#It can contain alphanumerics and underscore only
car 1=15

#Assigning decimal values to a variable 
wt = 60.25
print(wt)
type(wt)

#Assigning string value to variable    

new_car = 'cars'

String_Name = "Python string"

# Multiple Assignment

a = b = c = 34 # multiple assignment in single line

print(a)

print(b)

print(c)

a,b,c = 19,6.0,"I Love machine learning" # multiple assignment in single line
print(c)

# Integer values

a,b,c,d,e = 0,2,5,7,8


print(d)
print(a)
print(b)
print(e)
print(c)

new,old="iphone","MI"

print(new)
print(old)


# User assigning the value to variable using input function 

num_1 = input("hi, Enter a value =  ") # any value we can print in input

print ("you have entered ", num_1)

type(num_1)

# Restricting user input using int() function
  
age = int(input("enter the age = "))

print("your age is: ", age)

type(age)

# Restricting user input using int() and Float() function
num_1 = float(input("Enter a 1st value = "))
num_1
cnum_2 = int(input("Enter a 2nd value = "))
cnum_2
cnum_3 = complex(input("Enter a 2nd value = "))
cnum_3
results = num_1+num_2
print("final result", results)
type(results)

# Restricting user input using Float() and int() function, eval() helps us to evaluate according to user input
# even eval takes complex number also
# also boolean value
x = eval(input("enter the 1st value = ")) #int,float,complex,boolean but not str
x
type(x)
y = eval(input("enter the 2nd value = ")) # if we write true
results = x+y
print("final results = ",results)
type(results)

x= eval(input("enter the 2nd value = ")) # if we write true in x it means 1
x
y= eval(input("enter the 2nd value = "))
y
results = x+y #(True = 1, False = 0, 1+56=57, 0+56=56)
print("final results = ",results)

A = 33
A**(1/2) # square root
A**(1/3) # square cube
#Exponential in complex numver
A = 33+9j
A**(1/2) # square root
A**(1/3) # cube root

################################## Conditional Statement ####################################


# Example:1 - simple if and else conditions when you have  two  conditions

is_male = True

if is_male:
    print("you are male")
else:
    print("you are female")    

# Example: 2 - if you have more than two condition use elif 

#In the above example, the elif conditions are applied after the if condition. 
#Python will evalute the if condition and if it evaluates to False then it 
#will evalute the elif blocks and execute the elif block whose expression 
#evaluates to True. If multiple elif conditions become True, 
#then the first elif block will be executed.

is_male = True
is_tall = False 
# it will check every elif if 1st if is false
if is_male and is_tall: # and & not operator
    print("you are tall male")
elif is_male and not(is_tall):
    print("you are short male")
elif not(is_male) and is_tall:
    print("you are not male but tall")
else:
    print("you are not male and not tall")    
        
if is_male or is_tall:
  print(" you are male or a tall or both") ## or operator 

#Example:  3 - conditional inside a conditional 
### Nested if Statement
#it will not check next if they satisfied otherwise out of the condition 
score = 500
money = 2000
age = 65

if score > 100:
    print("You got good points")
    
    if money >= 5000: # from this it will out of the condition
        print("you win")
        
        if age >= 30:
            print("You win in middle age")
        else:
            print("You are win in young age")
    else:
        print("you have a high points but you do not have enough money")
        
else:
    print("your loser")

# 1st if is false it will out of the condition
if score < 100:
    print("You got good points")
    
    if money >= 5000: # from this it will out of the condition
        print("you win")
        
        if age >= 30:
            print("You win in middle age")
        else:
            print("You are win in young age")
    else:
        print("you have a high points but you do not have enough money")
        
else:
    print("your loser")

score = 500
money = 8000
age = 65

if score > 100:
    print("You got good points")
    
    if money >= 5000: # from this is true it will proceed
        print("you win")
        
        if age >= 30:
            print("You win in middle age")
        else:
            print("You are win in young age")
    else:
        print("you have a high points but you do not have enough money")
        
else:
    print("your loser")


#Example: 4
    
name = "human"
animalName = "dog"

if name == "animal": # if is not satisfied out of the conditon
    print("Name Entered is Animal")
    if animalName == "dog":
        print("valid Animal")
    else:
        print("animalName invalid")
else:
    print("the name entered is not valied")
    print ("your entered name is not a animal")
    
############################### Loops #########################

   
############### While Loop

#Example for 'While loop'

i=10
while i>0:
    print(i)
    i=i-1
    
i=1
while i<=10:
    print(i)
    i=i+1   
    
#GAME
random_number = int(20*5+5-10)

guess = 0

while guess != random_number: # if which i guess is equal to random number then jump to else statement
    guess = int(input("New Number: "))
    if guess > 0:
        if guess > random_number:
            print("number is too large")
        elif guess < random_number:
            print("number is too small")
    else:
        print("sorry that you are giveup!")
        break
else:
    print("Congratulations. YOU WON!")
    
    
# calss 
import random
n = 20
random_number = int(n * random.random())

guess = 0

while guess != random_number: # if which i guess is equal to random number then jump to else statement
    guess = int(input("New Number: "))
    guess = int(input("New Number: "))
    if guess > 0:
        if guess > random_number:
            print("number is too large")
        elif guess < random_number:
            print("number is too small")
    else:
        print("sorry that you are giveup!")
        break
else:
    print("Congratulations. YOU WON!")
    
# 20*0.1 = 2 (0.1 is a random number)

################ for Loop

#Example for 'for loop' 
#finite loops
#Example : 1
    
snacks = ['pizza','burger','shawarma','franky'] # either tuple,sets

for snack in snacks:
    print("current snack: ", snack)

#Example: 2

for i in range(10): # till 9 (n-1)
    print(i)
    
for i in range(1,15): # till 14 (n-1)
    print(i)
    
for i in range(1,20,2): # (start, end, step)
    print(i)    

#Ex 3
stock_prices = [['Apple',300],["samsung",400],["nokia",100]]
stock_prices

for items in stock_prices:
    print(items)
    
# if it is in dictionary

d = {'k1':1,'k2':2,'k3':3}

for item in d.items():
    print(item)

for key, value in d.items():
    print(key)
    print(value)  

#Nested Loops
#Nested 'for in for' and for in while will be asignments problems                       
#Nested while in for 

travelling  = input("yes or no: " )

while travelling == 'yes':
    
    num = eval(input("number of people travelling: " )) # if 3 means three times loop run   
    for num in range(1,num+1):
        name = input("Name: ")
        
        age = input("Age: ")
        
        sex= input("Male or Female: ")
        
        print(name)
        
        print(age)
        
        print(sex)
        
    travelling = input ("Oops! forgot someone: ")
  
############################### define function ##############################

#Example for advantage of functions 
    
#Imagine there are 1000 of code is created based on requirement without using functions 
# If same requirement is repeated in the same code as given below with reference of line numbers

print("Hello Function.Sharat?") #10
print("Hello Function.Sharat?")#14
print("Hello Function.Sharat?")#40
print("Hello Function.Sharat?")#67

#how to create function? 
def hello_func():
    i=4
    while i>0:
        print("Hello Function.Sharat")
        i=i-1
#call the function as and when required than writing whole code again 
hello_func()#10
       
#Advantages about functions - optimize code, good performance, 
#fast, easy to access etc
        
#simple function 
def hello(name,age,sal): # def func(Arguments)
    print("hi",name,"your age:",age,"your salary",sal)
    
hello("Sharat",25,50000)    
        
#add two numbers using return value 
def add(x,y,z):
    return(x-y+z)

add(10,20,50)

def add(x):
    return (x**3)
var = (1,2,3,4)
list(map(add,var))

#cube of n value 
def cube(num):
    return(num*num*num)
cube(3)

def even_check(number):
    if(number%2 == 0):
        print('given number is even')
    else:
        print("given number is odd")

even_check(5)

# not defined any value but just defined function

def odd(list1):
    for num in list1:
        if num%2==0:
            pass
        else:
            print(num)

list1=[1,2,3,4,5,6]
odd(list1)


########
def myfunc(a,b,c =0,d =0, e = 0):
    return sum((a,b,c,d,e))*0.05

myfunc(10,20,30,40,50)
myfunc(40,60) # returns 5% of the sum of a and b

# Defining the lambda function , map ,reduce
# lambda arguments: expressions
s = lambda x: x * x #ananomous function - not giving any name
s
s(12)

val = [1, 2, 3, 4, 5, 6]

S1 = list(map(lambda x: x * 2, val))
S1[1]
S1[2]

# Functional Programming Packages
val = [1, 2, 3, 4, 5, 6]

list(map(lambda x: x * 2, val)) # map for iteration like for 
list(map(lambda x: x * 2, (3,5,6,7))) # use tuple also
map(lambda x: x * 2, (3,5,6,7)) # not taking
Ruby = (1,4,5,6) # or you can give list,set,tuple any thing
tuple(map(lambda x: x * 2, Ruby)) # if you want your reuslt as tuple
set(map(lambda x: x * 2, Ruby))
c = lambda x,y,u,i,p: x**2+y*p/u-i
'''x = 2
y = 3
u = 4
i = 5
p = 8'''
print(c(2,3,4,5,6))

def add(x): # only for single argument otherwise error
    return (x**3)
var = (1,2,3,4)
list(map(add,var))
############################# Modules ################################

# Modules are also called as packages 
# how to call package is : Import package_name
    
#Example:1

#maths related package
import math
# pip means - Preferred installer Program
math.sqrt(16) # square root

math.pow(2,5) # 2 to the power 5

dir(math)

#Example:2

#calendar related package










