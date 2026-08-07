#Tasks
'''
print the following pattern using for loop
A
AB
ABC
ABCD
'''

for i in range(6):
    c=65
    for j in range(i):
        print(chr(c),end="")
        c+=1
    print()
'''
print the following pattern using for loop   
A
BC
DEF
GHIJ
KLMNO
'''
c=65
for i in range(6):
    for j in range(i):
        print(chr(c),end="")
        c+=1
    print()


'''
print ABCDEFGHIJKLMNO one by one
'''
c=65
for i in range(6):
    for j in range(i):
        print(chr(c))
        c+=1

'''
print the following pattern using for loop
1
12
123
1234
'''

'''
print these patterns using for and while loop both
1
22
333
4444
55555

55555
4444
333
22
1

AAAAAA
ABBBBA
ACCCCA
ADDDDA
AAAAAA
'''

'''
print the following pattern using for loop
1
12
123
1234
'''
#Solution
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()    
'''
print the following pattern using while loop
1
12
123
1234
'''
#solution
i=1
while i<=4:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1
'''
print this pattern using for and while loop both
1
22
333
4444
55555    
'''
#solution using for
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()

#Solution uisng while
i=1
while i<=5:
    j=1
    while j<=i:
        print(i,end="")
        j+=1
    print()
    i+=1
'''
print this pattern using for and while loop both
55555
4444
333
22
1    
'''
#Soution using for
for i in range(5, 0, -1):
    for j in range(i):
        print(i, end="")
    print()

#Solution using while
i = 5

while i >= 1:
    j = 1
    while j <= i:
        print(i, end="")
        j += 1
    print()
    i -= 1
'''
print this pattern using for and while loop both
AAAAAA
ABBBBA
ACCCCA
ADDDDA
AAAAAA
'''
#Solution using for loop
for i in range(1,6):
    for j in range(1,7):
        if i==1 or i==5 or j==1 or j==6:
            print("A",end="")
        else:
            print(chr(64+i),end="")
    print()

#Solution using while loop
i = 1
while i <= 5:
    j = 1
    while j <= 6:
        if i == 1 or i == 5 or j == 1 or j == 6:
            print("A", end="")
        else:
            print(chr(64 + i), end="")
        j += 1
    print()
    i += 1    

    

