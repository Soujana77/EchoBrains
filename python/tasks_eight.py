#task-1
'''
    create a sample login program
    store
    username='admin'
    password='python123'
    Ask the user to enter the username and passwsord
    if the username is correct
    check the password
    if correct print "login successful"
    otherwise print "Incorrect password"
    if the username is incorrect print "invalid Username"
'''

username=input("enter the username: ")
password=input("enter the password: ")
if username=='admin':
    if password=='python123':
        print("Login successful")
    else:
        print("Incorrect Password")
else:
    print("Incorrect Username")

#task-2
'''
accept age,monthly salary,credit score,loan is approved only if :
*age>=21
*salary >=30000
*credit score>=700
otherwise,print loan rejected
'''

age=int(input("enter the age: "))
salary=int(input("enter the salary: "))
credit_score=int(input("enter the credit score: "))
if age>=21 and salary>=30000 and credit_score>=700:
    print("Loan approved")
else:
    print("Loan rejected")

#right angle triangle          
for row in range(5):
    for col in range(row):
            print("*", end="") #end="" end of line
    print() #\n(new line)


x=65
for i in range(5):
    print(chr(x),end="")
    x+=1

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




    
    

       


