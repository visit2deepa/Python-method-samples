Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #if else examples 10
>>> #write a program whether person is eligible for voting or not
>>> age=int(input("Enter an age"))
Enter an age 20
>>> if(age>=18):    
...     print("Eligible for voting")
... else:
...     print("Not Eligible for voting")
... 
...     
Eligible for voting
>>> #################################################################
>>> #Check whether number is divisible by
>>> #Check whether number is divisible by 7
>>> num=int(input("Enter a number"))
Enter a number 23
>>> if(num%7==0):
...     print("number is divisible by 7")
... else:
...     print("number is not divisible by 7")
... 
...     
number is not divisible by 7
>>> ###################################################################
#write a program to calculate electricity bill(accept the number of units from user)according to following criteria 
E.g. Fort 1st 100 units, no charge; For next 100 units, rs 5 per unit; After 200 units, Rs 10 per unit
(if input is 350 then total bill Rs 2000)

bill=0
num=int(input("Enter an unit"))
Enter an unit 300
if num<=100:
    bill=0
elif num>100 and num<=200:
    bill=(num-100)*5
elif num>200:
    bill=500+(num-200)*10
    print("Amount to pay: ",bill)
----------------------------------------------------------------------------------------------------------
