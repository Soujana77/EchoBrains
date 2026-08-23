'''
Task 1 
find the first number 
Given : 
test= "My age is 25"
Use re.search() to find and print 25
'''

'''
Task-2 
Check the starting word 
Given:
text = "Python is easy"
Use re.match to check whether the string starts with "Python".
Expected O/P : Python

'''

'''
Task - Find all numbers
Given:
text = "I have 2 pens 5 books and 10 pencils"
use re.findall to extract all numbers"
Expected O/P : ['2','5','10']
'''
'''
Task - 4
Find all email addresses
text="Contact as at abc@gmail.com or supoort@yahoo.com"
use re.findall() to extract all email addresses
Expected O/P : ['abc@gmail.com ','supoort@yahoo.com']

'''

#Task 1 Solution
import re
text = "My age is 25"
result =  re.search(r"\d",text)
print(result)