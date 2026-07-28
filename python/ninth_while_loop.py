#WHILE LOOP
'''
while condition :
    statement
'''

'''
a="hello"
while a==a:
    print("hi")
    a="a"

a=1
while a<=5:
    print(a)
    a+=1

    
a=5
while a>=0:
    print(a)
    a-=1
'''
'''
#Print numbers from 0 to 5
num=0
while num<= 5: #0<=5=T,1<=5-T
    print(num)#0,1
    num+=1

#ask the same question until the desired answer does not come
a=""
while a!="python":
    a=input("which is the best programing language?")
print("Correct")        

#5 Tables using while loop
i = 1

while i<= 10:
    print("5 x", i, "=", 5 * i)
    i += 1


#Print the odd numbers between 1 to 10 using while loop

i = 1
while i <=10:
    if i%2!=0:
        print("the odd the numbers are " ,i)
        i+=1
        
#square pattern using *
n = 1
while(n<=5):
    print(5*" *")
    n+=1
'''
#print hallow square from * using while loop
i=0
while i<=5:
    j=0
    while j<=5:
        if i==0 or i==5 or j==0 or j==5:
            print("*",end="")
        else:
            print("2",end="")
        j+=1
    i+=1
    print()

        
i=0
while i<=6:
    j=0
    while j<=6:
        if i==0 or i==3 or i==6 or i==j or j==0 or j==3 or j==6 or j+i==6:
            print(" *",end="")
        else:
            print(" 2",end="")
        j+=1
    i+=1
    print()


#1. Print 5, 4, 3, 2, 1, 0 using while
i = 5

while i >= 0:
    print(i)
    i = i - 1

#2. Print the table of 5 using while
i = 1

while i <= 10:
    print("5 X", i, "=", 5 * i)
    i = i + 1

#3. Print numbers from 1 to 10, but even numbers should say "Hi I am"
i = 1

while i <= 10:

    if i % 2 == 0:
        print("Hi I am", i)
    else:
        print(i)

    i = i + 1
    
#4. Print the rectangle using while
#method-1    
row = 1

while row <= 4:

    if row == 1 or row == 4:
        print("****")
    else:
        print("*  *")

    row = row + 1

#method-2
row = 0

while row < 4:

    col = 0

    while col < 4:

        if row == 0 or row == 3 or col == 0 or col == 3:
            print("*", end="")
        else:
            print(" ", end="")

        col = col + 1

    print()

    row = row + 1
'''
Task 1

Output:

   *
  ***
 *****
*******
'''
rows = 4
i = 1

while i <= rows:
    spaces = rows - i
    while spaces > 0:
        print(" ", end="")
        spaces -= 1

    stars = 1
    while stars <= (2 * i - 1):
        print("*", end="")
        stars += 1

    print()
    i += 1

'''
Task 2

Output:

1
12
123
1234
'''
i = 1

while i <= 4:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1
'''
Task 3

Output:

1
23
456
78910
'''
num = 1
i = 1

while i <= 4:
    j = 1
    while j <= i:
        print(num, end="")
        num += 1
        j += 1
    print()
    i += 1

'''
Task 4

Output:

1234
123
12
1
'''
i = 4

while i >= 1:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i -= 1

'''
Task 5

Output:

AAAAA
ABBBA
ABBBA
ABBBA
AAAAA
'''
i = 0

while i < 5:
    j = 0
    while j < 5:
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("A", end="")
        else:
            print("B", end="")
        j += 1
    print()
    i += 1
    
