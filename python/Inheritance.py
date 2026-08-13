#Single inheritance
'''
class A():
    def __init__(self):
        print("con1")
class B(A):
        def __init__(self):
            super().__init__()
        print("con2")
obj=B(A)        

#Multilevel inheritance
class A():
    def __init__(self):
        point("con1")
class B(A):
    def __init__(self):
        super().__init__()
        print("con2")
class C(B):
    def __init__(self):
        super().__init__()
        print("con3")
obj=C()


#Multiple inheritance
class A():
    def __init__(self):
        print("con1")
class B():
    def __init__(self):
        super().__init__()
        print("con2")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("con3")
obj=B()

#Hirarchial Inheritance
class A():
    def __init__(self):
        print("con1")
class B(A):
    def __init__(self):
        super().__init__()
        print("con2")
class C(A):
    def __init__(self):
        super().__init__()
        print("con3")
obj=B()

#Hybrid Inheritance
class A():
    def __init__(self):
        print("con1")
class B(A):
    def __init__(self):
        super().__init__()
        print("con2")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("con3")
obj=B()



#Single inheritance program example
class s_marks():
    def __init__(self):
        print("Marks of s")
class m_marks(s_marks):
    def __init__(self):
        super().__init__()
        print("Marks of m")       
obj= m_marks(s_marks)

#Multilevel inheritance program example
class s_marks():
    def __init__(self):
        print("Marks of S")
class m_marks(s_marks):
    def _init__(self):
        super().__init__()
        print("Marks of S")
class p_marks(m_marks):
    def __init__(self):
        super.__init__()
        print("Marks of P")
obj=p_marks(s_marks)

#Multiple Inheritance
class s_marks():
    def __init__(self):
        print("Marks of S")
class m_marks(s_marks):
    def _init__(self):
        super().__init__()
        print("Marks of S")
class p_marks(s_marks,m_marks):
    def __init__(self):
        super.__init__()
        print("Marks of P")
obj=p_marks(s_marks)


class A():
    def __init__(self):
        print("Hello world")
class B(A):
    def __init__(self):
        super.__init__()
        print("Hello world"*2)

obj=B(A)
'''
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


d = Dog()

d.eat()    # inherited from Animal
d.bark()   # Dog's own method


#Single inheritance
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


d = Dog()

d.eat()
d.bark()

#Multiple inheritance
class Father:
    def house(self):
        print("Father has a house")


class Mother:
    def car(self):
        print("Mother has a car")


class Child(Father, Mother):
    def bike(self):
        print("Child has a bike")


c = Child()

c.house()
c.car()
c.bike()

#Multilevel Inheritance
class Grandfather:
    def house(self):
        print("Grandfather has a house")


class Father(Grandfather):
    def car(self):
        print("Father has a car")


class Son(Father):
    def bike(self):
        print("Son has a bike")


s = Son()

s.house()
s.car()
s.bike()

#Hirarchial Inheritance
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()

#Hybrid inheritance
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Cat(Animal):
    def meow(self):
        print("Meowing")


class Pet(Dog, Cat):
    def play(self):
        print("Playing")


p = Pet()

p.eat()
p.bark()
p.meow()
p.play()
        
 
