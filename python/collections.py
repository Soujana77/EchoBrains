#string is the collection of characters and number denoted with single quotes or double quotes 
#strings are immutable
'''
a="Hello"
print(a.upper())

a="Hello"
print(a.lower())

a="Hello"
print(len(a))

a="Hello"
print(a.count("l"))

#string inbuilt functions

#slicing a string
a="hello i'm 'agent'"
'''
'''
syntax
var[start:stop:step]
'''
'''
print(a[::]) #prints the whole string as o/p
print(a[:]) #prints the whole string as o/p

print(a[::-1]) #reversing the string

#negative indexing left to right



#Lists-it is a collection different elements 
l=[]
print(type(1))

a=list()
print(type(a))

lis=[1,"hi",true,3.0]
print(lis)
lis[1]=2
print(lis[3])#print(lis[-1])
'''
#list inside a list
b=[1,"hello",False,[10,[8,9,6],20],3.0]

print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[-1])
print(b[-2])
print(b[-3])
print(b[-4])
print(b[-5])
print(b[3][0])
print(b[3][1])
print(b[3][2])
print(b[3][1][0])
print(b[3][1][1])
print(b[3][1][2])

#sum of numbers given by user
#Square the list using for loop
#filter the list with even numbers only ,which were squared before
#filter the list with odd numbers only ,which were squared before

#sum of numbers given by user
#solution
num = int(input("Enter a number: "))

sum = 0

for i in range(num, 0, -1):
    sum = sum + i

print("Sum =", sum)    
    
#Square the list using for loop
#solution
l=[1,2,3,4,5,6,7,8,9,10]

square_list=[]

for i in l:
    square_list.append(i*i)
print(square_list)

#filter the list with even numbers only ,which were squared before
#solution
even_numbers=[] 
for j in square_list:
    if j%2==0:
       even_numbers.append(j)
print(even_numbers)

#filter the list with odd numbers only ,which were squared before
#solution
odd_numbers=[]
for k in square_list:
    if k%2!=0: #when i tried this i came to know that i can use the same variable or change the variable in for loop to print odd and even separately
        odd_numbers.append(k)
print(odd_numbers)        


      





