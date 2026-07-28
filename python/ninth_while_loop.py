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
    
