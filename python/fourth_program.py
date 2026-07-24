#swaping the values of 2 variables without using using the third variable
a=2
b=4
a,b=b,a
print(a)
print(b)

#Operators
#Arithmatic Operators :(+,-,*,/,//,**)
print("Started arithmatic operators")
a=2
b=4
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b",a*b)
print("a/b",a/b)
print("a//b",a//b)
print("a**b",a**b)
print("a%b",a%b)



'''
task get a integer input for variable a,b,c
multiply all 3 variables(a*b*c)
add all 3 variable(a+b+c)
divide the multiplied value by added values print it
'''


a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))
c = int(input("Enter the value of c = "))

mul = a * b * c
add = a + b + c

print("Multiplication =", mul)
print("Addition =", add)
print("Division =", mul / add)


#Assignment operator : (+=,-=,*=,/=,//=,**=)
x=1
x+=4 #x=x+1
print(x)

y=2
y-=2 #y=y-2
print(y)

z=4
z*=3 #z=z*3
print(z)

w=9
w/=4 #w=w/4
print(w)

u=6
u//=5 #u=u//5
print(u)

v=7
v**=2 #v=v**2
print(v)

#Bitwise operator (&,|,^,~,>>,<<)
'''
0000 - 0
0001 - 1
0010 - 2
0011 - 3
0100 - 4
0101 - 5
0110 - 6
0111 - 7
1000 - 8
1001 - 9
1010 - 10
1011 - 11
1100 - 12
1101 - 13
1110 - 14
1111 - 15
'''

'''
and gate
x y x&y
0 0  0
0 1  0
1 0  0
1 1  1
'''
print(4 & 6)
'''
0100 -> 4
0110 -> 6
_________
0100 -> 4
'''

'''
or gate
x y x*y
0 0  0
0 1  1
1 0  1
1 1  1
'''
print(4 | 6)
'''
0100 -> 4
0110 -> 6
_________
0110 -> 6
'''


#Left shift and Right shift
print(2>>1) #right shift
'''
8421
0010# 2 in binary
____
00010
'''
print(15>>3)

print(11<<4)

print(13>>3)

print(16>>5)



#negation
print(~7)
'''
~ = -(n+1)
    -(7+1)
    -8
    '''

#Comparision Operators(==,<=,>=,!=,<,>)

x=3
y=8
print(x==y)
print(x!=y)
print(x<=y)
print(x>=y)
print(x>y)
print(x<y)

#Logical operator(anf,or,not)
'''
and gate
x y x*y
0 0  0
0 1  0
1 0  0
1 1  1
'''
x=3
y=8
print(x==y and x!=y)

'''
or gate
x y x*y
0 0  0
0 1  1
1 0  1
1 1  1
'''
print(x==y and x!=y)

x=3
y=8
print(x==y and x!=y or x>=y and x<=y) #order wise execution

'''
not gate
x ~x
0 1
1 0
'''
x=3
y=8
print(not(x==y))









      
