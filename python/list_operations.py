#OPERATIONS ON LIST
#insert function

lst=[1,2,3,4]
lst.insert(1,2)#var.insert(index,val)
print(lst)

#remove function
lst=[1,2,3,4]
#lst.insert(1,2)#list.remove(val)
lst.remove(1)
print(lst)

#pop function
lst=[1,2,3,4]
#removes the last element of the list 
lst.pop(2)

#INBUILT FUNCTIONS 
print(max(lst))
print(min(lst))
print(len(lst))

lst=[1,2,3,4,5,6,7]
max=0
for i in lst:
    if (i>max):
        max = i
print(max)

min=0
for i in lst:
    if(i<min):
        min=i
print(min)

#List comprehension-consicing the program
list=[1,2,3,4]
#new=[exp for var in seq in condition]
new=[i**2 for i in list]
print(new)

#printing even numbers from list using list comprehension 
list=[1,2,3,4]
new=[i for i in list if i%2==0]
print(new)


#list=[10,20,30,45,59,60]
#o/p =[10,30,45,60]
list=[10,20,30,45,59,60]
val_to_rem=[20,59]
new_lst=[i for i in list if i not in val_to_rem]
print(new_lst)

        
    
