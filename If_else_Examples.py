Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#if else examples 10
#write a program whether person is eligible for voting or not
age=int(input("Enter an age"))
Enter an age 20
if(age>=18):    
    print("Eligible for voting")
else:
    print("Not Eligible for voting")

    
Eligible for voting
#################################################################
#Check whether number is divisible by
#Check whether number is divisible by 7
int num=(input("Enter a number"))
SyntaxError: invalid syntax
num=int(input("Enter a number"))
Enter a number 23
if(num%7==0)
SyntaxError: expected ':'
if(num%7==0):
    print("number is divisible by 7")
else:
    print("number is not divisible by 7")

    
number is not divisible by 7
###################################################################
#write a program to calculate electricity bill(accept the number of units from user)according to following criteria E.g. Fort 1st 100 units, no charge; For next 100 units, rs 5 per unit; After 200 units, Rs 10 per unit(if input is 350 then total bill Rs 2000)
bill=0
num=int(input("Enter an unit"))
Enter an unit 200
if(num<=100):
    amt=
    
SyntaxError: invalid syntax
bill=0
num=int(input("Enter an unit"))
Enter an unit  300
if num<=100:
    bill=0

    
bill=0
num=int(input("Enter an unit"))
Enter an unit  300
if num<=100:
    bill=0
    
SyntaxError: multiple statements found while compiling a single statement
bill=0
num=int(input("Enter an unit"))
Enter an unit 300
if num<=100:
    bill=0
elif num>100 and num<=200:
    bill=(num-100)*5
elif num>200:
    bill=500+(num-200)*10
    print("Amount to pay: "+bill)

    
Traceback (most recent call last):
  File "<pyshell#40>", line 7, in <module>
    print("Amount to pay: "+bill)
TypeError: can only concatenate str (not "int") to str
###########################################################
#Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700
n=[]
for x in range(1500,2701):
    if (x%7==0) and (x%5==0):
        n.append(str(x))
print(','.join(n))
SyntaxError: invalid syntax
>>> 
>>> n=[]
>>> for x in range(1500,2701):
...     if(x%7==0)and (x%5==0):
...         n.append(str(x))
... 
...         
>>> print(','.join(n))
1505,1540,1575,1610,1645,1680,1715,1750,1785,1820,1855,1890,1925,1960,1995,2030,2065,2100,2135,2170,2205,2240,2275,2310,2345,2380,2415,2450,2485,2520,2555,2590,2625,2660,2695
>>> ########################################################################
>>> #Write a Python program to count the number of even and odd numbers in a series of numbers E.g Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> numbers=[1,2,3,4,5,6,7,8,9]
>>> num_odd=0
>>> num_even=0
>>> for x in numbers:
...     if(x%2==0):
...         num_even+=1
...     else:
...         num_odd+=1
... 
...         
>>> print("count of even numbers:",num_even)
count of even numbers: 4
>>> print("count of odd numbers:",num_odd)
count of odd numbers: 5
