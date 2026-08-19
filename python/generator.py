#Generator
def add():
    return 1 #this does nt remember 
    return 2
    return 3
a=add()
print(a)
print(a)
#-----------------
def add():
    yield 1 #give one value , dont stop , remeber what is the nexr value 
    yield 2
    yield 3
a=add()
print(next(a))
print(next(a))
print(next(a))

