#A function is a reusable block of code that performs a particular task.
#def function_name():
    # code

#example program-1
def greet():
    print("Hello Soujanya")
    print("Welcome to python")
greet()

#example program-2
def hello():
    print("Hello")
hello()

#Function with Parameters
def greet(name):
    print("Hello",name)
greet("Soujanya")
greet("Rahul")
greet("Anu")

#Parameter vs Argument
#Parameter → variable in the function definition
#Argument → actual value passed when calling the function
def greet(name):       # name → parameter
    print("Hello",name)
greet("Soujanya")      #"Soujanya"->argument

#Multiple Parameters
#example program-1
def add(a, b):
    print(a + b)
add(10, 20)

#example program-2
def student(name, age, branch):
    print("Name:", name)
    print("Age:", age)
    print("Branch:", branch)

student("Soujanya", 21, "CSE")

#return
#example program-1
def add(a, b):
    print(a + b)

result = add(10, 20)
print(result)

#Function With Parameters + Return
def multiply(a, b):
    result = a * b
    return result

answer = multiply(5, 4)

print(answer)

#Default Parameters
def greet(name="Soujanya"):
    print("Hello", name)
greet()    
