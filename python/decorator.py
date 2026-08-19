#Decorator
#Basic syntax of decorator 
def add_choco(func):
    def wrapper():
        print("adding chocolate")
        func()
    return wrapper

@add_choco
def ice_cream():
    print("Venilla ice cream")
ice_cream()


#Example-2
def decorator(func):
    def wrapper():
        print("Starting...")
        func()
        print("finished...")
    return wrapper
def greet():
    print("Hello")
greet = decorator(greet)
greet()

'''
instead of using
def greet():
    print("hello")
greet = decorator(greet)

python gives us a much easier way to write this
we can write this as
@decorator
def greet():
    print("hello")
greet()
'''
