#Dictonary

'''
dictonary is mutable datatype , which is both
ordered and unordered based on the version,
keys can be duplicated , but not the values
'''
'''
#Creating an empty dictonary without inbuilt elements
dic={}
print(type(dic))

#Creating an empty dictonary with inbuilt elements
dict=dict()
print(type(dict))


#Syntax of dictonay
#dictoanry_name={key1:value1,key2:value2,key3:value3,...}

#Program 1
dicto={1:"a",2:"b",3:"c"}
for i in dic:
    print(i)

#Progarm 2
dic={ 1:"a",2:"b",3:"c"}
print(dic.values())
print(dic.keys())
print(dic[2])#to print b we used key 2
print(dic.pop(2))#we have to mention the key to pop funtion empty pop wont work

#Program 3
#dict1={1:"a",2:"b",3:"c"}
#O/p--> dict2={"a":1,"b":2,"c":3}
dict1={1:"a",2:"b",3:"c"}
dict2={}
for key,values in dict1:


word="banana"
{"b":1,"a":3,"n":2}
'''
#Using dictonary comprehension
word = "banana"
new={i:word.count(i)for i in word }
print(new)

#Without using dictonary comprehension
word = "banana"
new={}
for i in word:
    new[i]=word.count(i)
print(new)  
  


