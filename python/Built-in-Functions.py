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

#---------------
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
print(sum(numbers))
