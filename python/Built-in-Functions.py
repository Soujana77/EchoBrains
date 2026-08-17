#Built-in Functions
#Without len():
word = "Python"
count = 0

for i in word:
    count += 1

print(count)

#Using the built-in function:
word = "Python"

print(len(word))

#Some Important Built-in funtions
'''
print()-display ouput
input()-take input
len()-find Length
type()-find data type
int()-convert to integer
float()-Convert to float
str()	Convert to string
bool()	Convert to Boolean
sum()	Calculate total
max()	Find maximum
min()	Find minimum
abs()	Absolute value
round()	Round a number
sorted()	Sort values
range()	Generate a sequence
enumerate()	Get index + value
zip()	Combine iterables
'''

name = input("Enter your name: ")

print(name)

#print()
print("Hello")

#len()
word = "Python"
print(len(word))

#Type Conversion Functions
x = "100"
y = int(x)
print(y)
print(type(y))

#--------------
x = "10.5"
print(float(x))

#---------------
x = 100
print(str(x))

#---------------
x = 10
print(bool(x))

#---------------
numbers = [10, 20, 30, 40]
print(sum(numbers)) #Used to find the total of numbers.

#---------------
numbers = [10, 50, 20, 80, 30]
print(max(numbers)) #finds the largest value


#---------------
numbers = [10, 50, 20, 80, 30]
print(min(numbers))#finds the smallest value

#---------------
print(abs(-10)) #Returns the absolute value o/p = 10

#---------------
x = 10.5678
print(round(x))#Used to return numbers 

#---------------
numbers = [5, 2, 8, 1, 3]
print(sorted(numbers)) #Used to sort values 

#range()
for i in range(5):
    print(i)

#enumerate()
names = ["Soujanya", "Anu", "Rahul"]
for i in range(len(names)):
    print(i, names[i])

for index, name in enumerate(names):
    print(index, name)

#zip()
names = ["Soujanya", "Anu", "Rahul"]
marks = [90, 85, 95]

for name, mark in zip(names, marks):
    print(name, mark)

#any()
numbers = [1, 3, 5, 8]
print(any(x % 2 == 0 for x in numbers))

#all()
numbers = [2, 4, 6, 8]
print(all(x % 2 == 0 for x in numbers))

#id()
x=10
print(id(x)) #Returns the identity of an object.

#isinstance()
x = 10
print(isinstance(x,int))#Checks whether something belongs to a particular data type.
