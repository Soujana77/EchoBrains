#Example 1
class father():
    def age(self):
        print("i'm 50")
class son(father):
    def age(self):
        print("i'm 50")
obj=son()
obj.age()

#Example 2 
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


d = Dog()
d.sound()

#Example 3
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog says Bow Bow")
class Cat(Animal):
    def sound(self):
        print("Cat says Meow")
d = Dog()
c = Cat():

d.sound()
d.sound()

#Example 4
class Student:
    def __init__(self):
        print("Student constructor")

class CollegeStudent(Student):
    def __init__(self):
        print("College Student constructor")

s = CollegeStudent()

#Example 5
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()
