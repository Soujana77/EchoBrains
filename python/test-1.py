#Sum of 1 to n without any inbuilt function ,user has to enter the number

'''sum=0
num=int(input("Enter a number between 1 to 100"))
sum=(num+1)/2
print("Sum=",sum)
'''
'''
sum=0
a=int(input("enter a number: "))
for i in range(1,a+1):
    sum += i
print(sum)

#Reverse a string without using any inbuilt function
word="String"
new_word=""
for i in word:
    new_word=i+new_word
print(new_word)
'''
#Reverse a string without using while loop
str="hello"
n_str=""
i=0
while i< len(str):
    n_str=str[i]+n_str
    i+=1
print(n_str)    

'''
a=input("Enter a string")
n_a=""
for i in a:
    n_a=i+n_a
print(n_a)    
   ''' 
    
