"Name: Shahina Athar"
"Batch Id: 10122020"
"MODULE-1"
"""ASSIGNMENT-1 Data Types"""

#Please implement by using Python.
#1.	Construct 2 lists containing all the available data types  (integer, float, string, complex and Boolean) and do the following..
#a.	Create another list by concatenating above 2 lists
#b.	Find the frequency of each element in the concatenated list.
#c.	Print the list in reverse order.

List1 = ["Shahina",12,2.0,2+7j,True]
List2 = ["Athar",13,3.0,3+6j,False]

#a.concatenating above 2 lists

List3 = List1 + List2
List3

#b.frequency of each element in the concatenated list

len(List3)

#c.Print the list in reverse order

List3.reverse()
List3

#2.	Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in other set)
#a.	Find the common elements in above 2 Sets.
#b.	Find the elements that are not common.
#c.	Remove element 7 from both the Sets.

#a.	Find the common elements in above 2 Sets.

Set1 = {1,2,3,4,5,6,7,8,9,10}
Set2 = {5,6,7,8,9,10,11,12,13,14,15}

Set3 = Set1.intersection(Set2)
Set3

#b.	Find the elements that are not common

Set4 = Set1 ^ Set2
Set4

#c.Remove element 7 from both the Sets.

Set1.remove(7)
Set1
Set2.remove(7)
Set2

#3.	Create a data dictionary of 5 states having state name as key and number of covid-19 cases as values.
#a.	Print only state names from the dictionary.
#b.	Update another country and it’s covid-19 cases in the dictionary.

#a.	Print only state names from the dictionary.

Dictionary1 = {"Maharashtra": 100, "Telangana": 200, "Uttar Pradesh": 300,
                   "Himachal Pradesh": 400, "Bihar": 500}
Dictionary1
Dictionary1.keys()

#b.Update another country and it’s covid-19 cases in the dictionary.

Dictionary1["America"] = 240925
Dictionary1


"MODULE-2 OPERATORES"

#Please implement by using Python
#1.	A. Write an equation which relates   399, 543 and 12345 
#B.  “When I divide 5 with 3, I got 1. But when I divide -5 with 3, I got -2”—How would you justify it.

#1.	A. Write an equation which relates   399, 543 and 12345 

