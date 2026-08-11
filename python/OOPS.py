'''
OOPS is a programming paradigm based on the
concept of objects.
Objects represant real-world entities
(like a car, bank account, or student).

It helps in :
Organizing code better
Reusing code(Inheritance)
Securing data(encapsulation)
Handling complexity(abstraction , polymorphism
'''
#syntax
class class_name():
    #methods
#create objects to access class

class A():
    def fun(): #this is a method , a method is dependent on class , but function is indepnedent
        print("Hello")
#Functions inside the class is called method
#To create an object , take any variable and assign class_name to it
obj=A()
obj.fun()

#Using pass we can create an empty class
#self is a keyword that says there is a relationship b/w a class and a method 
class B():
    def add(self,a,b):
        print("Addition=",a+b)
    def sub(self,a,b):
        print("Subtraction=",a-b)
obj1=B()
obj1.add(11,11)
obj1.sub(9,9)



        
        
    
