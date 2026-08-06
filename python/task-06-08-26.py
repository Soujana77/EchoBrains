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

c=65
for i in range(6):
    for j in range(i):
        print(chr(c))
        c+=1


    
    