x = 12345
y = 543
z = 399
print(x//y)
print(x%y)

print('''Answer(a)-so the relation is "x = 22y+z" , so 12345%543 =399 ''')

#B.  “When I divide 5 with 3, I got 1. But when I divide -5 with 3, 
#I got -2”—How would you justify it.

a = 5
b = 3
c = a//b # 1.666 = 1 (round off)
c
# while doing minus of it it's taking it's approximate or you can say rounding off.
#This happens because , it rounds the result(quotient) to nearest integer that is 
#less than the result and 1 is less than 1.66 where -2 is less than -1.66
e = -5
f = e//b # -1.666 = -2 (round off)
f


#2.  a=5,b=3,c=10.. What will be the output of the following:

#A. a/=b

a = 5
b = 3
c = 10
a/=b
a

#B. c*=5  

c*=5 
c

#3. A. How to check the presence of an alphabet ‘s’ in word “Data Science” .

word = "Data Science"

"S" in "Data Science"

#B. How can you obtain 64 by using numbers 4 and 3 .

4**3

"MODULE 3 Variables"

#1.	What will be the output of the following (can/cannot):
#a.	Age1=5

Age1 = 5
Age1

#b.	5age=55

5age = 55 # error we can  not write variable which is start from numeric values
5age

#2.	What will be the output of following (can/cannot):
#a.	Age_1=100

Age_1=100
Age_1

#b.	age@1=100

age@1=100 # error 
age@

#3.	How can you delete variables in Python ?

#To delete a variable, it uses keyword "del"

"MODULE-4 Conditional Statements"

#Please write Python Programs for all the problems .
#1.	 Take a variable ‘age’ which is of positive value and check the following:
#a.	If age is less than 10, print “Children”.
#b.	If age is more than 60 , print ‘senior citizens’
#c.	 If it is in between 10 and 60, print ‘normal citizen’

age = int(input("What is your age: "))

if age < 10:
    print("You are Children")
elif age > 60:
    print("You are Senior Citizen")
else:
    print("You are Normal Citizen")    

#2.	Find  the final train ticket price with the following conditions. 
#a.	If male and sr.citizen, 70% of fare is applicable
#b.	If female and sr.citizen, 50% of fare is applicable.
#c.	If female and normal citizen, 70% of fare is applicable
#d.	If male and normal citizen, 100% of fare is applicable
#[Hint: First check for the gender, then calculate the fare based on age factor.. 
#For both Male and Female ,consider them as sr.citizens if their age >=60]

gender = input("What is your gender: ")
age = int(input("What is your age: "))
if gender == "Female" and age < 60:
    print("train ticket price is 70% of fare is applicable for Female and normal citizens")
elif gender == "Male" and age < 60:
    print("train ticket price is 100% of fare is applicable for Male and normal citizens")
elif gender == "Female" and age >= 60:
    print("train ticket price is 50% of fare is applicable for Female and Senior citizens")
else: 
    print("train ticket price is 70% of fare is applicable for Male and Senior citizens")

#3.	Check whether the given number is positive and divisible by 5 or not.  

X = int(input("Enter a number:"))

if X > 0 and X%5 == 0:
    print("The given number is positive and divisible by 5 ")
else:
    print("Not")    
   
"MODULE 5 LOOPS and Functions"

#Please implement Python coding for all the problems.

#1.	A) list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters exists in list1.
#B) How do we create a sequence of numbers in Python.
#C)  Read the input from keyboard and print a sequence of numbers up to that number

#1.	A) list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters exists 

list1 = [1,5.5,(10+20j),"data science"]
list1

def defun(list1):
    for i in list1:
        print(i)

defun(list1)    
    
#B) How do we create a sequence of numbers in Python.

x = range(10)
for i in x:
    print(i)
    
#C)  Read the input from keyboard and print a sequence of numbers up to that number

A = int(input("Enter number: "))

for i in range(0,A):
    print(i)

#2.	Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
#list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
#Create a dictionary such that list2 are keys and list 1 are values..

list1=[0,1,2,3,4,5,6,7,8,9]
list2=['zero','one','two','three','four','five','six','seven','eight','nine']

#we'll use zip function to make lists to dictionary.

mydict = dict(zip(list2 , list1))
mydict

#here list_2 is keys and list_1 is variable.
#3.Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10 to the even number
# and multiply with 5 if it is odd number in the list1..

list1 = [3,4,5,6,7,8]
list2 = []
for i in list1:
    if i%2 == 0:
        list2.append(i + 10)
    else:
        list2.append(i*5)
list2        

#4. Write a simple user defined function that greets a person in such a way that :
#i) It should accept both name of person and message you want to deliver.
#ii) If no message is provided, it should greet a default message ‘How are you’
#Ex: Hello ---xxxx---, How are you  - default message.
#Ex: Hello ---xxxx---, --xx your message xx---

def greets(name,message = "How are you?"):
    print(f'Hello {name}, {message}')
    
greets("Shahina")

#Here "How are you " is default message when we dont give any message.

greets("Shahina","What's your Plan Today")

#here when we give some message by user..so both can access this.

"MODULE 6 PACKAGES"

#Implement in Python
#1.	For the dataset “Indian_cities”, 
#a)	Find out top 10 states in female-male sex ratio
#b)	Find out top 10 cities in total number of graduates
#c)	Find out top 10 cities and their locations in respect of  total effective_literacy_rate.

import numpy as np
import pandas as pd

df = pd.read_csv("D:/C DRIVE-SSD DATA backup 15-12-2020/Desktop/360digitmg material/Python Assignment/Python Problem Statements/Indian_cities.csv")
df

df.columns

#a)	Find out top 10 states in female-male sex ratio

sexratio = df[["state_name", "sex_ratio"]].sort_values(by = 'sex_ratio', ascending = False).head(10)
sexratio

#b)	Find out top 10 cities in total number of graduates

total_graduates = df[["name_of_city", "total_graduates"]].sort_values(by = 'total_graduates', ascending = False).head(10)
total_graduates

#c)	Find out top 10 cities and their locations in respect of  total effective_literacy_rate.

effective_literacy_rate_total = df[["name_of_city","location","effective_literacy_rate_total"]].sort_values(by = "effective_literacy_rate_total", ascending = False).head(10)
effective_literacy_rate_total

#2.	For the data set “Indian_cities”
#a)	Construct histogram on literates_total and comment about the inferences
#b)	Construct scatter  plot between  male graduates and female graduates

#a)	Construct histogram on literates_total and comment about the inferences

import matplotlib.pyplot as plt
plt.hist(df.literates_total)

#By seeing the above graph we conclude that it is right skewness or positive skewness and it is asymmetry in shape.

#b)	Construct scatter  plot between  male graduates and female graduates

plt.xlabel("male graduates")
plt.ylabel("female graduates")
plt.scatter(df.male_graduates, df.female_graduates, color = 'r')

#3.	For the data set “Indian_cities”
#a)	Construct Boxplot on total effective literacy rate and draw inferences
#b)	Find out the number of null values in each column of the dataset and delete them.

#a)	Construct Boxplot on total effective literacy rate and draw inferences

plt.boxplot(df.effective_literacy_rate_total)

#b)	Find out the number of null values in each column of the dataset and delete them.

df.isnull().sum()

#there are no null values present in the dataset.

                          "Thank You"




