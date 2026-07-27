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
'''
username=input("enter the username: ")
password=input("enter the password: ")
if username=='admin':
    if password=='python123':
        print("Login successful")
    else:
        print("Incorrect Password")
else:
    print("Incorrect Username")'''

#task-2
'''
accept age,monthly salary,credit score,loan is approved only if :
*age>=21
*salary >=30000
*credit score>=700
otherwise,print loan rejected
'''
age=input("enter the age")
salary=input("enter the salary")
credit_score=input("enter the credit score")
if age>=21 and salary>=30000 and credit_score>=700:
    print("Loan approved")
else:
    print("Loan rejected")
          
