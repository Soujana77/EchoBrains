#Looping statements
#for loop
'''
syntax
for variable in seq:
staement
'''
for i in "hello":
    print(i)

#range(start,stop,step) -stop is optional,-step means skipping the value
for i in range(1,10,5):
    print(i)
    
for i in range(1,5):
    print(i)

for i in range(5):
    print(i)
#___________________________

for i in range(0,5,2):
    print(i)

#____________________________

for i in range(6):
    print(5*"*")

for i in range(6):
    print(5*" *")

#using for loop print 5,4,3,2,1,0
#using for loop print 5 table eg : 5X1=5,5X2=10....5X10=50
#using for loop print the number from 1 to 10 where every even number should say hi i am 2 , hi i am 4 till the last even number for given range    
'''
print this pattern        ****  using for loop
                          *  *
                          *  *
                          ****
                          '''
#USING IF IN FOR


#using for loop print 5,4,3,2,1,0

for i in range(5,-1,-1):
    print(i)

#using for loop print 5 table eg : 5X1=5,5X2=10....5X10=50

for i in range(1,11):
    print("5 X ",i,"=",5*i)


