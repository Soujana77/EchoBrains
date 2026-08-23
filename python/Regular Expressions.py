#Regular Expressions ->
'''
Finding the pattern in a particular strings,
matching text searching data validation (email or phone numbers )
extracting information from large datasets ,
and formatting or replacing text in files.
'''
#we will use packages to implement regular expression
#A package is a folder containg n number of modules(files) in the folder, the folder must contain
'''
search - anywhere
match - first 
find - findall
sub -replace
'''

import re
text = "My science marks is 99 and maths marks is 97"
result = re.findall(r"\d+",text)
result1 = re.findall(r"\d",text)
result2 = re.sub(r"\d+", "100",text)
result3 = re.match("python",text)
print(result)
print(result1)
print(result2)
print(result3)

#find the fisrt number text = "my age is 25" Use re.search() to find and print 25


 
