#Print 
#M1
lst = [1, 2, 3, [22, 55], 4, 5]
normal_list = []
nested_list = []
for i in lst:
    if type(i) == list:
        nested_list = i
    else:
        normal_list.append(i)
print(normal_list)
print(nested_list)

#M2
lst = [1, 2, 3, [22, 55], 4, 5]
i=0
lst1=[]
while i <=5:
    if(i==3):
        i+=1
        continue
    else:
        lst1.append(list[i])
    i+=1
print(lst)

#Print the 2nd largest number from the list
a=[1,2,6,4,5]
largest=second_largest=a[0]
for i in a :
    if i>largest:
        sec_largest=largest
        largest=i
    elif i > second_largest and i != largest:
         sec_largest=i
print("Second Largest=",sec_largest)        
        
        
        
        
    
    
