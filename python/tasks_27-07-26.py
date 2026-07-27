#27-07-2026 tasks

'''task h/w-1
    *
   *** 
  *****
 *******
 '''
'''Task h/w -2  
1
12
123
1234
'''

''' task-3
1
23
456
78910
'''

'''
task h/w-4
1234
123
12
1
'''

'''
task h/w-5
AAAAA
ABBBA
ABBBA
ABBBA
AAAAA
'''

'''task h/w-1
    *
   *** 
  *****
 *******
 '''
#Solution
rows = 4

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ",end="")
    for k in range(2 * i - 1):
        print("*",end="")
            
    print()

'''Task h/w -2  
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

''' task-3
1
23
456
78910
'''
#Solution
num = 1
for i in range(1,5):
    for j in range(i):
        print(num,end="")
        num+=1
    print()

'''
task h/w-4
1234
123
12
1
'''
#Solution
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()    

'''
task h/w-5
AAAAA
ABBBA
ABBBA
ABBBA
AAAAA
'''
#solution
#M-1
for i in range (1 ,6):
    if i==1 or i==5:
        print("AAAAA",end="")
    else:
        print("ABBBA",end="")
    print()

#M-2
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("A",end="")
        else:
            print("B",end="")
    print()
