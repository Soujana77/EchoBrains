#function to odd or even
def check_odd_even(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
print(check_odd_even(10))
print(check_odd_even(7))

#Function to find Largest Number
def largest(a,b):
    if a>b:
        return a
    else:
        return b
print(largest(10,20))

#Function With a Loop
def print_numbers(n):
    for i in range(1,n+1):
        print(i)
print_numbers(5)

#Function Calling another Function
def square(n):
    return n*n
def cube(n):
    return square(n)*n
print(cube(3))
