#Create a generator program that generates numbers from 1 to 10 
def numbers():
    for i in range(1,11):
        yield i
for num in numbers():
    print(num)

#Real world example of generator
def get_orders():
    orders = []

    for i in range(1, 1000001):
        orders.append(f"Order-{i}")

    return orders

#Create a generator function that generates even numbers from 1 to 20
def even_numbers():
    for i in range(0,21,2):
        yield i
for num in even_numbers():
    print(num)

#Create a generator that generates the square of numbers from 1 to 10
def sq_nums():
    for i in range(1,11):
        yield i*i
for num in sq_nums():
    print(num)
    
