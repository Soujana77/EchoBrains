#Conditional statements
#1.if
'''
if condition:
    statement
'''    
age=int(input("Enter your age:"))
if age>=18:
    print("you are 18+")
else:print("bye")

#2.else
'''
else:
    statement
'''
#program to check whether a numer is odd or even
num=int(input("Enter a number: "))
if num%2!=0:
    print("the number is odd")
else:print("the number is even")    

#program to check whether a numer is positive, negative or zero

num=int(input("Enter a number: "))
if num>0:
    print("the number is positive")
if num<0: #elif num<0:
    print("the number is negative")
else:
    print("The number is zero")

'''
in the above program we have used multiple if statements which is a drawback because , if we mention if it is mandatory to check all the ifs' in the program so we have to use elif'''


   
#program to check whether a numebr is divisible by both 3 and 7

a=int(input("enter a number: "))
if a%3==0 and a%7==0:
    print("yes the given number is divisible by both 3 and 7")
else:
    print("no the number not divisible by either 3 or 7 or both")

     
#nested if statement
'''
if condition:
   statement
   if condition:
      statement
   else: 
else:statement
'''
b=int(input("enter a number"))

      


           
